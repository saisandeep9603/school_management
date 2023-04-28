from django.db import models
from schools.models import *
from datetime import date
from students_progress.models import *

class notice_uploading(models.Model):
    school_name = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=60,default='')
    date_posted = models.DateField(blank=True)
    content = models.CharField(max_length=500)

    
