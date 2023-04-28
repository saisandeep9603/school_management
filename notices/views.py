from django.shortcuts import render,HttpResponse
from schools.models import *
from students_progress.models import *
from .models import *
from datetime import date
def notice_form(request):
    if request.method=="POST":
        school_nam = request.POST['school']
        contents = request.POST['noticess']
        title_of_notice = request.POST['title']
        login_school = request.user
        print(login_school,school_nam)
        if school_nam!=str(login_school):
            return HttpResponse("<h1>Invali School</h1>")
        else:
            school_obj = User.objects.get(username=school_nam)
            new_post = notice_uploading(school_name=school_obj,content=contents,title=title_of_notice,date_posted=date.today())
            new_post.save()
            return HttpResponse("<h1>Notice Uploaded Successfully</h1>")
    
    return render(request,'notice.html')


