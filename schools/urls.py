from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SignupPage,name='signup'),
    path('login/',LoginPage,name='login'),
    path('home/',HomePage,name='home'),
    path('logout/',LogoutPage,name='logout'),
    path('schooldetails/',totalschooldetails,name="totalschooldetails"),
    path('staffdetails/',staff_details,name='staff_details'),
    path('add_staff/',add_staff,name='add_staff'),
    path('remove_staff/',remove_staff,name='remove_staff'),
    path('remove_staff/<int:emp_id>/',remove_staff,name='remove_staff'),
    path('student_details/',students_details,name='students_details'),
    path('student_details_by_class/',student_details_by_class,name='student_details_by_class'),
    path('student_details_by_class/<str:class_names>/',student_details_by_class,name='student_details_by_class'),
    path('bonafide_fill/',bonafide,name='bonafide'),
    path('my_page/',my_page,name='my_page'),
    path('student_add/',student_add,name='student_add'),
    path('principal_access/',principal_access,name='principal_access'),
    path('staff_index/',staff_index,name='staff_index'),
    path('stafff_files/',stafff_files,name='staff_files'),
    path('staff_login/',staff_login,name='staff_login'),
    path('view_files_of_staff/',view_files_of_staff,name='view_files_of_staff'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)