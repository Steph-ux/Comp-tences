# Generated by Django 4.0.3 on 2022-03-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0023_alter_students_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
