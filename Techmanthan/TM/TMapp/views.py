from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from datetime import datetime


# Create your views here.
def home(request):
    
    return render(request,'start.html')


def quiz(request):
    if not request.user.is_anonymous:
        if request.method=="POST":
            qans=[]
            ans=[]
            count=Questions.objects.all().values().count()
            current_time = datetime.now().strftime('%H:%M:%S')
            for i in range(1,count+1):
                a=request.POST.get(f'q{i}')
                qans.append(a)
            for i in range(0,count):
                b=Questions.objects.all().values()[i]['ans']
                ans.append(b)
            score=0
            for i in range(0,len(ans)):
                if qans[i]==ans[i]:
                    score=score+1
            score_table=Score(tname=request.user.username,m1=request.user.first_name,m2=request.user.last_name,score=score,time=current_time)
            score_table.save()
            
            return render(request,"quiz.html",{'score':score,'s':0})
        request.session['time']=datetime.now().strftime('%H:%M:%S')
        qst=Questions.objects.values()
        return render(request,"quiz.html",{'questions':qst,'s':1})
    return redirect("login")


def signin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pas=request.POST.get('pas')
        user=authenticate(username=uname,password=pas)
        if user is not None:
            login(request,user)
            return redirect("quiz")
    return render(request,"login.html")


def signout(request):
    logout(request)
    return redirect("/")


def score(request):
    if request.user.is_superuser:
        obj=Score.objects.all().order_by('-score').values()
        return render(request,"score.html",{'teams':obj})
    return redirect("login")