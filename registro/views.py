from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .forms import RegForm, RegModelForm
#from .models import Registrado
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

#def Login(request):
    

 #   form = RegModelForm(request.POST or None)
  #  if form.is_valid():
   #     instance = (form.save(commit=False))
    #    instance.save()
     #   print (instance)
        #form_data = (form.cleaned_data)
        #abc = (form_data.get("email"))
        #abc2 = (form_data.get("nombre"))
        #obj = (Registrado.objects.create(email=abc, nombre=abc2))
        #print (form_data.get("edad"))
    #context = {
     #   "el_form": form,
        
    #}
   # return render(request,"Login1.html", context)
    
def inicio(request):
    
    return render (request,"index.html")

def artistas(request):
    
    return render (request,"Artistas.html")
def servicios(request):
    
    return render (request,"Servicios.html")
def dref(request):
    
    return render (request,"DrefQuila.html")
def PoztMalone(request):
    
    return render (request,"PoztMalone.html")
def Chriz(request):
    
    return render (request,"ChristianFrench.html")
def princi(request):

    return render (request,"inicio.html")

def zervicioz(request):

    return render (request,"zervicioz.html")
#def registrar(request):
    #if request.method == "POST":
       # form = UserCreationForm(request.POST)
       # if form.is_valid():
        #    user = form.save()
         #   username = form.cleaned_data.get('username')
          #  messages.success(request,f"new account created: {username}")
           # login(request, user)
            #messages.info(request, f"you are now logged in as {username}")
            #return redirect("templates:inicio")
       # else:
        #    for msg in form.error_messages:
         #       messages.error(request, f"{msg}:{form.error_messages[msg]}")

#    form = UserCreationForm
 #   return render(request, "templates/Login.html",context={"form":form})

#def logout_request(request):
 #   logout(request)
  #  messages.info(request, "Logged out succesfully!")
   # return redirect("templates:inicio")

#def login_request(request):
    #if request.method == "POST":
        #form = AuthenticationForm(request, data=request.POST)
        #if form.is_valid():
            #username = form.cleaned_data('username')
            #password = form.cleaned_data('password')
           # user = authenticate (username)('password')
            #if user is not None:
                #login(request, user)
                #messages.info(request, f"you are now in logged in as {username}")
                #return redirect("templates:inicio")

    #form = AuthenticationForm()
    #return render(request,"templates/inicio",{"form":form} )  
