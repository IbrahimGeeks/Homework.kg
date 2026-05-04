from django.shortcuts import render, get_object_or_404
from .models import Tourist

def tourist_detail_view(request, pk):
    tourist = get_object_or_404(Tourist, pk=pk)
    return render(request, 'tour_detail.html', {'tourist': tourist})

def tour_list_view(request):
    tourists = Tourist.objects.all()
    return render(request, 'tour_list.html', {'tourists': tourists})