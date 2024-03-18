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
    path('staff-user/',views.admin_user, name='staff-user'),
    path('faculty-user/',views.admin_user, name='faculty-user'),

]
