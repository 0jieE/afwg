from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    faculty = models.BooleanField(default=False)


    def __str__(self):
        template = '{0.first_name} {0.middle_name} {0.last_name}'
        return template.format(self)

class Admin_user_Manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(admin=True)
    
class Admin(User):

    user = Admin_user_Manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.admin = True
            self.staff = False
            self.faculty = False
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False
            
            return super().save(*args, **kwargs)
    
    def welcome(self):
        return "Only for admin user"
    
class Staff_user_Manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(staff=True)
    
class Staff(User):

    user = Staff_user_Manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.admin = False
            self.staff = True
            self.faculty =False
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False
            
            return super().save(*args, **kwargs)
    
    def welcome(self):
        return "Only for staff user"
    
class Faculty_user_Manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(faculty=True)
    
class Faculty_user(User):

    user = Faculty_user_Manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.admin = False
            self.staff = False
            self.faculty = True
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False
            
            return super().save(*args, **kwargs)
    
    def welcome(self):
        return "Only for faculty user"
    
@receiver(post_save, sender= Faculty_user)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.faculty == True:
        Faculty.objects.create(FacultyName=instance)
    
class Department(models.Model):
    DepartmentName = models.CharField(max_length = 50)
    DepartmentHead = models.CharField(max_length = 50)

    def __str__(self):
        template = '{0.DepartmentName}'
        return template.format(self)

class Faculty(models.Model):
    FacultyIdNo = models.CharField(max_length=50, null= True, blank = True)
    FacultyName = models.ForeignKey(User, related_name = 'FUname',on_delete = models.CASCADE)
    Gender = models.CharField(max_length = 50, null =True, blank = True)
    Position = models.CharField(max_length = 50, null = True, blank = True)
    Designation = models.CharField(max_length = 50, blank =True)
    DeloadUnit = models.IntegerField(null =True, blank = True)
    Department = models.ForeignKey(Department, related_name = 'FDepartment', on_delete = models.CASCADE, null =True, blank = True)

    def __str__(self):
        template = '{0.FacultyIdNo} {0.FacultyName}'
        return template.format(self)

class Room(models.Model):
    Number = models.CharField(max_length=20)
    Capacity = models.CharField(max_length=20)

class Time_Schedule(models.Model):
    Schedule = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.Schedule}'
        return template.format(self)

class Course(models.Model):
    Course_Code = models.CharField(max_length = 50)
    Descriptive_Title = models.CharField(max_length = 50)
    Unit_Lec = models.IntegerField(default = 0)
    Unit_Lab = models.IntegerField(default = 0)
    Credit_Unit = models.IntegerField(default = 0)
    Hours_Lec = models.DecimalField(max_digits = 4, decimal_places = 2, default = 0.0)
    Hours_Lab = models.DecimalField(max_digits = 4, decimal_places = 2, default = 0.0)

    def __str__(self):
        template = '{0.Course_Code}-{0.Descriptive_Title}'
        return template.format(self)

class Department_Course(models.Model):
    Department = models.ForeignKey(Department,related_name='department_name', on_delete=models.CASCADE)
    Course = models.ForeignKey(Course,related_name = 'course_name', on_delete=models.CASCADE)

class Instructor_Course(models.Model):
    Course = models.ForeignKey(Course,related_name = 'intructor_course', on_delete=models.CASCADE, null=True, blank=True)
    Instructor = models.ForeignKey(Faculty, related_name = 'course_intructor_name', on_delete=models.CASCADE)