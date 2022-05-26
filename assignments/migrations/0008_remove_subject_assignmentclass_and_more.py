# Generated by Django 4.0.2 on 2022-05-26 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0007_subject_assignmentclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='assignmentClass',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignmentClass',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='assignments.subject'),
        ),
    ]