from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='homepage'),
    path('login',views.login,name='login'),
     path('register',views.register,name='register'),
     # path('final',views.final,name='finalpage'),
    path('intermediate',views.intermediate,name='intermediate'),
    path('drop',views.drop,name='drop'),
    path('logout',views.logout,name='logout'),

]