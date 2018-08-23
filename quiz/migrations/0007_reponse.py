# Generated by Django 2.0.7 on 2018-08-06 11:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0006_exam_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_text', models.CharField(default='', max_length=1000)),
                ('score', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Exam',
                                           to='quiz.Exam')),
                ('multichoice',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_choice_answer',
                                   to='quiz.MultiChoice')),
                ('one_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='One_answer',
                                                 to='quiz.One_answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]