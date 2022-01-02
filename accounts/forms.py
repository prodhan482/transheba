from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import authenticate
from accounts.models import HelplessProfile, DonorProfile,User
from sheba.models import applyForRelief, donation



class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2')

        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password'
        }



class HelplessProfileInfoForm(forms.ModelForm):
    is_helpless = True
    male = 'Male'
    female = 'Female'
    Gender = [
        (male, 'Male'),
        (female, 'Female'),
    ]
    Gender = forms.ChoiceField(required=True, choices=Gender)

    class Meta:
        model = HelplessProfile
        fields = ('phone_number', 'profile_pic', 'Gender')


class DonorProfileInfoForm(forms.ModelForm):
    is_donor = True
    male = 'Male'
    female = 'Female'
    Gender = [
        (male, 'Male'),
        (female, 'Female'),
    ]
    Gender = forms.ChoiceField(required=True, choices=Gender)

    class Meta:
        model = DonorProfile
        fields = ('phone_number', 'profile_pic', 'Gender')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email')
class D_form(forms.ModelForm):
    class Meta:
        model = HelplessProfile
        fields = ['phone_number', 'profile_pic', 'Gender']

class applyReliefForm(forms.ModelForm):
    class Meta:
        model = applyForRelief
        fields = ['NID_No', 'Name', 'Distric', 'Village', 'Phone_no','Birth_Date','Marital_Status','ZIP_Code']   


class donationForm(forms.ModelForm):
    class Meta:
        model = donation
        fields = ['Name','Share_something','Phone_no', 'Payment_Method','Area','Marital_Status']






class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Username or password is invalid")

