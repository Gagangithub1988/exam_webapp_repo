from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User,auth
from django.contrib.auth.models import auth
from .models import Account

from django.contrib import messages
# Create your views here.
def home_view(request):
    return render(request,'testApp/home.html')

@login_required
def java_exam_view(request):
    return render(request,'testApp/java.html')
@login_required
def python_exam_view(request):
    return render(request,'testApp/python.html')
@login_required
def sql_exam_view(request):
    return render(request,'testApp/sql.html')

def register_view(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        agreement=request.POST.get('agreement')
        if agreement not in ['term']:
            messages.info(request,'Please accept our agreement')
            return redirect('/register')
        else:
            if password1==password2:
                if Account.objects.filter(username=username).exists():
                    messages.info(request,'Username is already exist is database')
                elif Account.objects.filter(email=email).exists():
                    messages.info(request,'Email id already registered with other user')
                else:
                    user=Account.objects.create_user(first_name=first_name,username=username,email=email,password=password1)
                    user.save()
                    return redirect('/sign_view')

    return render(request,'testApp/signup.html')

def sign_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/sign_view')

    return render(request,'registration/login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('/home')

from .forms import AccountForm
def profile_update_view(request):
    user=request.user
    form=AccountForm(instance=user)
    if request.method=='POST':
        form=AccountForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    return render(request,'testApp/profile_update.html',{'form':form})
def profile_view(request):
    return render(request,'testApp/profile.html')
