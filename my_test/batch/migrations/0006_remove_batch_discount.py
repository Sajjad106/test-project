# Generated by Django 4.2.5 on 2023-10-22 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0005_alter_batch_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='discount',
        ),
    ]
