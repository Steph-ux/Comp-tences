# Generated by Django 4.0.3 on 2022-03-11 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0018_rename_fichier_students_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
