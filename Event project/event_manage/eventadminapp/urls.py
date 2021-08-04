from django.urls import path
from . import views
urlpatterns = [
    path('profile',views.user_profile,name='profile'),
    path('logout',views.user_logout,name='logout'),
    path('passwordchange',views.password_change,name='passwordchange'),
    path('setpassword', views.set_password, name='setpassword'),
    path('signup',views.sign_up,name='signup'),
    path('login',views.user_login,name='login'),

    ]