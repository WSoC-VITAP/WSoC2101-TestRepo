from django.contrib.auth import authenticate,login, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "authentication/index.html")


def profile(request):
      return redirect(profile)


def signup(request):
     
   

   if request.method =='POST':
         username = request.POST['username']
        #  fname = request.POST['fname']
        #  lname = request.POST['lname']
         email = request.POST['email']
         pass1 = request.POST['pass1']
         pass2 = request.POST['pass2']
         
         if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
         if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
         if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
         if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
         if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
         
         myuser=User.objects.create_user(username,email,pass1)
         
        #  myuser.first_name=fname;
        #  myuser.last_name=lname;
         messages.success(request,"Your account has been successfully created!")
         myuser.save();
        

         #! Welcome email

         subject = "Welcome to Club Vit!!"
         message = "Hello " + myuser.username + "!! \n" + "Welcome to Club Vit!! \nThank you for visiting and joining\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAayush Anand"        
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser.email]
         send_mail(subject, message, from_email, to_list, fail_silently=True)
         
         return redirect('signin')
        

   return render(request,"authentication/signup.html")
    

    #    # username = request.POST.get('username')
    #      username = request.POST['username']
    #      fname = request.POST['fname']
    #      lname = request.POST['lname']
    #      email = request.POST['email']
    #      pass1 = request.POST.get('pass1')
    #      pass2 = request.POST.get('pass2')
    #     #pass2 = request.POST['pass2']
   
    #      myuser = User.objects.create_user(username,email,pass1)
    #      myuser.first_name=fname;
    #      myuser.last_name=lname;

    #      myuser.save()
    #      messages.success(request,"Your account has been successfully created")

    #      return redirect('signin')

   

def signin(request):

    if request.method=='POST':
          username = request.POST['username']
          pass1 = request.POST['pass1']

          user = authenticate(username=username,password=pass1)

          if user is not None:
             login(request,user)
             user_name = user.username
             return render(request,"authentication/profile.html",{'username':user_name})

          else:
            messages.error(request,"Bad Credentials") 
            return redirect('signin')  

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
   #  messages.success(request,"logout:")
    return redirect(home)



