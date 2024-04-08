from http.client import HTTPResponse
import json
from django.shortcuts import redirect, render
from django.http import  JsonResponse
from disco.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    song=songs.objects.filter(status=0)
    return render(request,"images/index.html",{"song":song})

def search(request):
    query = request.GET.get('query')
    song = songs.objects.all()
    qs = song.filter(name__icontains=query)
    return render(request, 'images/search.html', {"songs": qs})

def register(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      return redirect('/login')
  return render(request,"images/register.html",{'form':form})

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      fav_id=data['pid']
      product_status=songs.objects.get(id=fav_id)
      if product_status:
          if Favorite.objects.filter(user=request.user.id,song_like_id=fav_id):
            return JsonResponse({'status':'Song Already in Favourite'}, status=200)
          else:
            Favorite.objects.create(user=request.user,song_like_id=fav_id)
            return JsonResponse({'status':'Song Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
  
def LL_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      fav_id=data['pid']
      product_status=songs.objects.get(id=fav_id)
      if product_status:
          if Favorite.objects.filter(user=request.user.id,song_like_id=fav_id):
            return JsonResponse({'status':'Song Already in Listen later'}, status=200)
          else:
            Favorite.objects.create(user=request.user,song_like_id=fav_id)
            return JsonResponse({'status':'Song Added to Listen later'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)

def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favorite.objects.filter(user=request.user)
    return render(request,"images/fav.html",{"fav":fav})
  else:
    return redirect("/")

def LLviewpage(request):
  if request.user.is_authenticated:
    fav=Favorite.objects.filter(user=request.user)
    return render(request,"images/watch_later.html",{"fav":fav})
  else:
    return redirect("/")
  
def remove_fav(request,fid):
  item=Favorite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")

def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")


def login_page(request):
  if request.user.is_authenticated:
    return redirect("/home")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/home")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"images/login.html")
  
def Category_select(request):
    gory=category.objects.filter(status=0)
    return render(request,"images/Category.html",{"category":gory})

def Category_selectviews(request,name):
    if(category.objects.filter(name=name,status=0)):
        song=songs.objects.filter(category_name=name)
        return render(request,"images/song_page/index.html",{"songs":song,"cat":name})
    else:
        messages.warning(request,"No category found")
        return redirect('category_select')
  
def llviews(request,name):
    if(songs.objects.filter(name=name,status=0)):
        song=songs.objects.filter(name=name).first()
        return render(request,"images/song_page/ll_details.html",{"c_song":song})
    else:
        messages.warning(request,"No song found")
        return redirect('category_select')

def Trend_views(request,sname):
    if(songs.objects.filter(name=sname,status=0)):
        song=songs.objects.filter(name=sname,status=0).first()
        return render(request,"images/song_page/song_details.html",{"c_song":song})
    else:
        messages.warning(request,"No song found")
        return redirect('category_select')
   
    

def song_details(request,cname,sname):
    if(category.objects.filter(name=cname,status=0)):
        if(songs.objects.filter(name=sname,status=0)):
            song=songs.objects.filter(name=sname,status=0).first()
            return render(request,"images/song_page/song_details.html",{"c_song":song,"cn":cname})
        else:
            messages.warning(request,"No song found")
            return redirect('category_select')
    else:
        messages.warning(request,"No category found")
        return redirect('category_select')
    
def Trends(request):
    trend=songs.objects.filter(Trending=1)
    return render(request,"images/trend.html",{"Trend_songs":trend})