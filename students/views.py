from django.shortcuts import render
from .models import Students,Subjects,Marks

def test(request):
    return render(request, 'test.html')

def home(request):
    return render(request, 'home.html')

def students(request):
    student=Students.objects.all()
    context={
        'student' : student,
    }
    return render(request, 'students.html', context)

def subjects(request):
    subject=Subjects.objects.all()
    context={
        'subject' : subject,
    }
    return render(request, 'subjects.html', context)

def marks(request):
    mark=Marks.objects.all()
    context={
        'mark' : mark,
    }
    return render(request, 'marks.html', context)
