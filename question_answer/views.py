from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def Exams_list(req):
    return render(req, 'question_answer/exams_list.html')


@login_required(login_url='/login/')
def Exams_Form(req):
    return render(req, 'question_answer/exams_form.html')