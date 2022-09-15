from django.shortcuts import render
from AcademicManager.models import Academy
# Create your views here.
def courseMaterial(request):
    context= {
        'academy': Academy.objects.all()
    }
    # return render(request, 'Student/courseMaterial.html',context)
    return render(request, 'Student/courseMaterial.html', context)
