from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, PasswordResetForm, UsernameField
from django.contrib.auth.models import User
from .models import Admin,Staff,Faculty_user, Department
from django.utils.translation import gettext_lazy as _

class AdminRegistrationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"}))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"}))
    
    class Meta:
        model = Admin
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2')


class StaffRegistrationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"}))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"}))

    class Meta:
        model = Staff
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2')

class FacultyRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"}))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"}))

    class Meta:
        model = Faculty_user
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['DepartmentName','DepartmentHead']
