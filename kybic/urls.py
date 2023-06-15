from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from registration.views import LandingPageView,contact_page,service_page,about_page,blog_page,admin1_page,testimonials_page,blog1_page
# send_message

urlpatterns = [
    path('',LandingPageView.as_view(),name="home"),
    path('contactus/',contact_page,name="contact"),
    path('services/',service_page,name="services"),
    path('about/',about_page,name="about"),
    path('blog/',blog_page,name="blog"),
     path('admin1/',admin1_page,name="admin1"),
     path('testimonials/',testimonials_page, name='testimonials'),
     path('blog1/',blog1_page, name='blog1'),
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls',namespace="registration")),
    # path('send-message/', send_message, name='send_message'),
]


