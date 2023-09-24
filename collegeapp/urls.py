from django.urls import path
from .import views
app_name ='collegeapp'


urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('formss/',views.formss,name="formss"),
   
    path('register/',views.register,name="register"),
    
    path('register_student/',views.register_student,name="register_student"),
    
    path('login/',views.login,name="login"),
    path('login_student/',views.login_student,name="login_student"),
    
    # path('form/',views.regforms,name="regforms"),
    # path('form_student/',views.form_student,name="form_student"),
   
    
    # path('register/',views.register,name="register"),
    
    
    
   
     
   
    
]