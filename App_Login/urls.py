from django.urls import path
from App_Login import views




urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.user_change, name='change_profile'),
    path('password/', views.pass_change, name='password'),
    path('add_picture/', views.add_profile_pic, name='add_picture'),
    path('change_pro_pic/', views.change_pro_pic, name='change_pro_pic'),
]

