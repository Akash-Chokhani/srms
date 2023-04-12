from django.shortcuts import render
from .models import Students,Branch,Subjects,Branch_Subjects,Marks
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def test(request):
    return render(request, 'test.html')


@login_required
def home(request):
    """
        Return the name of all
    """
    return render(request, 'home.html')

def students(request):
    student=Students.objects.values()
    context={
        'student' : student,
    }
    return render(request, 'students.html', context)

def branch(request):
    branch=Branch.objects.values()
    context={
        'branch' : branch,
    }
    return render(request, 'branch.html', context)

def subjects(request):
    subject=Subjects.objects.values()
    context={
        'subject' : subject,
    }
    return render(request, 'subjects.html', context)

def branch_subjects(request,bcode):
    br=Branch.objects.filter(br_code=bcode).values().get()
    br_sub=Branch_Subjects.objects.filter(br_code_id=br['id']).values()
    subs=[]
    for x in br_sub:
        sub=Subjects.objects.filter(id=x['sub_code_id']).values().get()
        subs.append(sub)
    context={
        'branch' : br,
        'branch_sub' : subs,
    }
    return render(request, 'branch_subjects.html', context)

def marks(request):
    mark=Marks.objects.values()
    student_marks=[]
    for x in mark:
        stud=Students.objects.filter(id=x['rollno_id']).values().get()
        sub=Subjects.objects.filter(id=x['sub_code_id']).values().get()
        marks=dict(mark=x,student=stud,subject=sub)
        student_marks.append(marks)
    
    context={
        'student_marks' : student_marks,
    }
    return render(request, 'marks.html', context)

def results(request, roll):
    student=Students.objects.filter(rollno=roll).values().get()
    mark=Marks.objects.filter(rollno_id=student['id']).values()
    subject=Subjects.objects.filter(id=0).values()
    total=0
    percent=0
    for x in mark:
        subject|=Subjects.objects.filter(id=x['sub_code_id']).values()
        total+=x['marks']
        percent+=100
    percent=(total/percent)*100
    percent=round(percent,2)
    
    context={
        'student' : student,
        'subject_mark' : zip(subject,mark),
        'total' : total,
        'percent' : percent,
    }
    return render(request, 'results.html', context)

def add(request):
    student=Students.objects.values()
    context={
        'student' : student,
    }
    template = loader.get_template('add.html')
    return HttpResponse(template.render(context, request))

def addrecord(request):
  x = request.POST['rolle']
  y = request.POST['naam']
  member = Students(rollno=x, name=y)
  member.save()
  return HttpResponseRedirect(reverse('students'))

def ranks(request):
    pass
