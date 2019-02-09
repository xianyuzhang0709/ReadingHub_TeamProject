from django.conf.urls import url
from readinghub import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^about/$', views.about, name='about'),
    url(r'^book/$', views.book, name='book'),
    url(r'^event/$', views.event, name='event'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),


]