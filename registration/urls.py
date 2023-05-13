from django.urls import path
from .views import test

app_name = "registration"


urlpatterns = [
    path('test/',test,name="test"),
]
