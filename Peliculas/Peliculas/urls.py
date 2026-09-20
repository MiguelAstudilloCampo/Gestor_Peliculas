"""
URL configuration for Peliculas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from appPeliculas import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('', views.inicioTipos, name='inicioTipos'),
    path('', views.listarPeliculas, name='listarPeliculas'),
    path('Peliculas/tipo/<int:tipo_id>/', views.listarPeliculas, name='listarPeliculasPorTipo'),
    path('vistaAgregargenero/', views.vistaAgregargenero, name='vistaAgregargenero'),
    path('agregarGenero/', views.agregarGenero, name='agregarGenero'),
    path('vistaAgregarPelicula/', views.vistaAgregarPeliculas, name='vistaAgregarPeliculas'),
    path('agregarPelicula/', views.agregarPelicula, name='agregarPelicula'),
    path('consultarPelicula/<int:id>/', views.consultarPelicula, name='consultarPelicula'),
    path('actualizarPelicula/', views.actualizarPelicula, name='actualizarPelicula'),
    path('eliminarPelicula/<int:id>/', views.eliminarPelicula, name='eliminarPelicula'),
    path('vistaAgregartipo/', views.vistaAgregartipo, name='vistaAgregartipo'),
    path('agregarTipo/', views.agregarTipo, name='agregarTipo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)