from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.contrib.auth import logout,authenticate, login, update_session_auth_hash
from django.http import HttpResponse, JsonResponse
from .forms import AdminRegistrationForm, StaffRegistrationForm, FacultyRegistrationForm, LoginForm, DepartmentForm, FacultyForm,RoomForm,Time_ScheduleForm,CourseForm,Department_CourseForm,Instructor_CourseForm
from django.contrib.auth import views as auth_views
from .models import User, Department, Faculty,Room,Time_Schedule,Course,Department_Course,Instructor_Course

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
            if request.user.admin:
                 data['department_list'] = render_to_string('pages/list/department/department_list_admin.html',{'departments':departments})
            elif request.user.staff: 
                data['department_list'] = render_to_string('pages/list/department/department_list_staff.html',{'departments':departments})
        else:    
            context = {'department':department}
            data['html_form'] = render_to_string('pages/list/department/delete_department.html',context,request=request)
        return JsonResponse(data)


def save_department(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        departments= Department.objects.all()
        if request.user.admin:
            data['department_list'] = render_to_string('pages/list/department/department_list_admin.html',{'departments':departments})
        elif request.user.staff: 
            data['department_list'] = render_to_string('pages/list/department/department_list_staff.html',{'departments':departments})
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
    else:    
            form = FacultyForm(instance=faculty)
    return save_faculty(request, form, 'pages/list/faculty/edit_faculty.html')


def delete_faculty(request,pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    data = dict()
    if request.method == 'POST':
        faculty.delete()
        data['form_is_valid'] = True
        faculties= Faculty.objects.all()
        if request.user.admin:
            data['department_list'] = render_to_string('pages/list/faculty/faculty_list_admin.html',{'faculties':faculties})
        elif request.user.staff: 
            data['department_list'] = render_to_string('pages/list/faculty/faculty_list_staff.html',{'faculties':faculties})
    else:    
        context = {'faculty':faculty}
        data['html_form'] = render_to_string('pages/list/faculty/delete_faculty.html',context,request=request)
    return JsonResponse(data)


def save_faculty(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        faculties= Faculty.objects.all()
        if request.user.admin:
            data['faculty_list'] = render_to_string('pages/list/faculty/faculty_list_admin.html',{'faculties':faculties})
        elif request.user.staff: 
            data['faculty_list'] = render_to_string('pages/list/faculty/faculty_list_staff.html',{'faculties':faculties})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Room Views---------------#

#________________________________________________________________________________________________________


def room(request):
        rooms = Room.objects.all()
        return render(request, 'pages/list/room/room.html',{'rooms':rooms})

def add_room(request):
        if(request.method == 'POST'):
                form =RoomForm(request.POST)
        else:    
                form =RoomForm()

        return save_room(request, form, 'pages/list/room/add_room.html')


def edit_room(request,pk):
        room = get_object_or_404(Room, pk=pk)
        if(request.method == 'POST'):
                form =RoomForm(request.POST, instance=room)
        else:    
                form =RoomForm(instance=room)
        return save_room(request, form, 'pages/list/room/edit_room.html')


def delete_room(request,pk):
        room = get_object_or_404(Room, pk=pk)
        data = dict()
        if request.method == 'POST':
            room.delete()
            data['form_is_valid'] = True
            rooms= Room.objects.all()
            if request.user.admin:
                 data['room_list'] = render_to_string('pages/list/room/room_list_admin.html',{'rooms':rooms})
            elif request.user.staff: 
                data['room_list'] = render_to_string('pages/list/room/room_list_staff.html',{'rooms':rooms})
        else:    
            context = {'room':room}
            data['html_form'] = render_to_string('pages/list/room/delete_room.html',context,request=request)
        return JsonResponse(data)


def save_room(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        rooms= Room.objects.all()
        if request.user.admin:
            data['room_list'] = render_to_string('pages/list/room/room_list_admin.html',{'rooms':rooms})
        elif request.user.staff: 
            data['room_list'] = render_to_string('pages/list/room/room_list_staff.html',{'rooms':rooms})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Time Schedule Views---------------#

#________________________________________________________________________________________________________


def schedule(request):
        schedule = Time_Schedule.objects.all()
        return render(request, 'pages/list/schedule/schedule.html',{'schedule':schedule})

def add_schedule(request):
        if(request.method == 'POST'):
                form =Time_ScheduleForm(request.POST)
        else:    
                form =Time_ScheduleForm()

        return save_schedule(request, form, 'pages/list/schedule/add_schedule.html')


def edit_schedule(request,pk):
        schedule = get_object_or_404(Time_Schedule, pk=pk)
        if(request.method == 'POST'):
                form =Time_ScheduleForm(request.POST, instance=schedule)
        else:    
                form =Time_ScheduleForm(instance=schedule)
        return save_schedule(request, form, 'pages/list/schedule/edit_schedule.html')


def delete_schedule(request,pk):
        schedule = get_object_or_404(Time_Schedule, pk=pk)
        data = dict()
        if request.method == 'POST':
            schedule.delete()
            data['form_is_valid'] = True
            schedule= Time_Schedule.objects.all()
            if request.user.admin:
                 data['schedule_list'] = render_to_string('pages/list/schedule/schedule_list_admin.html',{'schedule':schedule})
            elif request.user.staff: 
                data['schedule_list'] = render_to_string('pages/list/schedule/schedule_list_staff.html',{'schedule':schedule})
        else:    
            context = {'schedule':schedule}
            data['html_form'] = render_to_string('pages/list/schedule/delete_schedule.html',context,request=request)
        return JsonResponse(data)


def save_schedule(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        schedule= Time_Schedule.objects.all()
        if request.user.admin:
            data['schedule_list'] = render_to_string('pages/list/schedule/schedule_list_admin.html',{'schedule':schedule})
        elif request.user.staff: 
            data['schedule_list'] = render_to_string('pages/list/schedule/schedule_list_staff.html',{'schedule':schedule})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#________________________________________________________________________________________________________


                        #------------Course Views---------------#

#________________________________________________________________________________________________________


def course(request):
    courses = Course.objects.all()
    return render(request, 'pages/list/course/course.html',{'courses':courses})

def add_course(request):
        if(request.method == 'POST'):
                form =CourseForm(request.POST)
        else:    
                form =CourseForm()

        return save_course(request, form, 'pages/list/course/add_course.html')


def edit_course(request,pk):
    course = get_object_or_404(Course, pk=pk)
    if(request.method == 'POST'):
            form = CourseForm(request.POST, instance=course)
    else:    
            form = CourseForm(instance=course)
    return save_course(request, form, 'pages/list/course/edit_course.html')


def delete_course(request,pk):
    course = get_object_or_404(Course, pk=pk)
    data = dict()
    if request.method == 'POST':
        course.delete()
        data['form_is_valid'] = True
        courses= Course.objects.all()
        if request.user.admin:
            data['department_list'] = render_to_string('pages/list/course/course_list_admin.html',{'courses':courses})
        elif request.user.staff: 
            data['department_list'] = render_to_string('pages/list/course/course_list_staff.html',{'courses':courses})
    else:    
        context = {'course':course}
        data['html_form'] = render_to_string('pages/list/course/delete_course.html',context,request=request)
    return JsonResponse(data)


def save_course(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        courses= Course.objects.all()
        if request.user.admin:
            data['course_list'] = render_to_string('pages/list/course/course_list_admin.html',{'courses':courses})
        elif request.user.staff: 
            data['course_list'] = render_to_string('pages/list/course/course_list_staff.html',{'courses':courses})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#________________________________________________________________________________________________________


                        #------------Department Course Views---------------#

#________________________________________________________________________________________________________


def department_course(request):
    department_course = Department_Course.objects.all()
    return render(request, 'pages/list/department_course/department_course.html',{'department_course':department_course})

def add_department_course(request):
        if(request.method == 'POST'):
                form =Department_CourseForm(request.POST)
        else:    
                form =Department_CourseForm()

        return save_department_course(request, form, 'pages/list/department_course/add_department_course.html')


def edit_department_course(request,pk):
    department_course = get_object_or_404(Department_Course, pk=pk)
    if(request.method == 'POST'):
            form = Department_CourseForm(request.POST, instance=department_course)
    else:    
            form = Department_CourseForm(instance=department_course)
    return save_department_course(request, form, 'pages/list/department_course/edit_department_course.html')


def delete_department_course(request,pk):
    department_course = get_object_or_404(Department_Course, pk=pk)
    data = dict()
    if request.method == 'POST':
        department_course.delete()
        data['form_is_valid'] = True
        department_course= Department_Course.objects.all()
        if request.user.admin:
            data['department_course_list'] = render_to_string('pages/list/department_course/department_course_list_admin.html',{'department_course':department_course})
        elif request.user.staff: 
            data['department_course_list'] = render_to_string('pages/list/department_course/department_course_list_staff.html',{'department_course':department_course})
    else:    
        context = {'department_course':department_course}
        data['html_form'] = render_to_string('pages/list/department_course/delete_department_course.html',context,request=request)
    return JsonResponse(data)


def save_department_course(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        department_course= Department_Course.objects.all()
        if request.user.admin:
            data['department_course_list'] = render_to_string('pages/list/department_course/department_course_list_admin.html',{'department_course':department_course})
        elif request.user.staff: 
            data['department_course_list'] = render_to_string('pages/list/department_course/department_course_list_staff.html',{'department_course':department_course})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Instructor Course Views---------------#

#________________________________________________________________________________________________________


def instructor(request):
    instructors = Instructor_Course.objects.all()
    return render(request, 'pages/list/instructor/instructor.html',{'instructors':instructors})

def add_instructor(request):
        if(request.method == 'POST'):
                form =Instructor_CourseForm(request.POST)
        else:    
                form =Instructor_CourseForm()

        return save_instructor(request, form, 'pages/list/instructor/add_instructor.html')


def edit_instructor(request,pk):
    instructor = get_object_or_404(Instructor_Course, pk=pk)
    if(request.method == 'POST'):
            form = Instructor_CourseForm(request.POST, instance=instructor)
    else:    
            form = Instructor_CourseForm(instance=instructor)
    return save_instructor(request, form, 'pages/list/instructor/edit_instructor.html')


def delete_instructor(request,pk):
    instructor = get_object_or_404(Instructor_Course, pk=pk)
    data = dict()
    if request.method == 'POST':
        instructor.delete()
        data['form_is_valid'] = True
        instructors = Instructor_Course.objects.all()
        if request.user.admin:
            data['instructor_list'] = render_to_string('pages/list/instructor/instructor_list_admin.html',{'instructors':instructors})
        elif request.user.staff: 
            data['instructor_list'] = render_to_string('pages/list/instructor/instructor_list_staff.html',{'instructors':instructors})
    else:    
        context = {'instructor':instructor}
        data['html_form'] = render_to_string('pages/list/instructor/delete_instructor.html',context,request=request)
    return JsonResponse(data)


def save_instructor(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            instructors = Instructor_Course.objects.all()
            if request.user.admin:
                data['instructor_list'] = render_to_string('pages/list/instructor/instructor_list_admin.html',{'instructors':instructors})
            elif request.user.staff: 
                data['instructor_list'] = render_to_string('pages/list/instructor/instructor_list_staff.html',{'instructors':instructors})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
