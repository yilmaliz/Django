from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.IndexView,name="index"),
     url(r'^detail/(?P<pk>[0-9]+)/$', views.CharDetail, name='detail'),
    url(r'^film/', views.IndexMovie,name="indexMovie"),
    url(r'^cartoon/', views.IndexCartoon,name="indexCartoon"),
    url(r'^darkside/', views.IndexDarkside,name="indexDarkside"),

    url(r'^lightside/', views.IndexLightside,name="indexLightside"),
    url(r'^games/', views.IndexGames,name="indexGames"),
    url(r'^story/',views.IndexStory,name="indexStory"),


]



