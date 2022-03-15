from django.contrib import admin
from .models import Students, StudentsAdmin

# Register your models here.
admin.site.register(Students, StudentsAdmin)
