from django.conf.urls import url
from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path ('', views.index, name='index'),
    path ('form/', views.form, name='form'),
]
