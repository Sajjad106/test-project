# Generated by Django 4.2.5 on 2023-10-21 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0002_rename_time_batch_time_remove_batch_no_of_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='student_id',
        ),
    ]
