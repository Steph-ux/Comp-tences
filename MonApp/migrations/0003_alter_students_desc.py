# Generated by Django 4.0.3 on 2022-03-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0002_alter_students_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]
