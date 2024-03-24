from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, PasswordResetForm, UsernameField
from django.contrib.auth.models import User
from .models import Admin,Staff,Faculty_user, Department,Faculty,Room,Time_Schedule,Course,Department_Course,Instructor_Course
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


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['FacultyIdNo','FacultyName','Gender','Position','Designation','DeloadUnit','Department']
        widgets = {
            'FacultyName':forms.HiddenInput(),
            'FacultyIdNo': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Id No.'}),
            'Gender': forms.TextInput(attrs={'rows': 3, 'class': 'form-control-sm', 'placeholder': 'Select Gender'}),
            'Position': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Position'}),
            'Designation': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Designatin'}),
            'DeloadUnit': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Deload Unit'}),
            'Department': forms.Select(attrs={'class':'form-control-sm', 'placeholder': 'Select Department'}),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['Number','Capacity']

class Time_ScheduleForm(forms.ModelForm):
    class Meta:
        model = Time_Schedule
        fields = ['Schedule',]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['Course_Code','Descriptive_Title','Unit_Lec','Unit_Lab','Credit_Unit','Hours_Lec','Hours_Lab']

class Department_CourseForm(forms.ModelForm):
    class Meta:
        model = Department_Course
        fields = ['Department','Course']

class Instructor_CourseForm(forms.ModelForm):
    class Meta:
        model = Instructor_Course
        fields = ['Course','Instructor']