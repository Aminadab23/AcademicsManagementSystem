from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . forms import *
from users.models import user

from django.contrib import messages,auth
from django.contrib.auth.decorators import *
from users.models import *
from AcademicManager.models import ICTDescription
# Create your views here.
@login_required
def home(request):
     
    context= {
        'academies': Academy.objects.all(),
        'courses': course.objects.all(),
        'd':ICTDescription.objects.all(),

    }
    return render(request, 'Coordinator/home.html', context)
@login_required
def addcourse(request):
    if request.method =='POST':
        form = addCourse(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'course added successfully!!')
            redirect('home')
    else:
        form = addCourse()
    context={
        'form': form
    }
    return render(request, 'Coordinator/add_course.html', context)
@login_required
def acdet(request):
    if request.method == 'POST':
        academy = Academy.objects.filter(Ac_name = request.POST['academy']).first()
        form = course.objects.filter(academy = academy).all()
    else:
        form = course.objects.all()
    context={
        'courses': form,
    }
    return render(request, 'Coordinator/course_detail.html', context)
@login_required
def addStudent(request):
      
    context={
        'recite': UploadRecite.objects.all(),

        
    }
    
    return render(request, 'Coordinator/validateRecite.html', context)

def students(request):
      
    context={
        'recite': user.objects.filter(Roll= "student")
        
    }
    
    return render(request, 'Coordinator/validateRecite.html', context)


def validate(request):
    
    a = user.objects.filter(FullName = request.POST['name']).first()
    print(a.Roll)
    print(a.FullName)
    # ap = Profile.objects.filter(user = a).first() 
    # print(ap)
    form = addStud(instance=a)
    if request.method=="POST":
        print('in if block')
        form = valStud(request.POST, instance=a)
        if form.is_valid():
            r = UploadRecite.objects.filter(name = request.POST['name'])
            r.delete()
            form.save()
            print('saved')
            messages.success(request, 'validation successfull')
            return redirect('addStudent')
        
    else:
        print('in else block')
        form = course.objects.all()
    context={
        'courses': form,
    }
    return redirect('addStudent')

   




def logout(request):
    auth.logout(request)
    return redirect('index')