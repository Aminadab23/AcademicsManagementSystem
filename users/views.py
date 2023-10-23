from difflib import context_diff
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .forms import *
from django.contrib.auth.decorators import *
from AcademicManager.models import Academy, ICTDescription
from .models import user
from Coordinator.models import course
# Create your views here.
def index(request):
    if request.method=='POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration successfull!!')
        else:
            messages.error(request,'oops..... your form is invalied. not registered! pls try again')
    else:
        form= UserRegistrationForm()
    a= ICTDescription.objects.all()
   
    
    context={
        'form': form,
        'academy': Academy.objects.all(),
        'courses':course.objects.all(),
        'd': ICTDescription.objects.all(),
    }
    return render(request,'users/inde.html',context)
def login(request):
    if request.method=='POST':
        email = request.POST['email']
        p = request.POST['password1']
        user= auth.authenticate(email= email, password = p)
        if user is not None:
            auth.login(request,user)
            if user.Roll == 'Academic Manager':
                return redirect('ahome')
            elif user.Roll == 'Coordinator':
                return redirect('chome')
            elif user.Roll == 'user':
                return redirect('home')
        else:
            messages.error(request, 'wrong username or password')
    return redirect('index')
@login_required
def home(request):
    a= ICTDescription.objects.all()
    
    context={
        
        'academy': Academy.objects.all(),
        'courses': course.objects.all(),
        'd': ICTDescription.objects.all(),
       
    }

    return render(request, 'users/home.html', context)
@login_required
def reciteUpload(request):
    print('jkhjhadf')
    if request.method =='POST':
        a= request.POST['academy']
        print(a)
        form = reciteUpForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['recite'].name)
            form.save()
            print('saved....')
            messages.success(request, 'upload successfull!!')
            return redirect('home')
        else:
            messages.error(request,f'upload failed')
            return redirect('home')
    
 
@login_required
def profile_update(request):
    if request.method=='POST':
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, f'Your Profile has been Updated')
            return redirect('home')
            
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user)

    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_update.html',context)
    
def logout(request):
    auth.logout(request)
    return redirect('index')

def acdetail(request,name):
    a= Academy.objects.filter(Ac_name=name).first()
    c= course.objects.filter(academy = a)
    context= {
        'courses': c

    }
    return render(request, 'users/academy_detail.html', context)
def UserMess(request):
    print(request.POST['name'])
    print(request.POST['email'])
    print(request.POST['message'])
    if request.method == 'POST':
        form = MESS(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Message sent successfully. Thank you!')
            return redirect('index')
    print('method not post')
    return redirect('index') 
