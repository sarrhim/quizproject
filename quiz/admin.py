from django.contrib import admin

from .models import Exam, Question, Free_text, MultiChoice, One_answer, Reponse, Invitation, studentClass

# Register your models here.
admin.site.register(Exam)
admin.site.register(Reponse)
admin.site.register(Question)
admin.site.register(Free_text)
admin.site.register(MultiChoice)
admin.site.register(One_answer)
admin.site.register(studentClass)
admin.site.register(Invitation)
