from django.shortcuts import render,HttpResponse
from .models import *
from schools.models import *
from django.contrib.auth import get_user_model

User = get_user_model()
def students_marks_submission(request):
    if request.method=="POST":
        classess = request.POST['class_name']
        name_of_student = request.POST['name']
        dept = request.POST['department']
        marks_given = request.POST['marks']

       
        try:
            sub_obj = subjects.objects.get(subject_names=dept)
            class_obj = classes.objects.get(class_names=classess)
            student_obj = students.objects.get(name= name_of_student)
            student_class = students.objects.filter(class_name=class_obj)
            print(class_obj,student_obj,student_class)
            previous = students_marks.objects.filter(student_name=student_obj,sub_name=sub_obj)
            #print("marls",previous.values())
            if previous:
                return HttpResponse("<h1>already recorded data!!</h1>")
            else:
                if student_obj and student_class :
                    subject_obj = subjects.objects.get(subject_names=dept)
                    marks_file = students_marks(student_name=student_obj,marks=marks_given,sub_name=subject_obj)
                    marks_file.save()
                    return HttpResponse("<h1>given</h1>")
                
        except:
         return HttpResponse("<h1>please enter correct details!!")
    return render(request,'students_progress/marks_form.html')


def student_progress(request):
   if request.method=='POST':
        try:
            
            flag=False
            name_submitted = request.POST['name']
            sch = request.user
            studentss=students.objects.filter(school_name=sch).values()
            for i in studentss:
                if i['name']==name_submitted:
                    flag=True
                    break
            
            if flag==True:
                print("checer")
                names = students.objects.get(name=str(name_submitted))
                print(names)
                marks = students_marks.objects.filter(student_name=names)
                print(marks)
                print(marks)
                total_marks =0
                for mark in marks:
                    total_marks +=mark.marks
                print(total_marks)

                #print(s,emps)
                return render(request,'students_progress/marksheet.html',{'students':names,'marks':marks,'total_marks':total_marks})
            
            else:
                 return HttpResponse("<h1>No Student with that name in our School!!</h1>")

        except:
            return HttpResponse("<h1>No Data Found!!")
      
   return render(request,'students_progress/students_progress.html')

       
