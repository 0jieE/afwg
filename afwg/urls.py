from django.urls import path
from admin_adminlte import views
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Authentication
    path('register-as-admin', views.register_admin, name='register-admin'),
    path('register-as-staff', views.register_staff, name='register-staff'),
    path('register-as-faculty', views.register_faculty, name='register-faculty'),
    path('',views.login_view, name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('admin-user/',views.admin_user, name='admin-user'),
    path('staff-user/',views.staff_user, name='staff-user'),
    path('faculty-user/',views.faculty_user, name='faculty-user'),

    #Department
    path('department/', views.department, name='department'),
    path('department/add_department/', views.add_department, name='add-department'),
    path('department/<int:pk>/edit/', views.edit_department, name='edit-department'),
    path('department/<int:pk>/delete/', views.delete_department, name='delete-department'),

    #faculty
    path('faculty/', views.faculty, name='faculty'),
    path('faculty/<int:pk>/edit/', views.edit_faculty, name='edit-faculty'),
    path('faculty/<int:pk>/delete/', views.delete_faculty, name='delete-faculty'),

    #room
    path('room/', views.room, name='room'),
    path('room/add_room/', views.add_room, name='add-room'),
    path('room/<int:pk>/edit/', views.edit_room, name='edit-room'),
    path('room/<int:pk>/delete/', views.delete_room, name='delete-room'),

    #Schedule
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/add_schedule/', views.add_schedule, name='add-schedule'),
    path('schedule/<int:pk>/edit/', views.edit_schedule, name='edit-schedule'),
    path('schedule/<int:pk>/delete/', views.delete_schedule, name='delete-schedule'),

    #Course
    path('course/', views.course, name='course'),
    path('course/add_course/', views.add_course, name='add-course'),
    path('course/<int:pk>/edit/', views.edit_course, name='edit-course'),
    path('course/<int:pk>/delete/', views.delete_course, name='delete-course'),

    #Department-Course
    path('department-course/', views.department_course, name='department-course'),
    path('department-course/add_department-course/', views.add_department_course, name='add-department-course'),
    path('department-course/<int:pk>/edit/', views.edit_department_course, name='edit-department-course'),
    path('department-course/<int:pk>/delete/', views.delete_department_course, name='delete-department-course'),

    #Instructor-Course
    path('instructor/', views.instructor, name='instructor'),
    path('instructor/add_instructor/', views.add_instructor, name='add-instructor'),
    path('instructor/<int:pk>/edit/', views.edit_instructor, name='edit-instructor'),
    path('instructor/<int:pk>/delete/', views.delete_instructor, name='delete-instructor'),


]
