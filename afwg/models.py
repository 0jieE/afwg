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

class Faculty(models.Model):
    FacultyIdNo = models.CharField(max_length=50, null= True, blank = True)
    FacultyName = models.ForeignKey(User, related_name = 'FUname',on_delete = models.CASCADE)
    Gender = models.CharField(max_length = 50, null =True, blank = True)
    Position = models.CharField(max_length = 50, null = True, blank = True)
    Designation = models.CharField(max_length = 50, blank =True)
    DeloadUnit = models.IntegerField(null =True, blank = True)
    Department = models.ForeignKey(Department, related_name = 'FDepartment', on_delete = models.CASCADE, null =True, blank = True)

