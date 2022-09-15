from django.shortcuts import render,redirect
from users.forms import UserRegistrationForm
from django.contrib.auth.decorators import *
from .forms import *
from .models import *
from django.contrib import messages
from users.models import *
# from Coordinator.models import
from Coordinator.models import course
@login_required
def home(request):
     
    context= {
        'academies': Academy.objects.all(),
        'courses': course.objects.all(),
        'd':ICTDescription.objects.all(),

    }
    return render(request, 'ACM/home.html', context)
@login_required
def addAcademy(request):
    if request.method == 'POST':
        form = Add_Academy(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Academy added successfully!!')
            return redirect('ahome')
        else:
            messages.error(request, 'form not valied please try again..!')
    else:
        form = Add_Academy()
    context={
        'form':form
    }
    return render(request,'ACM/add_academy.html', context)
@login_required
def addCoordinator(request):
     
    context={
        'p_form': user.objects.filter(Roll='user'),

        
    }
    
    return render(request, 'ACM/addcoordinator.html', context)

@login_required
def validate(request):
    a = user.objects.filter(FullName = request.POST['FullName']).first()
    print(a.Roll)
  
    form = AddCoordinator(instance=a)
    if request.method=="POST":
        print('in if block')
        form = valStud(request.POST, instance=a)
        if form.is_valid():
           
            form.save()
            print('saved')
            messages.success(request, 'Coordinator Added successfuly..!')
            return redirect('ahome')
        else:
            messages.error(request,'oops.... unable to add coordinator.')
        
    else:
        print('in else block')
#        form = course.objects.all()
#    context={
#        'courses': form,
#    }
    return redirect('add-coordinator')



@login_required
def describe(request):
    if request.method=='POST':
        de = ICT(request.POST)
        if de.is_valid():
            r = ICTDescription.objects.filter(name = 'ICT department')
            r.delete()
            de.save()
            messages.success(request,'uodate successfull.')
        
    else:
        
        de = ICT()
    a= ICTDescription.objects.filter(name= 'ICT department')
    context={
        'fields': de,
        'current':a
    }
    return render(request, 'ACM/ICTdescription.html', context)
@login_required
def mess(request):
    if request.method == 'POST':
        form = UserMessage.objects.filter(email= request.POST['email'])
        form.delete()
    else:
        form= UserMessage.objects.all()
    context= {
        'form': UserMessage.objects.all()
    }
    return render(request,'ACM/messages.html',context)