from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
   email = models.CharField(max_length=60)
   access = models.IntegerField(default=0)

class classes(models.Model):
   class_names = models.CharField(max_length=60,default='')

   def __str__(self):
      return self.class_names

class students(models.Model):
   name = models.CharField(max_length=60)
   age = models.IntegerField(default=0)
   fathername = models.CharField(max_length=60)
   contact_number = models.IntegerField(default=0)
   class_name = models.ForeignKey(classes,on_delete=models.CASCADE)
   school_name = models.ForeignKey(User,on_delete=models.CASCADE)

   def __str__(self):
      return self.name
   
class staff(models.Model):
   name = models.CharField(max_length=60,default='',blank=True,null=True)
   phonenumber = models.IntegerField(default=0)
   department = models.CharField(max_length=70)
   school_name = models.ForeignKey(User,on_delete=models.CASCADE,default='')

   def __str__(self):
      return self.name


   

class staff_files(models.Model):
   
   description = models.CharField(max_length=100,default='')
   file = models.FileField(upload_to='')
   staff_name = models.ForeignKey(staff,on_delete=models.CASCADE,default='',null=True)

   def __str__(self):
      return self.description
