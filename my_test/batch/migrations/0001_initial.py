# Generated by Django 4.2.5 on 2023-10-03 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_test', '0011_rename_id_studententry_student_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('Time', models.CharField(max_length=50)),
                ('no_of_student', models.IntegerField()),
                ('description', models.TextField()),
                ('fee', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('module', models.TextField(max_length=11)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_test.studententry')),
            ],
        ),
    ]