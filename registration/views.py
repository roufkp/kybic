from django.shortcuts import render,redirect
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def test(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


class LandingPageView(generic.TemplateView):
    template_name = "home.html"

def about_page(request):
   return render(request,"about.html")
def contact_page(request):
   return render(request,"contact.html")

def service_page(request):
   return render(request,"services.html")
