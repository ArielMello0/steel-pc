from django.urls import path
from AppProyecto.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),

    path('logout/', LogoutView.as_view(template_name='AppProyecto/logout.html'), name="logout"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),

    
    path('busquedaNumBlog/', busquedaNumBlog, name="busquedaNumBlog"),
    path('buscar/', buscar, name="buscar"),


    path('autorFormulario/', autorFormulario, name="autorFormulario"),
    path('crearFormAutor/', crearFormAutor, name="crearFormAutor"),
    path('leerAutor/', leerAutor, name="leerAutor"),
    path('eliminarAutor/<id>', eliminarAutor, name="eliminarAutor"),
    path('editarAutor/<id>', editarAutor, name="editarAutor"),
    
    
    path('suscriptorFormulario/', suscriptorFormulario, name="suscriptorFormulario"),
    path("crearFormSuscriptor/", crearFormSuscriptor, name="crearFormSuscriptor"),
    path('leerSuscriptor/', leerSuscriptor, name="leerSuscriptor"),
    path('eliminarSuscriptor/<id>', eliminarSuscriptor, name="eliminarSuscriptor"),
    path('editarSuscriptor/<id>', editarSuscriptor, name="editarSuscriptor"),
   
    path('blogFormulario/', blogFormulario, name="blogFormulario"),
    path("crearFormBlog/", crearFormBlog, name="crearFormBlog"),
    path('eliminarBlog/<id>', eliminarBlog, name="eliminarBlog"),
    path('leerBlog/', leerBlog, name="leerBlog"),
    path('editarBlogs/<id>',editarBlogs , name="editarBlogs"),
    



]