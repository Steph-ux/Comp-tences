# Generated by Django 4.0.3 on 2022-03-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonApp', '0021_alter_students_adresse_alter_students_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='domaine',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
