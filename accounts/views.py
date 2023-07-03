from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib .auth.models import User,auth
# Create your views here.


def login(request):
   if request.method =='POST':
         username =request.POST[username]
         password =request.POST[password]

         user = auth.authenticate(username=username,password=password)

         if user is not None:
             auth.login(request,user)
             return redirect("/")
         else:
             messages.info(request,'invalid credentials')
             return redirect('login')
         
   else:
        return render(request,'login.html')









def register(request):
    
    if request.method =='POST':
        first_name =request.POST[first_name]
        last_name =request.POST[last_name]
        username =request.POST[username]
        password1 =request.POST[password1]
        password2 =request.POST[password2]
        email =request.POST[email]
        
        if password1==password2:
           if user.objects.fiter(username=username).exists():
               messages.info(request,'username Taken')
               return redirect('register')
           elif user.objects.filter(email=email):
                 messages.info(request,'Email Taken')
                 return redirect('register')
           else:    
                user = user.objects.create_user(username=username, password=password1,first_name=first_name,last_name=last_name,email=email )
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info('password no matching..')
            return redirect('register')
               
        return redirect('/')
    
    else:

        return render(request,'register.html')
