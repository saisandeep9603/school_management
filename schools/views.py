
from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import render
from notices.models import *


from .models import *
User = get_user_model()

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        access_token = request.POST.get("access_value")
        print(access_token)
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email=email,password=pass1,access=access_token)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        school = request.user
        if user is not None:
            login(request,user)
            return render(request,'home.html',{'school':school})
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def totalschooldetails(request):
    school_name="sai"
    print(school_name)
    return render(request,'principal_index.html',{'school_name':school_name})

def staff_details(request):
    emps = staff.objects.filter(school_name=request.user)
    context= {
        'emps': emps
    }
    if len(context)>0:

        return render(request,'staff_details.html',context)
    else:
        return HttpResponse("<h1>no staff</h1>")


def add_staff(request):
    if request.method=='POST':
        firstname=request.POST['name']
        phone=int(request.POST['phone'])
        dept=(request.POST['department'])
        school = request.user 
        
        print(school)
        new_employe=staff(name=firstname,phonenumber=phone,department=dept,school_name=school)
        new_employe.save()
        return HttpResponse("<center><h1>staff added successfully</h1></center>")

    else:
        return render(request,'staff_create.html')

def remove_staff(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove=staff.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("<center><h1>Employee has removed successfully!</h1></center>")
        except:
            return HttpResponse("<center><h1>Please select properly!</h1></center>")
    emps=staff.objects.filter(school_name=request.user)
    context={
        'emps':emps
    }
    return render(request,'staff_removal.html',context)
    

def students_details(request):
    emps = students.objects.filter(school_name=request.user)
    context= {
        'emps': emps
    }
    if len(context)>0:

        return render(request,'student_details.html',context)
    else:
        return HttpResponse("<h1>no students</h1>")

def student_details_by_class(request,class_names=''):
    if len(class_names)>0:
        print(class_names)
        class_obj = classes.objects.get(class_names = class_names)
        emps = students.objects.filter(class_name=class_obj)
        context={
            'emps':emps
                    }
        print(context)
        return render(request,'student_details.html',context)
        # except:
        #     return HttpResponse("<center><h1>Please select properly!</h1></center>")
        

    emps = classes.objects.all()
    context={
        'emps':emps
    }
    return render (request,'class_name.html',context)

def bonafide(request):
    if request.method=='POST':
        name = request.POST['name']
        classses = request.POST['class_name']
        print(name,classses)

        return HttpResponse("<h1>snfskdnf</h1>")

    emps = classes.objects.all()
    context={
        'emps':emps
    }
    return render (request,'bonafide_fill.html',context)

def  my_page(request):
    if request.method=='POST':
        name_of_student = request.POST['name']
        name_of_class = request.POST['class_name']
        class_obj = classes.objects.get(class_names = name_of_class)
        checker =[name_of_student,name_of_class]
        emps = students.objects.filter(class_name=class_obj)
        
        students_list =[]
        for emp in emps:
            students_list.append([emp.name,name_of_class])
        if checker in students_list:
            checker.append(request.user )
            context={
          'emps':checker
        
    }
            print(checker)
            return render(request,'bonafide.html',context)
        else:
            return HttpResponse("<h1>student not  found</h1>")




    return render(request,'bonafide_fill.html')

def student_add(request):
    if request.method=='POST':
     
        student_name = request.POST['name']
        student_age = request.POST['age']
        student_father = request.POST['fathername']
        phone=int(request.POST['phonenumber'])
        
        name_of_class = (request.POST['classname'])
        class_obj = classes.objects.get(class_names = name_of_class)
        school = request.user 
        
        print(school)
        new_student = students(name=student_name,age=student_age,fathername=student_father,contact_number=phone,
                             class_name=class_obj,school_name=school)
        new_student.save()
        return HttpResponse("<center><h1  style='margin-top:5px;'>student added successfully</h1></center>")
    return render(request,'students_add.html')

def principal_access(request):
    if request.method=="POST":
        school_name = str(request.POST['school_name'])
        access_token = str(request.POST['access_token'])
        school = str(request.user )
        token = str(request.user.access)
        if school_name==school and token==access_token:
            school_name=school_name.upper()
            return render(request,'principal.html',{'school_name':school_name})
        return HttpResponse("<h1>Invalid access!!</h1>")
    return render(request,'principal_access.html')

faculty=''
def staff_login(request):
    if request.method=='POST':
        global faculty
        faculty = request.POST['name']
        school = request.user
        staffs = staff.objects.filter(school_name=school)
        for i in staffs:
            if i.name==faculty:
                k=faculty.upper()
                return render(request,'staff_index.html',{'k':k})
        
    
        return HttpResponse("<h1>No Staff with that name in our School!!</h1>")
    school = request.user
    notices = reversed(list(notice_uploading.objects.filter(school_name=school)))
    print(notices)
    
   
    context={
        'notices':notices
    }

    return render(request,'staff_login.html',context)

def staff_index(request):
    
    return render(request,'staff_index.html')

def stafff_files(request):
    if request.method=='POST':
        sname = request.POST['name']
        description_of_file = request.POST['Description']
        doc = request.FILES #returns a dict-like object
        doc_name = doc['myfile']
        school = request.user
        staff_obj = staff.objects.get(name=faculty)
        new_file = staff_files(description=description_of_file,file=doc_name,staff_name=staff_obj)
        new_file.save()
        #print(staff_obj)
        #print(sname)
        #print(description_of_file)
        return HttpResponse("<h1>successfully uploaded</h1>")
    return render(request,'files_upload.html')

def view_files_of_staff(request):

    school = request.user
    #staffs = staff.objects.filter(school_name=school)
    faculty_obj = staff.objects.get(name=faculty)
    emps = staff_files.objects.filter(staff_name=faculty_obj).all()
    context ={
        'emps':emps,
        'faculty':faculty
    }
    print(context)
    #return HttpResponse("<h1>helo</h1>")
    return render(request,'staff_files.html',context)




    




