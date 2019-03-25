from django.conf.urls import url
from readinghub import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recommend_a_book/(?P<username>[\w\-]+)/$', views.recommend_a_book, name='recommend_a_book'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/recommend_book/(?P<username>[\w\-]+)/$', views.recommend_book, name='recommend_book'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<book_name_slug>[\w\-]+)/$', views.show_book, name='show_book'),
    url(r'^about/$', views.about, name='about'),
    url(r'^book/$', views.all_book, name='book'),
    url(r'^event/$', views.event, name='event'),
    url(r'^events/(?P<event_name_slug>[\w\-]+)/$', views.show_event, name='show_event'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^like/$', views.like_book, name='like_book'),
    url(r'^join/$', views.join_event, name='join_event'),
]
