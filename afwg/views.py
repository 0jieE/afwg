from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.contrib.auth import logout,authenticate, login, update_session_auth_hash
from django.http import HttpResponse, JsonResponse
from .forms import AdminRegistrationForm, StaffRegistrationForm, FacultyRegistrationForm, LoginForm, DepartmentForm, FacultyForm
from django.contrib.auth import views as auth_views
from .models import User, Department, Faculty

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
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})

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


#///////////////////////////////CRUDE/////////////////////////////////////////////////////////////

#________________________________________________________________________________________________________


                        #------------department Views---------------#

#________________________________________________________________________________________________________


def department(request):
        departments = Department.objects.all()
        return render(request, 'pages/list/department/department.html',{'departments':departments})

def add_department(request):
        if(request.method == 'POST'):
                form = DepartmentForm(request.POST)
        else:    
                form = DepartmentForm()

        return save_department(request, form, 'pages/list/department/add_department.html')


def edit_department(request,pk):
        department = get_object_or_404(Department, pk=pk)
        if(request.method == 'POST'):
                form = DepartmentForm(request.POST, instance=department)
        else:    
                form = DepartmentForm(instance=department)
        return save_department(request, form, 'pages/list/department/edit_department.html')


def delete_department(request,pk):
        department = get_object_or_404(Department, pk=pk)
        data = dict()
        if request.method == 'POST':
            department.delete()
            data['form_is_valid'] = True
            departments= Department.objects.all()
            data['department_list'] = render_to_string('pages/list/department/department_list.html',{'departments':departments})
        else:    
            context = {'department':department}
            data['html_form'] = render_to_string('pages/list/department/delete_department.html',context,request=request)
        return JsonResponse(data)


def save_department(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        form = DepartmentForm(request.POST,)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            departments= Department.objects.all()
            data['department_list'] = render_to_string('pages/list/department/department_list.html', {'departments':departments})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Faculty Views---------------#

#________________________________________________________________________________________________________


def faculty(request):
    faculties = Faculty.objects.all()
    return render(request, 'pages/list/faculty/faculty.html',{'faculties':faculties})


def edit_faculty(request,pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if(request.method == 'POST'):
            form = FacultyForm(request.POST, instance=faculty)
            print(2)
    else:    
            form = FacultyForm(instance=faculty)
    return save_faculty(request, form, 'pages/list/faculty/faculty.html')


def delete_faculty(request,pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    data = dict()
    if request.method == 'POST':
        faculty.delete()
        data['form_is_valid'] = True
        faculties= Faculty.objects.all()
        data['faculty_list'] = render_to_string('pages/list/faculty/faculty_list.html',{'faculties':faculties})
    else:    
        context = {'faculty':faculty}
        data['html_form'] = render_to_string('pages/list/faculty/faculty.html',context,request=request)
    return JsonResponse(data)


def save_faculty(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            faculties= Faculty.objects.all()
            data['faculty_list'] = render_to_string('pages/list/faculty/faculty_list.html', {'faculties':faculties})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

