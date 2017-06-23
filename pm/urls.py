from django.conf.urls import url

from . import views

urlpatterns = [
# ex: /pm/
    url(r'^$', views.index, name='index'),
# ex: /pm/save/
    url(r'^save/$', views.save, name='save'),
]