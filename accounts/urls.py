from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('helpless_register/', views.helpless_register, name='helpless_register'),
    path('donor_register/', views.donor_register, name='donor_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_dtls/', views.profile_dtls, name='profile_dtls'),
    path('Dash/', views.Dash.as_view(), name="Dash"),
    path('staffDash/', views.staffDash.as_view(), name="staffDash"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('ComplainBox/', views.ComplainBox.as_view(), name="ComplainBox"),
    path('createOTP/', views.createOTP, name='createOTP'),
    path('confirm_otp/', views.confirm_otp, name='confirm_otp'),
    path('Post_blog/', views.Post_blog.as_view(), name='Post_blog'),
    path('applyRelief/', views.applyRelief, name='applyRelief'),
    path('donation/', views.donation, name='donation'),
]
