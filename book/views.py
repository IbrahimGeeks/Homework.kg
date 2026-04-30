from urllib import request

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . import models
# Create your views here.
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(request, 'book_detail.html', {'book': book_id})


def book_list_view(request):
    if request.method == 'GET':
        query_book = models.Book.objects.all().order_by('id')
        return render(request, 'book_list.html', {'book': query_book})





def message1(request) :
    return HttpResponse('Я всегда очень дружески отношусь к тем, кто мне безразличен. Оскар Уайльд')

def message2(request) :
    return HttpResponse('Замечательный день сегодня. То ли чай пойти выпить, то ли повеситься. Антон Павлович Чехов')

def message3(request) :
    return HttpResponse('У меня нет времени на то, чтобы быть несчастным. Стивен Кинг')