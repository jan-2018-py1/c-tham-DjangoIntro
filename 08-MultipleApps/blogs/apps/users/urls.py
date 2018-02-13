from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users/html$', views.html),
]