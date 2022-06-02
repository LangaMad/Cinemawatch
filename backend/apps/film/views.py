from .forms import FilmCommentForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import Film, Celebrity, Comment
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

# Create your views here.

class IndexPage(TemplateView):
    template_name = "index.html"



@csrf_exempt
def get_film_detail(request, pk):
    try:
        film = Film.objects.get(id=pk)
        comments = Comment.objects.filter(film=film)
    except Film.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = FilmCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.film = film
            instance.save()
        return redirect('film_single', pk=film.id)
    else:
        form = FilmCommentForm()
    context = {
            'film':film,
            'comments':comments,
            'form':form
        }
    return render(request, 'film_single.html', context)



class CelebrityListView(ListView):
    model = Celebrity
    paginate_by = 1
    template_name = 'celebrity_list.html'
    context_object_name = "celebrities"

class CelebrityDetailView(DetailView):
    model = Celebrity
    template_name = 'celebrity_detail.html'
    context_object_name = "celebrity"

class FilmListView(ListView):
    model = Film
    paginate_by = 2
    template_name = 'film_list.html'
    context_object_name = "films"