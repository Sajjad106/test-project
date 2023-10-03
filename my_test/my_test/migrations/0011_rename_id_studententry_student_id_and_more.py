# Generated by Django 4.2.5 on 2023-10-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_test', '0010_alter_studententry_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studententry',
            old_name='id',
            new_name='student_id',
        ),
        migrations.AlterField(
            model_name='studententry',
            name='contact_no',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='studententry',
            name='grade',
            field=models.IntegerField(max_length=12),
        ),
    ]
