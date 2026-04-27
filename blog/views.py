from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def message1(request) :
    return HttpResponse('Я всегда очень дружески отношусь к тем, кто мне безразличен. Оскар Уайльд')

def message2(request) :
    return HttpResponse('Замечательный день сегодня. То ли чай пойти выпить, то ли повеситься. Антон Павлович Чехов')

def message3(request) :
    return HttpResponse('У меня нет времени на то, чтобы быть несчастным. Стивен Кинг')