from django.urls import path
from django.urls import path, include
from .views import test
from . import views

app_name = "registration"


urlpatterns = [
    path('test/',test,name="test"),
    path('accounts/',include('accounts.urls')),
    path('blog/<int:blog_id>/', views.blog_post_detail, name='blog_post_detail'),
     
]