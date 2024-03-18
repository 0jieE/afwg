from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template
from django.contrib.auth import logout,authenticate, login, update_session_auth_hash
from .forms import AdminRegistrationForm, StaffRegistrationForm, FacultyRegistrationForm, LoginForm
from django.contrib.auth import views as auth_views
from .models import User

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                print(2)
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.admin:
                login(request, user)
                return redirect('admin-user/')
            elif user is not None and user.staff:
                login(request, user)
                return redirect('staff-user/')
            elif user is not None and user.faculty:
                login(request, user)
                return redirect('faculty-user/')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def user_logout_view(request):
  logout(request)
  return redirect('login')

#indexes

def admin_user(request):
    
    return render(request, 'admin_user/admin_index.html')

def faculty_user(request):
    
    return render(request, 'faculty_user/faculty_index.html')

def staff_user(request):
    
    return render(request, 'staff_user/staff_index.html')

#register

def register_admin(request):
    msg = None
    success = False

    if request.method == "POST":
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = AdminRegistrationForm()
    
    return render(request, 'admin_user/admin_register.html',{"form": form, "msg": msg, "success": success})

def register_staff(request):
    msg = None
    success = False

    if request.method == "POST":
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = StaffRegistrationForm()
    
    return render(request, 'staff_user/staff_register.html', {"form": form, "msg": msg, "success": success})

def register_faculty(request):
    msg = None
    success = False

    if request.method == "POST":
        form = FacultyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = FacultyRegistrationForm()
    
    return render(request, 'faculty_user/faculty_register.html', {"form": form, "msg": msg, "success": success})