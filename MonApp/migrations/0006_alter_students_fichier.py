# Generated by Django 4.0.3 on 2022-03-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0005_remove_students_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='fichier',
            field=models.FileField(upload_to='media/dossier/'),
        ),
    ]
