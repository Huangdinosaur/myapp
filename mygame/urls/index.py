from mygame.views.index import index
from django.urls import path,include 
urlpatterns=[
    path("",index,name="index"),
    path("menu/",include("mygame.urls.menu.index")),
    path("playground/",include("mygame.urls.playground.index")),
    path("settings/",include("mygame.urls.settings.index"))

]
