from django.urls import path
from App_Blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
]
