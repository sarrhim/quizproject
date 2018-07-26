from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Exam,Question
from django.views import generic
from django.views.generic import View
from django.db import connection
from django.shortcuts import render,redirect
from .models import Question,Exam,One_answer,Free_text,MultiChoice
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader


def index(request):
    all_exams=Exam.objects.all().filter(is_active="True")
    template=loader.get_template('exams/index.html')
    context= {
          'all_exams':all_exams,
             }
    return HttpResponse(template.render(context,request))


def create_view(request):
   return render(request, 'exams/createExam.html')


def detail(request, question_id):
  
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})
'''
def questions(request,Exam_id):
    row=Question.objects.all().filter(examen_id=Examen_id)
    l=[]
    k=[]
    for q in row:
        k=[]
        k.append(q.question_text)
        row1=Answer.objects.all().filter(question_id=q.id)
        for m in row1:
            k.append(m)
        l.append(k)

    dict={}
    template=loader.get_template('question.html')
    dict[1]=l
    context= dict
    return HttpResponse(template.render(context,request))
'''
def index1(request,Examen_id):
    latest_question_list = Question.objects.all().filter(exam_id=Exam_id)
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'quiz/index.html', context)
