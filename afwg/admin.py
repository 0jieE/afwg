from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Admin,Staff, Faculty

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username', 'first_name','last_name')
    list_filter = ('username', 'first_name', 'admin','staff','faculty',)
    ordering = ('username',)
    list_display = ('username', 'first_name','middle_name','last_name',
                    'is_superuser','is_active', 'is_staff','admin','staff','faculty')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','middle_name','last_name',)}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active','admin','staff','faculty')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}),
    )

class admin_config(UserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name','middle_name','last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','middle_name','last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}
         ),
    )

class staff_config(UserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name','middle_name','last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','middle_name','last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}
         ),
    )

class faculty_config(UserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name','middle_name','last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','middle_name','last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}
         ),
    )

admin.site.register(User,UserAdminConfig)
admin.site.register(Admin,admin_config)
admin.site.register(Staff,staff_config)
admin.site.register(Faculty,faculty_config)