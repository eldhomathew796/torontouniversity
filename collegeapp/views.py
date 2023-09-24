from django.contrib import auth, messages
from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


from collegeapp.models import*

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'Register.html')

def home(request):
    return render(request,'Home.html')
def formss(request):
    return render(request,'formss.html')

# def regforms(request):
#     return render(request,'form.html')



# def register_student(request):
#     if request.method == 'POST':
#         print("Register")
      
            
#         username=request.POST["username"]
        
#         password=request.POST["password"]
#         cpassword=request.POST["cpassword"]
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username taken")
#                 return redirect("register_student")
           
#             else:
                
#                 user=User.objects.create_user(username=username,password=password)
#                 user.save()
#                 return render(request,'login.html')
#                 print("created")
#         else:
#             messages.info(request,'password not matching')
#             return redirect("register_student")
#         return redirect("login" )  
#     else:    
#         return render(request,'Register.html')
def register_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['cpassword']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken ')
                # return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'email taken ')
                return redirect('register_student')
            else:
                user = User.objects.create_user(username=username, 
                                                password=password, )
                user.save();
            return redirect('login_student')

        else:
            messages.info(request, 'password not matching')
            return redirect('register_student')
        return redirect('/')
    return render(request,'Register.html')    


def login_student(request):
    if request.method=="POST":    
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"Home.html")
        
        else:
            messages.info(request,"User name or password incorrect")
            return redirect('login_student')
            
        
    return render(request,'login.html')

def form_student(request):
    cose= course.objects.all()
    dep=department.objects.all()
    if request.method=="POST": 
        name=request.POST["fullname"]
        Dob=request.POST["date"]
        age=request.POST["age"]
        
        gender=request.POST["gender"]
        phnumber=request.POST["number"]
        email=request.POST["email"]
        deptm=request.POST['dept']
        cour=request.POST['coses']
        address=request.POST["address"]
        purpose=request.POST["purpose"]
        
        dep=department.objects.all()  
        print(dep)
        cose=department.objects.get(id=cour)  
        details=studentdetails (department=dep,course=cose,name=name,Dob=Dob,age=age,gender=gender,phonenumber=phnumber,email=email,address=address,purpose=purpose) 
        details.save()
        
        return redirect('form_student')
    return render(request,'form.html',{'dep':dep,'cose':cose})
        
    
     

