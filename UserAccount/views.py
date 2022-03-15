import form as form
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from MonApp.formulaire import StudentsForm
from MonApp.models import Students


def dashb(request):
    return render(request, 'db.html')


def user_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    list_info = Students.objects.filter(user=request.user)
    return render(request, 'info.html', {'liste_info': list_info})


class Addinfo(CreateView):
    model = Students
    form_class = StudentsForm
    template_name = 'addinfo.html'
    success_url = 'info'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Addinfo, self).form_valid(form)


class Updateinfo(UpdateView):
    model = Students
    form_class = StudentsForm
    template_name = 'students_form.html'
    success_url = '/user/info'


class Deleteinfo(DeleteView):
    model = Students
    success_url = '/user/info'
