# Generated by Django 4.0.3 on 2022-03-08 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0003_alter_students_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
