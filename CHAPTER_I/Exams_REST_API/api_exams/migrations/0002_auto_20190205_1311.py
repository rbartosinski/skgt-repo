# Generated by Django 2.1.5 on 2019-02-05 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_exams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='task',
        ),
        migrations.AddField(
            model_name='exam',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_exams.Task'),
        ),
    ]