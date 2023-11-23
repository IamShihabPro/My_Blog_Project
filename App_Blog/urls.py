from django.urls import path
from App_Blog import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    # path('details/<slug:slug>/', views.blog_details, name='blog_details'), use path given below code 
    path('details/<path:slug>/', views.blog_details, name='blog_details'),
]
