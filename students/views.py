from django.shortcuts import render
from .models import Students,Subjects,Marks
from django.contrib.auth.decorators import login_required

def test(request):
    return render(request, 'test.html')


@login_required
def home(request):
    """
        Return the name of all
    """
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


def ranks(request):
    """
        Show the ranks based on total marks (percentage) and the percentage obtained too...
    """
    pass

def student_result_details(request, student_pk):
    pass

def student_profile(request):
    """
    return the profile details of the student
    """
    pass

def subject_branch_wise(request):
    """
    Return the name of branches sorted branch wise
    """
    pass


