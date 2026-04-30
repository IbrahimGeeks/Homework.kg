from django.urls import path
from . import views

urlpatterns = [
    path('message1/', views.message1, name='message1'),
    path('message2/', views.message2, name='message2'),
    path('message3/', views.message3, name='message3'),
    path('', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
]