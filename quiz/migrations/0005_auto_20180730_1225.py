# Generated by Django 2.0.7 on 2018-07-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('quiz', '0004_auto_20180730_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_text',
            name='answer_text',
            field=models.CharField(default=' ', max_length=600, verbose_name='answer_text'),
        ),
    ]
