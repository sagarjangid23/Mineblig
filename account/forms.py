from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


# This form class is used to create a new user.
class SignUpForm(UserCreationForm):
  password2 = forms.CharField(label='Password (again)',widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email']
    labels = {'email':'Email'}


#This class is used to edit the users(active users) profile details
class EditUserProfileForm(UserChangeForm):
  password = None
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email','date_joined','last_login']
    labels = {'email':'Email'}


#This class is used to edit the admins(superusers) profile details.
class EditAdminUserProfileForm(UserChangeForm):
  password = None
  class Meta:
    model = User
    fields = '__all__'
    labels = {'email':'Email'}