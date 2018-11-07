# blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tabuleiro$', views.tabuleiro, name='tabuleiro'),
    url(r'^vd$', views.videogame, name='videogame'),
    url(r'^obrigada$', views.obrigada, name='obrigada'),
    url(r'^google3d8ceef29a3d0cf1', name='google'),
]
