from random import *

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question, Exam, One_answer, Free_text, MultiChoice, Reponse


def index(request):
    if request.user.is_authenticated:
        all_exams = Exam.objects.all().filter(is_active="True")
        template = loader.get_template('exams/index.html')
        context = {
            'all_exams': all_exams,
        }
        return HttpResponse(template.render(context, request))
    else:
        return render(request, 'registration/home.html')


def create_view(request):
    return render(request, 'exams/createExam.html')


def detail(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exams/details.html', {'exam1': exam,
                                                  'exam1_id': exam_id, })


def createExam(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST['examName']:
            examName = request.POST['examName']
            ExamDesc = request.POST['ExamDesc']
            category = request.POST['category']
            logo = request.FILES['logo']

            exam = Exam()
            exam.name = examName
            exam.description = ExamDesc
            exam.category = category
            exam.logo = logo
            exam.save()
            request.session['id'] = exam.id
            print(request.session['id'])

            context = {
                'exam_id': exam.id,
            }
            return render(request, 'exams/createQuest.html', context)


def editExam(request, exam_id):
    if request.user.is_authenticated:
        exam = get_object_or_404(Exam, pk=exam_id)
        if request.method == 'POST':
            exam.name = request.POST['examName']
            exam.description = request.POST['examDesc']
            exam.category = request.POST['category']
            exam.logo = request.FILES['logo']
            exam.save()
            return redirect('/quiz/')
        else:
            template = loader.get_template('exams/editExam.html')
            context = {
                'exam': exam,

            }
            return HttpResponse(template.render(context, request))


def deleteExam(request, exam_id):
    if request.user.is_authenticated:
        Exam.objects.filter(pk=exam_id).delete()
        return redirect('/quiz/')


def addQuest(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST['Description']:
            question = Question()
            question.exam = exam
            question.question_text = request.POST['Description']
            question.footer_text = request.POST['Footer']
            question.header_text = request.POST['Header']
            question.success_message = request.POST['Success']
            question.fail_message = request.POST['Fail']
            question.point = request.POST['points']
            type_quest = request.POST['type']
            question.save()
            if type_quest == 'one':
                one1 = One_answer()
                one1.answer_description = request.POST['answer_description1']
                one1.answer_variant = request.POST['answer_variant1']
                one1.answer_point = request.POST['answer_points1']
                one1.question = question
                one1.save()
                one2 = One_answer()
                one2.answer_description = request.POST['answer_description2']
                one2.answer_variant = request.POST['answer_variant2']
                one2.answer_point = request.POST['answer_points2']
                one2.question = question
                one2.save()
                one3 = One_answer()
                one3.answer_description = request.POST['answer_description3']
                one3.answer_variant = request.POST['answer_variant3']
                one3.answer_point = request.POST['answer_points3']
                one3.question = question
                one3.save()
            if type_quest == 'multi':
                multi1 = MultiChoice()
                multi1.question = question
                multi1.multi_description = request.POST['answer_descriptionm1']
                multi1.multi_variant = request.POST['answer_variantm1']
                multi1.choice_point = request.POST['pointsm1']
                multi1.save()
                multi2 = MultiChoice()
                multi2.question = question
                multi2.multi_description = request.POST['answer_descriptionm2']
                multi2.multi_variant = request.POST['answer_variantm2']
                multi2.choice_point = request.POST['pointsm2']
                multi2.save()
                multi3 = MultiChoice()
                multi3.question = question
                multi3.multi_description = request.POST['answer_descriptionm3']
                multi3.multi_variant = request.POST['answer_variantm3']
                multi3.choice_point = request.POST['pointsm3']
                multi3.save()
            if type_quest == 'free':
                free = Free_text()
                free.question = question
                free.answer_text = request.POST['text']
                free.save()
                return redirect('/quiz/')
        else:
            template = loader.get_template('exams/addQuestion.html')
            context = {
                'exam': exam

            }

            return HttpResponse(template.render(context, request))


def modifOne(request, question_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)
        if request.method == 'POST':

            question.question_text = request.POST['Description']
            question.footer_text = request.POST['Footer']
            question.header_text = request.POST['Header']
            question.success_message = request.POST['Success']
            question.fail_message = request.POST['Fail']
            question.point = request.POST['points']
            question.save()
            i1 = request.POST['id1']
            i2 = request.POST['id2']
            i3 = request.POST['id3']
            onee1 = get_object_or_404(One_answer, pk=i1)
            onee1.answer_description = request.POST['answer_description1']
            onee1.answer_variant = request.POST['answer_variant1']
            onee1.answer_point = request.POST['answer_point1']
            onee1.question = question
            onee1.save()
            onee2 = get_object_or_404(One_answer, pk=i2)
            onee2.answer_description = request.POST['answer_description2']
            onee2.answer_variant = request.POST['answer_variant2']
            onee2.answer_point = request.POST['answer_point2']
            onee2.save()
            onee3 = get_object_or_404(One_answer, pk=i3)
            onee3.answer_description = request.POST['answer_description3']
            onee3.answer_variant = request.POST['answer_variant3']
            onee3.answer_point = request.POST['answer_point3']
            onee3.save()
            return redirect('/quiz/')
        else:
            template = loader.get_template('exams/ModifOneAnswer.html')
            context = {
                'question': question

            }
            return HttpResponse(template.render(context, request))


def modifmulti(request, question_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)
        if request.method == 'POST':

            question.question_text = request.POST['Description']
            question.footer_text = request.POST['Footer']
            question.header_text = request.POST['Header']
            question.success_message = request.POST['Success']
            question.fail_message = request.POST['Fail']
            question.point = request.POST['points']
            question.save()
            i1 = request.POST['id1']
            i2 = request.POST['id2']
            i3 = request.POST['id3']
            multi1 = get_object_or_404(MultiChoice, pk=i1)
            multi1.multi_description = request.POST['answer_description1']
            multi1.multi_variant = request.POST['answer_variant1']
            multi1.choice_point = request.POST['points1']
            multi1.question = question
            multi1.save()
            multi2 = get_object_or_404(MultiChoice, pk=i2)
            multi2.multi_description = request.POST['answer_description2']
            multi2.multi_variant = request.POST['answer_variant2']
            multi2.choice_point = request.POST['points2']
            multi2.save()
            multi3 = get_object_or_404(MultiChoice, pk=i3)
            multi3.multi_description = request.POST['answer_description3']
            multi3.multi_variant = request.POST['answer_variant3']
            multi3.choice_point = request.POST['points3']
            multi3.save()
            return redirect('/quiz/')
        else:
            template = loader.get_template('exams/ModifMultiAnswer.html')
            context = {
                'question': question

            }
            return HttpResponse(template.render(context, request))


def modifFree(request, question_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)
        if request.method == 'POST':

            question.question_text = request.POST['Description']
            question.footer_text = request.POST['Footer']
            question.header_text = request.POST['Header']
            question.success_message = request.POST['Success']
            question.fail_message = request.POST['Fail']
            question.point = request.POST['points']
            question.save()
            i = request.POST['id']
            free = get_object_or_404(Free_text, pk=i)
            free.answer_text = request.POST['text']
            free.save()
            return redirect('/quiz/')
        else:
            template = loader.get_template('exams/ModifFreeText.html')
            context = {
                'question': question

            }
            return HttpResponse(template.render(context, request))


def deleteQuest(request, question_id):
    if request.user.is_authenticated:
        Question.objects.filter(pk=question_id).delete()
        return redirect('/quiz/')


def envoie(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST['Description']:
            question = Question()
            question.exam = Exam.objects.get(pk=request.session['id'])
            question.question_text = request.POST['Description']
            question.footer_text = request.POST['Footer']
            question.header_text = request.POST['Header']
            question.success_message = request.POST['Success']
            question.fail_message = request.POST['Fail']
            question.point = request.POST['points']
            type_quest = request.POST['type']
            question.save()
            if type_quest == 'one':
                one1 = One_answer()
                one1.answer_description = request.POST['answer_description1']
                one1.answer_variant = request.POST['answer_variant1']
                one1.answer_point = request.POST['answer_points1']
                one1.question = question
                one1.save()
                one2 = One_answer()
                one2.answer_description = request.POST['answer_description2']
                one2.answer_variant = request.POST['answer_variant2']
                one2.answer_point = request.POST['answer_points2']
                one2.question = question
                one2.save()
                one3 = One_answer()
                one3.answer_description = request.POST['answer_description3']
                one3.answer_variant = request.POST['answer_variant3']
                one3.answer_point = request.POST['answer_points3']
                one3.question = question
                one3.save()
            if type_quest == 'multi':
                multi1 = MultiChoice()
                multi1.question = question
                multi1.multi_description = request.POST['answer_descriptionm1']
                multi1.multi_variant = request.POST['answer_variantm1']
                multi1.choice_point = request.POST['pointsm1']
                multi1.save()
                multi2 = MultiChoice()
                multi2.question = question
                multi2.multi_description = request.POST['answer_descriptionm2']
                multi2.multi_variant = request.POST['answer_variantm2']
                multi2.choice_point = request.POST['pointsm2']
                multi2.save()
                multi3 = MultiChoice()
                multi3.question = question
                multi3.multi_description = request.POST['answer_descriptionm3']
                multi3.multi_variant = request.POST['answer_variantm3']
                multi3.choice_point = request.POST['pointsm3']
                multi3.save()
            if type_quest == 'free':
                free = Free_text()
                free.question = question
                free.answer_text = request.POST['text']
                free.save()
        return render(request, 'exams/createQuest.html')


x = 0
liste = []
bliste = []
w = 0


def passer(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)

    global liste
    global bliste
    global x
    q = Question.objects.filter(exam=exam)
    l = []
    for i in q:
        l.append(i.id)
    liste = sample(l, k=len(l))
    bliste = [False] * len(liste)
    x = 0
    return render(request, 'exams/passerExam.html', {'exam1': exam,
                                                     'exam1_id': exam_id,
                                                     'y': liste[0]})


def passer2(request, exam_id, question_id):
    global liste
    global bliste
    global x
    global w
    first = 0

    exam1 = Exam.objects.get(pk=exam_id)
    q = Question.objects.filter(exam=exam1)

    question = Question.objects.get(pk=question_id)
    if x == len(liste) - 1:
        bliste[x] = True
    x = liste.index(question.id)
    if request.method == 'POST':
        if w == 0:
            bliste[x - 1] = True
            first = 1
        else:
            bliste[x] = True

        rep = Reponse()
        rep.user = request.user
        rep.exam = exam1
        if 'radios' in request.POST:
            c = request.POST['radios']
            a = One_answer.objects.get(pk=c)
            rep.one_answer = a
            rep.score = a.answer_point
            rep.save()
        elif 'radiosM' in request.POST:
            c = request.POST['radiosM']
            a = MultiChoice.objects.get(pk=c)
            rep.multichoice = a
            rep.score = a.choice_point
            rep.save()
        else:
            c = request.POST['text']
            rep.free_text = c
            # score for free text question for review
            rep.score = 2
            rep.save()
        x = x + 1
        if x < len(liste):

            context = {
                'examen_id': exam_id,
                'examen': exam1,
                'quest_id': question_id,
                'quest': question,
                'liste': liste,
                'i': liste[x],
                'bliste': bliste,
                'first': first,
            }

            return render(request, "exams/ExamQuest.html", context)
            w = w + 1

            # in last question, submit redirect to first question not submitted in list if exist else to result
        else:

            if liste[bliste.index(False)] >= 0:
                context = {'examen_id': exam_id,
                           'examen': exam1,
                           'quest_id': question_id,
                           'quest': question,
                           'liste': liste,
                           'bliste': bliste,
                           'i': liste[bliste.index(False)],
                           'first': first,
                           }

                return render(request, "exams/ExamQuest.html", context)
            else:
                return result(request, exam_id)

    else:
        if x < len(liste) - 1:

            context = {
                'examen_id': exam_id,
                'examen': exam1,
                'quest_id': question_id,
                'quest': question,
                'liste': liste,
                'bliste': bliste,
                'i': liste[x + 1],
                'first': first,

            }
        else:
            context = {
                'examen_id': exam_id,
                'examen': exam1,
                'quest_id': question_id,
                'quest': question,
                'liste': liste,
                'bliste': bliste,
                'i': liste[bliste.index(False)],
                'first': first,
            }
        return render(request, "exams/ExamQuest.html", context)


def result(request, exam_id):
    score = 0
    exam = Exam.objects.get(pk=exam_id)
    listeRep = Reponse.objects.filter(exam=exam, user=request.user)
    for res in listeRep:
        score += res.score
    context = {
        'username': request.user,
        'examen_id': exam_id,
        'exam': exam,
        'score': score,
    }
    print(score)

    return render(request, "exams/result.html", context)


def reponse(request, exam_id):
    return 0
