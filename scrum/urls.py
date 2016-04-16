from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^usr_logout/$', views.usr_logout, name='usr_logout'),
]