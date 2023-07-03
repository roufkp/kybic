from django.urls import path
from django.urls import path, include
from .views import test

app_name = "registration"


urlpatterns = [
    path('test/',test,name="test"),
     path('accounts/',include('accounts.urls')),
]