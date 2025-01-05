from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("vivek",views.vivek,name="vivek"),
    path("<str:name>",views.greet,name="greet")
]