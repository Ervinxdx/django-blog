from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegistrarionForm
from blogs.models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import Group
def home(request):
    #ALL SE USA PARA OBTENER TODOS LOS DATOS .SE PUDE USAR CAULQUIER VARIALBE PERO QUE REPRESENTE EL DATO QUE CONTIENE
    posts = Blog.objects.filter(is_featured=True).order_by('-update_at') #CONTROL + . PARA IMPORTAR MAS FACIL :)

    context = {
        'featured_posts' : posts
    }
    #print(categories) #PODEMOS COMPROBAR ASI SI FUNCIONO EL CODIGO
    return render(request, 'home.html',context) # NO OLVIDAR TAMBIEN AGREGAR CONTEXT PARA MOSTRAR EN LA PAGINA

def register(request):
    if request.method == 'POST':
        form = RegistrarionForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name ='blog_group')
            group.user_set.add(user)
            return redirect('register')
    else:
        form =RegistrarionForm()
    
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()    
    context = {
        'form' : form
    }
    return render(request,'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')