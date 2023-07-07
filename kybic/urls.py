from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.urls import path




from registration.views import (LandingPageView,contact_page,service_page,
about_page,blog_page,admin1_page,testimonials_page,blog1_page,blogform_page,form_page
,create_testimonial,edit_testimonial,delete_testimonial,create_Blog,edit_blog,delete_blog,)
# send_message


urlpatterns = [
    path('',LandingPageView.as_view(),name="home"),
    path('contactus/',contact_page,name="contact"),
    path('services/',service_page,name="services"),
    path('about/',about_page,name="about"),
    path('blog/',blog_page,name="blog"),
     path('admin1/',admin1_page,name="admin1"),
     path('testimonials/',testimonials_page, name='testimonials'),
     path('form/',form_page, name='form'),
     path('blogform/',blogform_page, name='blogform'),
     path('addtestimonial/',create_testimonial, name='addtestimonial'),
     path('blog1/',blog1_page, name='blog1'),
     path('addblog/',create_Blog, name='addblog'),
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls',namespace="registration")),
     path('edit_testimonial/<int:pk>/', edit_testimonial, name='edit_testimonial'),
     path('delete_testimonial/<int:pk>/', delete_testimonial, name='delete_testimonial'),
     path('edit_blog/<int:pk>/', edit_blog, name='edit_blog'),
      path('delete_blog/<int:pk>/', delete_blog, name='delete_blog'),
       path('accounts/', include('accounts.urls',namespace="accounts")),
        
       
       
      
      



      


    # path('send-message/', send_message, name='send_message'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


