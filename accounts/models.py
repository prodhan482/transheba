from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email address is required for users.")
        if not username:
            raise ValueError("Username is required for users.")

        user = self.model(email=self.normalize_email(email),
                          username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email),
                                username=username, password=password)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_helpless = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # used for login -_-
    REQUIRED_FIELDS = ['email', ]

    objects = UserAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)


class HelplessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    profile_pic = models.ImageField(
        default='default.png', upload_to=path_and_rename, verbose_name="Profile Picture")
    # profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    male = 'Male'
    female = 'Female'
    Gender = [
        (male, 'Male'),
        (female, 'Female'),
    ]
    Gender = models.CharField(max_length=10, choices=Gender, default=male)
    is_helpless = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    profile_pic = models.ImageField(
        upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    male = 'Male'
    female = 'Female'
    Gender = [
        (male, 'Male'),
        (female, 'Female'),
    ]
    Gender = models.CharField(max_length=10, choices=Gender, default=male)
    is_donor = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staffID = models.IntegerField(unique=True, null=True)
    phone_number = models.CharField(max_length=11)
    profile_pic = models.ImageField(
        upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    male = 'Male'
    female = 'Female'
    Gender = [
        (male, 'Male'),
        (female, 'Female'),
    ]
    Gender = models.CharField(max_length=10, choices=Gender, default=male)
    is_employee = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

