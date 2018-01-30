from . models import Character, Movie, Game
from django.shortcuts import render,get_object_or_404,redirect


def IndexView(request):
    template_name= "wiki/index.html"
    return render(request,template_name)


def IndexMovie(request):
    movie=Movie.objects.filter(Type="0")
    template_name="wiki/indexMovie.html"
    return render(request,template_name,{"movie":movie})



def IndexCartoon(request):
    cartoon=Movie.objects.filter(Type="1")
    template_name="wiki/indexCartoon.html"
    return render(request,template_name,{"movie":cartoon})



def IndexDarkside(request):
    darkside =  Character.objects.filter(Side="0")
    template_name="wiki/indexDarkside.html"
    return render(request,template_name,{"char":darkside})

def IndexLightside(request):
    lightside =  Character.objects.filter(Side="1")
    template_name="wiki/indexLightside.html"
    return render(request,template_name,{"char":lightside})


def IndexGames(request):
    games=Game.objects.all()
    template_name="wiki/indexGames.html"
    return render(request,template_name,{"games":games})



def IndexHome(request):
    template_name="wiki/indexHome.html"
    return render(request,template_name)


def IndexStory(request):
    template_name="wiki/indexStory.html"
    return render(request,template_name)

def CharDetail(request, pk):
    template_name = "wiki/details.html"
    model = get_object_or_404(Character,pk=pk)
    return render(request,template_name,context={"object":model})
