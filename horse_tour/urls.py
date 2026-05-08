from django.urls import path
from . import views

urlpatterns = [ 
    path('tourists/', views.tour_list_view, name='tour_list'),
    path('tourist/<int:pk>/', views.tourist_detail_view, name='tourist_detail'),
    path('tourist/create/', views.tourist_create_view, name='tourist_create'),
    path('tourist/<int:pk>/update/', views.tourist_update_view, name='tourist_update'),
    path('tourist/<int:pk>/delete/', views.tourist_delete_view, name='tourist_delete'),
    
]