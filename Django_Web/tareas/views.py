from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm, PerfilForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout as auth_logout

@login_required
def perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = PerfilForm(instance=request.user)

    return render(request, "tareas/perfil.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_tareas')
    else:
        form = AuthenticationForm()
    return render(request, 'tareas/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('login')


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 🔑 Loguea automáticamente al registrarse
            return redirect('lista_tareas')
    else:
        form = UserCreationForm()
    return render(request, 'tareas/registro.html', {'form': form})


@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(owner=request.user)
    return render(request, 'tareas/lista.html', {'tareas': tareas})


@login_required
def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.owner = request.user
            tarea.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear.html', {'form': form})


@login_required
def editar_tarea(request, tarea_id):  # 👈 nombre debe coincidir con urls.py
    tarea = get_object_or_404(Tarea, id=tarea_id)
    form = TareaForm(request.POST or None, instance=tarea)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_tareas")

    return render(request, "tareas/editar.html", {"form": form, "tarea": tarea})


@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, owner=request.user)
    if request.method == "POST":
        tarea.delete()
        return redirect('lista_tareas')


@login_required
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, owner=request.user)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')
