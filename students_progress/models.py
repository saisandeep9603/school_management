from django.db import models
from schools.models import *


class subjects(models.Model):
    subject_names = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_names

class students_marks(models.Model):
    student_name = models.ForeignKey(students,on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
    sub_name = models.ForeignKey(subjects,on_delete=models.CASCADE)

    
    

