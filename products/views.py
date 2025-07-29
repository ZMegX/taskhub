from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour, Request
from .forms import RequestForm

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'templates/tour_list.html', {'tours': tours})

def make_request(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.tour = tour
            new_request.save()
            return redirect('tour_list')
    else:
        form = RequestForm()
    return render(request, 'products/make_request.html', {'form': form, 'tour': tour})