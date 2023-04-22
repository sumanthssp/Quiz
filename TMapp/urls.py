from django.contrib import admin
from django.urls import path
from TMapp import views

urlpatterns = [
    path('', views.home,name="home"),
    path('quiz',views.quiz,name="quiz"),
    path('login',views.signin,name="login"),
    path('logout',views.signout,name="logout"),
    path('score',views.score,name="score"),
]