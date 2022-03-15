from django.urls import path
from .views import *
urlpatterns = [
    path('', dashb, name="dashb"),
    path('info', user_info, name="info"),
    path('ajouter_info', Addinfo.as_view(), name="ajouter_info"),
    path('update/<int:pk>', Updateinfo.as_view(), name="update"),
    path('delete/<int:pk>', Deleteinfo.as_view(), name="delete"),
]
