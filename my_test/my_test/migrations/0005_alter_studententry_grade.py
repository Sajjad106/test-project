# Generated by Django 4.2.4 on 2023-09-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_test', '0004_rename_gurdians_name_studententry_guardians_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studententry',
            name='grade',
            field=models.PositiveIntegerField(),
        ),
    ]
