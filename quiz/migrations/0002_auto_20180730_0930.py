# Generated by Django 2.0.7 on 2018-07-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multichoice',
            name='multi_description',
            field=models.CharField(default=' ', max_length=600, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='multichoice',
            name='multi_variant',
            field=models.CharField(default=' ', max_length=600, verbose_name='variant'),
        ),
        migrations.AlterField(
            model_name='one_answer',
            name='answer_description',
            field=models.CharField(default=' ', max_length=600, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='one_answer',
            name='answer_variant',
            field=models.CharField(default=' ', max_length=600, verbose_name='variant'),
        ),
    ]
