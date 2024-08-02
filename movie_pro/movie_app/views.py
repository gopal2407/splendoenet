from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


# Create your views here.
def review_form(request):
    template_name = 'movie_app/form.html'
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_url')
    context = {'form': form}
    return render(request, template_name, context)


def review_data(request):
    template_name = 'movie_app/data.html'
    objs = Review.objects.all()
    context = {'objs': objs}
    return render(request, template_name, context)


def review_update(request, pk):
    template_name = 'movie_app/form.html'
    obj = Review.objects.get(pk=pk)
    form = ReviewForm(instance=obj)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('data_url')
    context = {'form': form}
    return render(request, template_name, context)


def review_delete(request, pk):
    template_name = 'movie_app/delete.html'
    obj = Review.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('data_url')
    context = {'obj': obj}
    return render(request, template_name, context)


# movie title  or director
def search_tile_director(request):
    template_name = 'movie_app/data.html'
    data = request.POST['data']
    objs = Review.objects.filter(title=data) | Review.objects.filter(director=data)
    context = {'objs': objs}
    return render(request, template_name, context)


# filter by status and genres
def filter_status(request):
    template_name = 'movie_app/data.html'
    data = request.POST['data']
    objs = Review.objects.filter(status=data)
    context = {'objs': objs}
    return render(request, template_name, context)


def filter_genres(request):
    template_name = 'movie_app/data.html'
    data = request.POST['data']
    objs = Review.objects.filter(genres=data)
    context = {'objs': objs}
    return render(request, template_name, context)
