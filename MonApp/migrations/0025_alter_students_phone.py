# Generated by Django 4.0.3 on 2022-03-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0024_alter_students_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='phone',
            field=models.IntegerField(max_length=25),
        ),
    ]
