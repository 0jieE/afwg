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

]
