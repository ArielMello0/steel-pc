from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppProyecto.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render (request,"AppProyecto/inicio.html")

def nosotros(request):
    return render(request, "AppProyecto/nosotros.html")

@login_required
def blogFormulario(request):
    return render(request, "AppProyecto/blogFormulario.html",{"avatar":obtenerAvatar(request)})

@login_required
def crearFormBlog(request):
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            titulo=informacion["titulo"]
            num_blog=informacion["num_blog"]
            blog=Blog(titulo=titulo, num_blog=num_blog)
            blog.save()
            return render (request, "AppProyecto/inicio.html")
    
    else:
        formulario=BlogForm()
        return render (request, "AppProyecto/crearFormBlog.html", {"formulario":formulario})

@login_required
def leerBlog(request):
    blogs=Blog.objects.all()
    return render(request, "AppProyecto/leerBlog.html", {"blogs":blogs})

@login_required
def eliminarBlog(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    blogs=Blog.objects.all()
    return render(request, "AppProyecto/leerBlog.html",{"blogs":blogs})

@login_required
def editarBlog(request, id):
    blog=Blog.objects.get(id=id)
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            blog.titulo=informacion["titulo"]
            blog.num_blog=informacion["num_blog"]
            blog.save()
            blogs=Blog.objects.all()
            return render(request, "AppProyecto/leerBlog.html",{"blogs":blogs})
        
    else:
        form=BlogForm(initial={"titulo":blog.titulo, "num_blog":blog.num_blog})
        return render(request, "AppProyecto/editarBlog.html",{"formulario":form, "blog":blog})


@login_required
def autorFormulario(request):
    return render(request, "AppProyecto/autorFormulario.html",{"avatar":obtenerAvatar(request)})

@login_required
def crearFormAutor (request):
    if request.method=="POST":
        form=AutorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            profesion=informacion["profesion"]
            autor=Autor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            autor.save()
            autores=Autor.objects.all()
            return render(request, "AppProyecto/leerAutor.html", {"autores":autores})
    
    else:
        formulario=AutorForm()
        return render (request, "AppProyecto/crearFormAutor.html", {"formulario":formulario})

@login_required
def leerAutor(request):
    autores=Autor.objects.all()
    return render(request, "AppProyecto/leerAutor.html", {"autores":autores})

@login_required
def eliminarAutor(request, id):
    autor=Autor.objects.get(id=id)
    autor.delete()
    autores=Autor.objects.all()
    return render(request, "AppProyecto/leerAutor.html",{"autor":autor})

@login_required
def editarAutor(request, id):
    autor=Autor.objects.get(id=id)
    if request.method=="POST":
        form=AutorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            autor.nombre=informacion["nombre"]
            autor.apellido=informacion["apellido"]
            autor.email=informacion["email"]
            autor.profesion=informacion["profesion"]
            autor.save()
            autores=Autor.objects.all()
            return render(request, "AppProyecto/leerAutor.html",{"autores":autores})
        
    else:
        form=AutorForm(initial={"nombre":autor.nombre, "apellido":autor.apellido, "email":autor.email, "profesion":autor.profesion})
        return render(request, "AppProyecto/editarAutor.html",{"formulario":form, "autor":autor})
        

@login_required
def suscriptorFormulario(request):
    return render(request, "AppProyecto/suscriptorFormulario.html",{"avatar":obtenerAvatar(request)})

@login_required
def crearFormSuscriptor(request):
    if request.method=="POST":
        form=SuscriptorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            suscriptor=Suscriptor(nombre=nombre, apellido=apellido, email=email)
            suscriptor.save()
            return render (request, "AppProyecto/inicio.html")
    
    else:
        formulario=SuscriptorForm()
        return render (request, "AppProyecto/crearFormSuscriptor.html", {"formulario":formulario})



@login_required
def leerSuscriptor(request):
    suscriptores=Suscriptor.objects.all()
    return render(request, "AppProyecto/leerSuscriptor.html", {"suscriptores":suscriptores})

@login_required
def eliminarSuscriptor(request, id):
    suscriptor=Suscriptor.objects.get(id=id)
    suscriptor.delete()
    suscriptores=Suscriptor.objects.all()
    return render(request, "AppProyecto/leerSuscriptor.html",{"suscriptor":suscriptor})



@login_required
def editarSuscriptor(request, id):
    suscriptor=Suscriptor.objects.get(id=id)
    if request.method=="POST":
        form=SuscriptorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            suscriptor.nombre=informacion["nombre"]
            suscriptor.apellido=informacion["apellido"]
            suscriptor.email=informacion["email"]
            suscriptor.save()
            suscriptores=Suscriptor.objects.all()
            return render(request, "AppProyecto/leerSuscriptor.html",{"suscriptores":suscriptores}) 
    else:
        form=SuscriptorForm(initial={"nombre":suscriptor.nombre, "apellido":suscriptor.apellido, "email":suscriptor.email})
        return render(request,"AppProyecto/editarSuscriptor.html",{"formulario":form, "suscriptor":suscriptor})
        




###################################busquedassss

def busquedaNumBlog(request):
    return render(request,"AppProyecto/busquedaNumBlog.html")

def buscar(request):
    if request.GET["num_blog"]:
        num_blog=request.GET["num_blog"]
        blogs=Blog.objects.filter(num_blog=num_blog)
        return render(request, "AppProyecto/resultadosBusqueda.html", {"blogs":blog})
    else:
        return render(request, "AppProyecto/busquedaNumBlog.html", {"mensaje":"Ingrese un número de blog"})

#Vista para login

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppProyecto/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppProyecto/login.html", {"formulario":form,"mensaje":f"Usuario o contraseña incorrectos"})

        else:
            return render(request, "AppProyecto/login.html", {"formulario":form,"mensaje":f"Usuario o contraseña incorrectos"})

    else:
        form=AuthenticationForm()
        return render(request, "AppProyecto/login.html", {"formulario":form})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "AppProyecto/inicio.html", {"mensaje":f"Usuario {username} creado correctmante"})
        else:
            return render(request, "AppProyecto/register.html", {"formulario":form, "mensaje":"Formulario invalido"})

    
    else:
        form=UserRegisterForm()
        return render(request, "AppProyecto/register.html",{"formulario":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "AppProyecto/inicio.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "AppProyecto/editarPerfil.html", {"formulario":form, "usuario":usuario,"mensaje":"Formulario inválido"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, "AppProyecto/editarPerfil.html", {"formulario":form, "usuario":usuario})
##################################
@login_required
def agregarAvatar(request):
    if request.method=='POST':
        formulario=AvatarForm(request.POST,request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppProyecto/inicio.html', {'usuario':request.user, 'mensaje':'Avatar agregado exitosamente',"imagen": avatar.imagen.url})
        else:
            return render(request, 'AppProyecto/agregarAvatar.html', {'formulario':formulario, 'mensaje':'FORMULARIO INVALIDO'})

    else:
        formulario=AvatarForm()
        return render(request, "AppProyecto/agregar.html", {"formulario":formulario, "usuario":request.user})


@login_required
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/imagenPorDefecto.jpg"
    return imagen