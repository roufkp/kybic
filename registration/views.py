from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .forms import FeedbackForm,TestimonialForm,BlogForm
from .models import Testimonials,Blog 
from . import views
# from django.contrib.auth.models import user, auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404



def test(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


class LandingPageView(generic.TemplateView,LoginRequiredMixin):
   template_name = "home.html"





def about_page(request):
   testimonials=Testimonials.objects.all()
   print(testimonials)
   context={
      'testimonials':testimonials,
   }
   return render(request,"about.html",)

def contact_page(request):
   def sendmail(request):
      if request.method == 'POST':
         name = request.POST.get('name')
         phone = request.POST.get('phone')
         email = request.POST.get('email')
         message = request.POST.get('message')
         
         # Send email
         content = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n \nMessage:{message}"
         print("send mail")
         # Send the email
         email = EmailMessage(
            subject=f'Contact form submission from KYBIC website',
            body=content,
            from_email='developer.addox@gmail.com', # replace with your email address
            to=['roufkpkp@gmail.com'], # replace with the recipient email address
            reply_to=[email],
            headers={'From': email}
         )
         email.send()

         
         return render(request,"contact.html",{testimonials:'testimonials'})
      else:
         return render(request, 'contact.html')  # Render the contact form template if it's a GET request
   testimonials=Testimonials.objects.all()
   sendmail(request)
   context={
      'testimonials':testimonials,
   }
   return render(request,"contact.html",context)


def service_page(request):
   return render(request,"services.html")
   

def blog_page(request):
   blog =Blog.objects.all()
   context ={
      'blog':blog,
   }
   return render(request,"blog.html",context)



def admin1_page(request):
   return render(request,"admin1.html")


@login_required
def testimonials_page(request):
   testimonials = Testimonials.objects.all()
   context = {
      'testimonials':testimonials,
   }
   return render(request,"testimonials.html",context)


@login_required
def blog1_page(request):
   a =Blog.objects.all()
   context ={
      'b':a,
   }
   return render(request,"blog1.html",context)






def form_page(request):
   return render(request,"form.html")

def blogform_page(request):
   return render(request,"blogform.html")







   #view

   #testimonial section

   #create 
def create_testimonial(request):    
   form = TestimonialForm()
   if request.method == 'POST':
      form = TestimonialForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()  # Save the form data to the model
         return redirect('testimonials')  # Redirect to a success page or another view

      else:
         print('hi',form.errors)

   else:
      form = TestimonialForm()

   return render(request, 'form.html', {'form': form})



#EDIT

def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonials, pk=pk)
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonials')  # Redirect to testimonials listing page or any other desired page
    else:
        form = TestimonialForm(instance=testimonial)
    
    return render(request, 'edit_testimonial.html', {'form': form, 'testimonial': testimonial})




#DELETE
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonials, pk=pk)
    
    if request.method == 'GET':
        testimonial.delete()
        return redirect('testimonials')  # Redirect to testimonials listing page or any other desired page

#delete end



#blog view

def create_Blog(request):
   form = BlogForm()
   if request .method == 'POST':
      form = BlogForm(request.POST,request.FILES )
      if form.is_valid():
         form.save()
         return redirect('blog1')
      
   return render(request,'blogform.html',{'form':form, })
#blog view end



#blog edit


def edit_blog(request, pk):
   blog = get_object_or_404(Blog, pk=pk)

   if request.method =='POST':
      form = BlogForm(request.POST, request.FILES, instance=blog)
      if form.is_valid():
         form.save()
         return redirect('blog1')
   else:
      form =BlogForm(instance=blog)
   return render(request,'edit_blog.html',{ 'form':form, 'blog1':blog})


def delete_blog(request, pk):
   blog = get_object_or_404(Blog, pk=pk)
   if request.method =='GET':
      blog.delete()
      return redirect('blog1')
   
   
def blog_post_detail(request, pk):
   blog= get_object_or_404(Blog, pk=pk)
   return render(request, 'blog_post_detail.html', {'blog': blog})







   # def login(request):
   #     return render (request,'login.html') 

      
   # def login(request):
   #    if request.method =='POST':
   #       Username = request.POST['Username']
   #       password = request.POST['password']

   #       user = user .object.create_user(request, username=username, password=password)
   #       user .save()
   #       print('user created')
   #       return redirect('/')
       
   #    else:
   #       return render(request,"login.html")






  


# def send_message(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         # Send email
#         content = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n \nMessage:{message}"
#         print("send mail")
#         # Send the email
#         email = EmailMessage(
#             subject=f'Contact form submission from KYBIC website',
#             body=content,
#             from_email='developer.addox@gmail.com', # replace with your email address
#             to=['roufkpkp@gmail.com'], # replace with the recipient email address
#             reply_to=[email],
#             headers={'From': email}
#         )
#         email.send()
        
#         return render(request, 'contact.html')  # Render a success page after sending the email
#     else:
#         return render(request, 'contact.html')  # Render the contact form template if it's a GET request
