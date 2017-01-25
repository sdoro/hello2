from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^helloIP$', views.myIp, name='myIp'),
    url(r'^year$', views.year, name='year'),
    url(r'^month$', views.month, name='month'),
    url(r'^day$', views.day, name='day'),
    url(r'^empty$',views.empty),
    url(r'^emptyArgs$',views.emptyArgs),
]
