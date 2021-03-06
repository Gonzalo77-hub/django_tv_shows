from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def redir(request):
    return redirect("/Shows")

def crear(request):

    errors= Show.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect("/Shows/New")
    else:

        titulo = request.POST['title']
        network = request.POST['Network']
        release = request.POST['Release']
        description = request.POST['desc']
        show = Show.objects.create(
        title=titulo, 
        network=network, 
        Release=release,
        desc= description,)
        messages.success(request, "Show de TV agregado correctamente")


        return redirect(f"/Shows/{show.id}")

def index(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(request, 'index2.html', context)


def second(request):
    return render(request, 'index.html')

def info_show(request, val):
    variable = {
         'tv': Show.objects.get(id=val),
    }
    return render(request, 'show.html', variable)

def edit_show(request, val):
    variable = {
        'programa': Show.objects.get(id=val)
    }
    return render(request, 'edit.html', variable)

def edit(request):
    print(request.POST)
    errors= Show.objects.edit_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f"/Shows/{request.POST['id_show']}/edit")
    else:
        ed_title = request.POST['edit_title']
        ed_network =request.POST['edit_Network']
        ed_release = request.POST['edit_releaseDate']
        ed_desc = request.POST['edit_desc']
        id_programa = request.POST['id_show']
        program = Show.objects.get(id=id_programa)
        program.title = ed_title
        program.network = ed_network
        program.Release = ed_release
        program.desc = ed_desc
        program.save()
        messages.success(request, "Show de TV editado correctamente")

        return redirect("/Shows")
def delete(request, val):
    borr = Show.objects.get(id=val)
    borr.delete()
    
    return redirect("/Shows")



