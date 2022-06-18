from .forms import FilmCommentForm, RatingForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import Film, Celebrity, Comment, Rating
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse

# Create your views here.
from django.db.models import Q
from django_filters.views import FilterView
from .filters import FilmFilter , CelebrityFilter

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

    try:
        user_rating = Rating.objects.get(user=request.user, film=film)
    except:
        user_rating = None

    context = {
            'film':film,
            'comments':comments,
            'user_rating':user_rating,
            'form':form,
            'star_form':RatingForm()
        }
    return render(request, 'film_single.html', context)



class CelebrityListView(ListView):
    model = Celebrity
    paginate_by = 1
    template_name = 'celebrity_list.html'
    context_object_name = "celebrities"
    filterset_class = CelebrityFilter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CelebrityFilter(self.request.GET, queryset=self.get_queryset())
        return context

class CelebrityDetailView(DetailView):
    model = Celebrity
    template_name = 'celebrity_detail.html'
    context_object_name = "celebrity"

class FilmListView(FilterView):
    model = Film
    paginate_by = 2
    template_name = 'film_list.html'
    context_object_name = "films"
    filterset_class = FilmFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FilmFilter(self.request.GET, queryset=self.get_queryset())
        return context

class AddStarRating(View):

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                user=request.user,
                film_id=int(request.POST.get('film')),
                defaults={"stars_id":int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class SearchFilmView(ListView):
    model = Film
    template_name = 'film_list.html'
    paginate_by = 10


    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.filter(is_active=True)
        q = self.model.objects.filter(
            Q(name__icontains=search_text)
            |Q(description__icontains = search_text)

        )
        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')
        return context


class SearchCelebrityView(ListView):
    model = Celebrity
    template_name = 'celebrity_list.html'
    paginate_by = 10


    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.all()
        q = self.model.objects.filter(
            Q(name__icontains=search_text)
            |Q(description__icontains = search_text)

        )
        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')
        return context

# class FilmListFilterView(FilterView):
#     model = Film
#     template_name = 'film_list.html'
#     filterset_class = FilmFilter
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = FilmFilter(self.request.GET, queryset=self.get_queryset())
#         return context




# class CelebrityListFilterView(FilterView):
#     model = Celebrity
#     template_name = 'celebrity_list.html'
#     filterset_class = CelebrityFilter
#     paginate_by = 4
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = CelebrityFilter(self.request.GET, queryset=self.get_queryset())
#         return context

