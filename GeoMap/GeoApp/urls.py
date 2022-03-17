from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('', views.home, name='index'),
    path('map', views.map, name='map'),
    path('map_two', views.map_two, name='map_two'),
    path('map_ajax', views.map_ajax, name='map_ajax')
    # path('odata', views.oData, name='odata'),
    # path('no_data', views.oData, name='no_data'),

]
