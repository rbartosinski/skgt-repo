# Generated by Django 2.1.5 on 2019-02-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='final_grade',
            field=models.IntegerField(null=True),
        ),
    ]
