from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Admin,Staff, Faculty_user, Faculty,Room, Time_Schedule, Course, Department_Course, Instructor_Course

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

class faculty_user_config(UserAdmin):
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
admin.site.register(Faculty_user,faculty_user_config)
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display=('FacultyIdNo','FacultyName','Gender','Position','Designation','DeloadUnit','Department')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=('Number','Capacity')

@admin.register(Time_Schedule)
class TimeScheduleAdmin(admin.ModelAdmin):
    list_display=('Schedule',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('Course_Code','Descriptive_Title','Unit_Lec','Unit_Lab','Credit_Unit','Hours_Lec','Hours_Lab')

@admin.register(Department_Course)
class Department_CourseAdmin(admin.ModelAdmin):
    list_display=('Department','Course')

@admin.register(Instructor_Course)
class Instructor_CourseAdmin(admin.ModelAdmin):
    list_display=('Instructor','Course')