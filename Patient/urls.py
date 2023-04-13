from django.urls import path
from .import views


urlpatterns=[

    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='reg'),
    path('predict',views.predict,name='predict'),
    path('contact',views.contact,name='contact'),



]