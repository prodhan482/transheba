from django.contrib import auth, messages
from django.shortcuts import render, redirect
from accounts.forms import UserForm, DonorProfileInfoForm, HelplessProfileInfoForm, UserUpdateForm,applyReliefForm,donationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.views.generic import TemplateView
from accounts.models import HelplessProfile
from sheba.models import ComplainBox, Contact,post
from django.views.generic import CreateView
from .forms import AccountAuthenticationForm
from django.core.files.storage import FileSystemStorage


def login_view(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        if user.is_employee:
            return render(request, 'staffDash.html')
        else:
            return render(request, 'dashboard.html')
    else:
        if request.POST:
            form = AccountAuthenticationForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    if user.is_employee:
                        return render(request, 'staffDash.html')
                    else:
                        return render(request, 'dashboard.html')
                else:
                    return redirect("/login/")
        else:
            form = AccountAuthenticationForm()
        context['login_form'] = form
        return render(request, 'login.html', context)




def logout(request):
    auth.logout(request)
    return redirect('login')


def helpless_register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = HelplessProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.is_active = True
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # registered = True
            return redirect('login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = HelplessProfileInfoForm()

    return render(request, 'helpless_register.html',
                  {'registered': registered,
                   'user_form': user_form,
                   'profile_form': profile_form})


def donor_register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = DonorProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.is_donor = True
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # registered = True
            return redirect('login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = DonorProfileInfoForm()

    return render(request, 'donor_register.html',
                  {'registered': registered,
                   'user_form': user_form,
                   'profile_form': profile_form})





class ComplainBox(CreateView):
    model = ComplainBox
    fields = '__all__'
    template_name = 'ComplainBox.html'


def createOTP(request):
    return render(request, 'otp_form.html')

def confirm_otp(request):
    return render(request, 'confirm_otp.html')

@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = HelplessProfileInfoForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = HelplessProfileInfoForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'UpdateProfile.html', context)

@login_required
def applyRelief(request):
    if request.method == "POST":
        relief_form = applyReliefForm(data=request.POST)

        if relief_form.is_valid():
            relief = relief_form.save()
            relief.save()

            return redirect('Dash')
        else:
            print(relief_form.errors)
    else:
        relief_form = applyReliefForm()

    return render(request, 'applyForRelief.html',
                  {'relief_form': relief_form})


@login_required
def donation(request):
    if request.method == "POST":
        donate_form = donationForm(data=request.POST)

        if donate_form.is_valid():
            donate = donate_form.save()
            donate.save()

            return redirect('/Dash/')
        else:
            print(donate_form.errors)
    else:
        donate_form = donationForm()

    return render(request, 'donation.html',
                  {'donate_form': donate_form})



@login_required
def profile_dtls(request):
    return render(request, 'profile.html')

class Home(TemplateView):
    template_name = 'home.html'

class Dash(TemplateView):
    template_name = 'dashboard.html'

class staffDash(TemplateView):
    template_name = 'staffDash.html'

class Contact(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'contact.html'

class password_reset(CreateView):
    template_name = 'password_reset_form.html'

class Post_blog(CreateView):
    model = post
    fields = '__all__'
    template_name = 'post.html'