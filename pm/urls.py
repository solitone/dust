from django.conf.urls import url

from . import views

urlpatterns = [
# ex: /pm/
    url(r'^$', views.index, name='index'),
# ex: /pm/chart/
    url(r'^chart/$', views.chart, name='chart'),
# ex: /pm/pm25series/
    url(r'^pm25series/$', views.pm25series, name='pm25series'),
# ex: /pm/pmseries/
    url(r'^pmseries/$', views.pmseries, name='pmseries'),
# ex: /pm/save/
    url(r'^save/$', views.save, name='save'),
]