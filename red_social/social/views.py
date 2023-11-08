# social/views.py
from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirigir al inicio después del registro
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def inicio(request):
    # Lógica para la página de inicio (mostrar publicaciones, etc.)
    return render(request, 'inicio.html')


def perfil(request, usuario_id):
    # Lógica para ver el perfil de un usuario
    return render(request, 'perfil.html')

