from django.shortcuts import render, get_object_or_404, redirect
from .models import Tourist
from .forms import TouristForm

def tour_list_view(request):
    tourists = Tourist.objects.all()
    search_query = request.GET.get('search_tour')
    if search_query:
        tours = tours.filter(title__icontains=search_query)
        
    paginator = Paginator(tours, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'tours/tour_list.html', {
        'page_obj': page_obj, 
        'search_query': search_query
    })
    

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