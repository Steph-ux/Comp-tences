# Generated by Django 4.0.3 on 2022-03-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0020_alter_students_adresse_alter_students_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='adresse',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]