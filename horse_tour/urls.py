from django.urls import path
from . import views

urlpatterns = [ 
    path('tourists/', views.tour_list_view, name='tour_list'),
    path('tourist/<int:pk>/', views.tourist_detail_view, name='tourist_detail'),
]