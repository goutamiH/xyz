from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django.contrib.auth.models import User
from django.db import models
# Create your forms here.
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class Room_Form(forms.ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']

class contact_Us_Form(forms.ModelForm):
	class Meta:
		model=contact_us_model
		fields='__all__'

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields = '__all__'

class Dairy_Writing_Form(forms.ModelForm):
	class Meta:
		model=Diary_Writing
		fields="__all__"

class StoryForm(forms.ModelForm):
	class Meta:
		model=ShareStory
		fields="__all__"