from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('routes/', views.routes, name='routes'),
    path('which_road/', views.which_road, name='which_road'),
    path('all_which_road/', views.all_which_road, name='all_which_road'),
    path('all_all_which_road/', views.all_all_which_road, name='all_all_which_road'),
    path('request/', views.request, name='request'),
    path('route_request/', views.route_request, name='route_request'),
    path('route_requests/', views.route_requests, name='route_requests'),
    path('result/', views.result, name='result'),
    path('descri/', views.descri, name='descri')
]
