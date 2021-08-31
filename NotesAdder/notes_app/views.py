"""from django.views.generic import TemplateView

# Create your views here.
app_name = 'notes_app'

class IndexPage(TemplateView):
    template_name = 'notes_app/index.html'"""

import random

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .models import Note


def home_view(request):
    # note_obj = Note.objects.get(id = 2)
    note_objs = Note.objects.all()
    # import pdb;pdb.set_trace()
    print("")
    context = {
        "notes": note_objs
    }

    index = render_to_string("notes_app\index.html",context)

    return HttpResponse(index)


def delete_view(request, id):
    note_obj = Note.objects.get(id = id)
    note_obj.delete()
    # note_obj.save()

    index = render_to_string("notes_app\delete.html")

    return HttpResponse(index)

def add_view(request):
    page = render_to_string("notes_app/note_add.html")
    return HttpResponse(page)


def add_note(request):
    # import pdb;pdb.set_trace();
    # note_objs = Note.objects.add()
    if request.method == 'GET':
        content = request.GET.get('content','Empty Note')
        note_obj = Note()
        # note_obj = note_objs.objects.get(id)
        note_obj.content = content
        note_obj.save()
        # return HttpResponse("notes_app\index.html")
        return home_view(request)

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "notes_app/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "notes_app/login_view.html", context)
