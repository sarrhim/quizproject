from django.contrib.auth.models import User
from django.db import models


class Exam(models.Model):
  
    name = models.CharField(max_length=64, verbose_name=u'Exam_name' ,default=" ")
    logo = models.ImageField(upload_to='logos',  null=True)
    description=models.CharField(max_length=600, verbose_name=u'Exam_descr' ,default=" ")
    category = models.CharField(max_length=200, verbose_name=u'category', default=" ")
    timer=models.IntegerField(default=0)
    mode = models.CharField(
        max_length=40,
        default='Training',
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=256, verbose_name=u'Question\'s text', default=" ")
    point=models.IntegerField(default=0)
    header_text = models.CharField(max_length=600, verbose_name=u'header\'s text', default=" ")
    footer_text = models.CharField(max_length=600, verbose_name=u'footer\'s text', default=" ")
    success_message = models.CharField(max_length=600, verbose_name=u'success\'s message', default=" ")
    fail_message = models.CharField(max_length=600, verbose_name=u'fail\'s message', default=" ")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,)

    def __str__(self):
        return "{content}".format(content=self.question_text)
class One_answer(models.Model):
    answer_variant=models.CharField(max_length=600, verbose_name=u'variant', default=" ")
    answer_description=models.CharField(max_length=600, verbose_name=u'description', default=" ")
    answer_point=models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer_variant
class Free_text(models.Model):
    answer_text=models.CharField(max_length=600, verbose_name=u'answer_text', default=" ")
    question = models.ForeignKey(Question, on_delete=models.CASCADE )
    def __str__(self):
        return self.answer_text

class MultiChoice(models.Model):
    multi_variant=models.CharField(max_length=600, verbose_name=u'variant', default=" ")
    multi_description=models.CharField(max_length=600, verbose_name=u'description', default=" ")
    choice_point=models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.multi_variant


class Reponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='Exam', default=1)
    one_answer = models.ForeignKey(One_answer, on_delete=models.CASCADE, related_name='One_answer', null=True)
    multichoice = models.ForeignKey(MultiChoice, on_delete=models.CASCADE, related_name='multi_choice_answer',
                                    null=True)
    free_text = models.CharField(max_length=1000, default='')
    score = models.IntegerField(default=0)


class studentClass(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prof', default=1)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam', default=0)
    email_invited = models.CharField(max_length=1000, default="")


class Invitation(models.Model):
    prof = models.ForeignKey(User, on_delete=models.CASCADE, related_name='professor', default=1)
    student = models.CharField(max_length=600, default=" ")
    exams = models.ForeignKey(Exam, on_delete=models.CASCADE, default=0)
