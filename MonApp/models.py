from django.contrib import admin
from django.db import models
from django.forms import forms
from django.contrib.auth.models import User
from django.urls import reverse


class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=25)
    adresse = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="photos")
    cv = models.FileField(upload_to="cv")
    domaine = models.CharField(max_length=45)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name



class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'adresse', 'image', 'cv', 'domaine', 'desc']
    list_filter = ('name',)
    search_fields = ['name']
