# Generated by Django 4.2.4 on 2023-09-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studententry',
            name='contact_no',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AddField(
            model_name='studententry',
            name='date_of_birth',
            field=models.DateField(blank=True, default='1988-01-01'),
        ),
        migrations.AddField(
            model_name='studententry',
            name='fathers_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='studententry',
            name='grade',
            field=models.CharField(default='A', max_length=12),
        ),
        migrations.AddField(
            model_name='studententry',
            name='gurdians_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='studententry',
            name='mothers_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='studententry',
            name='peresent_adress',
            field=models.TextField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='studententry',
            name='permanent_adress',
            field=models.TextField(default='N/A', max_length=100),
        ),
    ]
