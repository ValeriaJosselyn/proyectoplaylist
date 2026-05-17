from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cancion, Comentario

# 1. Lista principal de canciones
def lista_musica(request):
    canciones = Cancion.objects.all().order_by('-fecha_agregada')
    return render(request, 'blog/publicaciones.html', {'canciones': canciones})

# 2. Formulario para agregar canciones (con validación de título)
def agregar_cancion(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        
        if not titulo:
            return render(request, "blog/crear.html", {"error": "El título de la canción es completamente obligatorio."})
        
        Cancion.objects.create(
            titulo=titulo,
            artista=request.POST.get("artista", "Desconocido"),
            foto_url=request.POST.get("foto_url", ""),
            album=request.POST.get("album", ""),
            genero=request.POST.get("genero", "Pop"),
            letra=request.POST.get("letra", "")
        )
        return redirect("lista_musica")
    return render(request, 'blog/crear.html')

# 3. Vista para ver la letra de la canción y dejar comentarios
def detalle_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        texto = request.POST.get("texto")
        if nombre and texto:
            Comentario.objects.create(cancion=cancion, nombre=nombre, texto=texto)
            return redirect('detalle_cancion', cancion_id=cancion.id)
            
    return render(request, 'blog/detalle.html', {'cancion': cancion})

# 4. Endpoint de la API JSON
def api_canciones(request):
    data = Cancion.objects.all().values('id', 'titulo', 'artista', 'genero')
    return JsonResponse(list(data), safe=False)