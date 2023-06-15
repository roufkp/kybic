from django.shortcuts import render,redirect
from django.views import generic
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .forms import FeedbackForm



def test(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


class LandingPageView(generic.TemplateView):
    template_name = "home.html"

def about_page(request):
   return render(request,"about.html")

def contact_page(request):
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
      return render(request,"contact.html")
   else:
      return render(request, 'contact.html')  # Render the contact form template if it's a GET request


def service_page(request):
   return render(request,"services.html")
   

def blog_page(request):
   return render(request,"blog.html")


def admin1_page(request):
   return render(request,"admin1.html")

def testimonials_page(request):
   return render(request,"testimonials.html")

def blog1_page(request):
   return render(request,"blog1.html")



   
  


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
