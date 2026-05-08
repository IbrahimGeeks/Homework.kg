from django.shortcuts import render, get_object_or_404, redirect
from .models import Tourist
from .forms import TouristForm

def tour_list_view(request):
    tourists = Tourist.objects.all()
    return render(request, 'tour_list.html', {'tourists': tourists})

def tourist_detail_view(request, pk):
    tourist = get_object_or_404(Tourist, pk=pk)
    return render(request, 'tour_detail.html', {'tourist': tourist})

def tourist_create_view(request):
    form = TouristForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tour_list')
    return render(request, 'tour_form.html', {'form': form})

def tourist_update_view(request, pk):
    tourist = get_object_or_404(Tourist, pk=pk)
    form = TouristForm(request.POST or None, instance=tourist)
    if form.is_valid():
        form.save()
        return redirect('tour_list')
    return render(request, 'tour_form.html', {'form': form})

def tourist_delete_view(request, pk):
    tourist = get_object_or_404(Tourist, pk=pk)
    if request.method == "POST":
        tourist.delete()
        return redirect('tour_list')
    return render(request, 'tour_confirm_delete.html', {'tourist': tourist})