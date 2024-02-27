from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def dashboard(request):
    user = request.user
    try:
     leave_list = leave.objects.filter(user=request.user)
    except leave.DoesNotExist:
     leave_list = None
    leave_list = leave.objects.filter(user=user)
    return render(request,'dashboard.html',locals())

def apply(request):
    user = request.user
    if request.method == 'POST':
        user = request.user
        start = request.POST.get('start')
        end = request.POST.get('end')
        type = request.POST.get('type')
        reason = request.POST.get('reason')
        l_save = leave(user=user,start=start,end=end,type=type,reason=reason)
        l_save.save()
        messages.info(request,'Leave applied successfully')
        return redirect('dashboard')
    else:
     return render(request,'apply.html')

def total(request):
    leave_all = leave.objects.filter(user=request.user)
    total = len(leave_all)
    return render(request,'total.html',locals())

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('apply')
        
    else:
     return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.info(request,'Account created Successfuly')
                return redirect('login')
        else:
            messages.error(request,'Password Not The Same')
            return redirect('register')
    else:
     return render(request,'register.html')
    

def profile(request):
    user = request.user
    prof_info = profileinfo.objects.filter(user=user)
    try:
     profile_info = profileinfo.objects.filter(user=request.user)
    except profileinfo.DoesNotExist:
       profile_info = None
    return render(request,'profile.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/')


def profile_update(request):
   if request.method == 'POST':
      prof_save = profileinfo.objects.get_or_create(
         user = request.user,
         firstname=request.POST.get('firstname'),
         secondname=request.POST.get('secondname'),
         age=request.POST.get('age'),
         address=request.POST.get('address'),
         mobile=request.POST.get('mobile'),
      )
      messages.info(request,'Profile updated successfully')
      return redirect('profile')
   else:
    return render(request,'profile_update.html')
   


def delete(request,id):
   dele = leave.objects.get(id=id)
   dele.delete()
   messages.info(request,'Leave deleted successfully')
   return redirect('dashboard')



def profile_edit(request,id):
   x = profileinfo.objects.get(id=id)
   if request.method == 'POST':
        user = request.user
        firstname=request.POST.get('firstname')
        secondname=request.POST.get('secondname')
        age=request.POST.get('age')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        edit = profileinfo.objects.get(id=id)
        edit.firstname = firstname
        edit.secondname = secondname
        edit.age = age
        edit.address = address
        edit.mobile = mobile
        edit.save()
        messages.info(request,'profile edit is successful')
        return redirect('profile')
   else:
    return render(request,'profile_edit.html',locals())
   


def preview(request,id):
   x = leave.objects.get(id=id)
   return render(request,'preview.html',locals())