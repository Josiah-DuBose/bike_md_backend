from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from .models import Tech


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class TechForm(forms.ModelForm):

    class Meta:
        model = Tech
        fields = ['experience', 'job_title', 'shop']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=4, label="Username")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=5, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length=5, label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError(
            "The username %s is already taken." % username)

    def clean(self):
        password = self.cleaned_data.get("password", None)
        confirm_password = self.cleaned_data.get("confirm_password", None)
        if password == confirm_password:
            return self.cleaned_data

        raise forms.ValidationError("The passwords do not match.")
