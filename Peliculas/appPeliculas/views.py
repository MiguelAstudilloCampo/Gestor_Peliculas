from django.shortcuts import render;
from django.conf import settings;
from django.db import Error;
from appPeliculas.models import genero, peliculas, tipo;
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render, redirect
import os

# Create your views here.

def inicio (request):
    return render (request, "inicio.html");

def vistaAgregargenero(request):
    return render (request, "agregarGenero.html");

@csrf_exempt
def agregarGenero (request):
    try :
        nombre = request.POST['nombre'];
        #Crear objeto de tipo genero
        gener = genero(gen_nombre=nombre);
        #Salvar el genero y guardarlo en la base de datos
        gener.save();
        mensaje = "Genero agrgado exitosamente";
    except Error as error :
        mensaje = str(error);
    
    retorno = {"mensaje":mensaje};
    # return JsonResponse(retorno);
    return render(request, "agregarGenero.html", retorno);


def vistaAgregartipo(request):
    return render (request, "agregartipo.html");


@csrf_exempt
def agregarTipo(request):
    if request.method != "POST":
        return render(request, "agregartipo.html")

    try:
        nombre = request.POST.get("nombre")
        type = tipo(tip_nombre=nombre)
        type.save()
        mensaje = "Tipo agregado exitosamente"
    except Error as error:
        mensaje = str(error)

    return render(request, "agregartipo.html", {"mensaje": mensaje})


def listarPeliculas(request, tipo_id=None):
    if tipo_id:
        movies = peliculas.objects.filter(pel_tipo_id=tipo_id)
        tipo_actual = tipo.objects.get(id=tipo_id)
    else:
        movies = peliculas.objects.all()
        tipo_actual = None

    tipos = tipo.objects.all()

    retorno = {
        "movies": movies,
        "tipo_actual": tipo_actual,
        "tipos": tipos
    }

    return render(request, "listarPeliculas.html", retorno)

def inicioTipos (request):
    tipos = tipo.objects.all();
    
    retorno = {"tipos" : tipos}
    
    # return JsonResponse(retorno);
    return render (request, "inicio.html", retorno)


def vistaAgregarPeliculas (request):
    generos = genero.objects.all()
    tipos = tipo.objects.all()
    
    retorno = {"generos":generos,
               "tipos":tipos}
    
    return render (request, "agregarPelicula.html", retorno)

# @csrf_exempt
def agregarPelicula (request):
    try:
        ##codigo = request.POST["cod"]
        titulo = request.POST["title"]
        protagonista = request.POST["prota"]
        duracion = int(request.POST["dure"])
        sinopsis = request.POST["sinop"]
        foto = request.FILES["photo"]
        idGenero = request.POST["idGenero"]
        idTipo = request.POST["idTipo"]
        
        visto_input = request.POST.get("pel_visto")
        pel_visto_valor = True if visto_input in ["Si", "true", "True", "1", "on"] else False
        
        gener = genero.objects.get(pk=idGenero)
        tip = tipo.objects.get(pk=idTipo)
        
        peli = peliculas (##pel_codigo = codigo,
                          pel_titulo = titulo,
                          pel_protagonista = protagonista,
                          pel_duracion = duracion,
                          pel_sinopsis = sinopsis,
                          pel_foto = foto,
                          pel_genero = gener,
                          pel_tipo = tip,
                          pel_visto = pel_visto_valor)
        
        peli.save()
        mensaje ="Pelicula agregada exitosamente"
        
        
    except Error as error :
        mensaje = str (error);
    
    retorno = {"mensaje":mensaje, 'idPelicula':peli.id}
    
    # return JsonResponse (retorno)
    return render (request, "agregarPelicula.html", retorno);


def consultarPelicula(request, id):
    pelicula = peliculas.objects.get(pk=id)
    generos = genero.objects.all()
    tipos = tipo.objects.all()
    retorno = {"pelicula":pelicula, "generos":generos, "tipos":tipos}
    return render(request,"actualizarPelicula.html",retorno)

def actualizarPelicula(request):
    try:
        idPelicula = request.POST['idPelicula']
        peliculaActualizar = peliculas.objects.get(pk=idPelicula)
        
        ##peliculaActualizar.pel_codigo = request.POST["cod"]
        peliculaActualizar.pel_titulo = request.POST["title"]
        peliculaActualizar.pel_protagonista = request.POST["prota"]
        peliculaActualizar.pel_duracion = int(request.POST["dure"])
        peliculaActualizar.pel_sinopsis = request.POST["sinop"]
        
        visto_input = request.POST.get("pel_visto")
        peliculaActualizar.pel_visto = True if visto_input in ["Si", "true", "True", "1", "on"] else False
        
        
        if 'photo' in request.FILES:
            foto = request.FILES["photo"]
            if peliculaActualizar.pel_foto:
                os.remove(os.path.join(settings.MEDIA_ROOT, str(peliculaActualizar.pel_foto)))
            peliculaActualizar.pel_foto = foto
        
        idGenero = int(request.POST["idGenero"])
        
        gener = genero.objects.get(pk=idGenero)
        peliculaActualizar.pel_genero = gener
        
        idTipo = int(request.POST["idTipo"])
        
        tip = tipo.objects.get(pk=idTipo)
        peliculaActualizar.pel_tipo = tip
        peliculaActualizar.save()
        
        mensaje = "Película actualizada exitosamente"
        
    except Error as error:
        mensaje = str(error)
    
    retorno = {"mensaje": mensaje}
    
    return redirect("/")


def eliminarPelicula(request, id):
    try:
        peliculaEliminar = peliculas.objects.get(pk=id)
        peliculaEliminar.delete()
        mensaje = "Pelicula Eliminada Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno={"mensaje":mensaje}
    return redirect ("/")