from .forms import FilmCommentForm, RatingForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import Film, Celebrity, Comment, Rating
from backend.apps.accounts.models import User, Rank
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse

# Create your views here.
from django.db.models import Q
from django_filters.views import FilterView
from .filters import FilmFilter, CelebrityFilter

from django.contrib.auth.decorators import login_required


@login_required
def update_rank(request):
    rank_1 = Rank.objects.get(name='Новичок')
    rank_2 = Rank.objects.get(name='Любитель')
    rank_3 = Rank.objects.get(name='Знаток')
    rank_4 = Rank.objects.get(name='Гуру')
    rank_5 = Rank.objects.get(name='Киноман')

    user = User.objects.filter(id=request.user.id)

    if request.user.experience < 5:
        user.update(rank=rank_1)
    elif request.user.experience < 20:
        user.update(rank=rank_2)
    elif request.user.experience < 50:
        user.update(rank=rank_3)
    elif request.user.experience < 300:
        user.update(rank=rank_4)
    else:
        user.update(rank=rank_5)



class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_rank(self.request)
        return context



@csrf_exempt
def get_film_detail(request, pk):
    try:
        film = Film.objects.get(id=pk)
        comments = Comment.objects.filter(film=film)
        update_rank(request)
    except Film.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = FilmCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.film = film
            instance.save()
            user = User.objects.filter(id=request.user.id)
            value = int(request.user.experience)+1
            user.update(experience=str(value))
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



class CelebrityListView(FilterView):
    model = Celebrity
    paginate_by = 1
    template_name = 'celebrity_list.html'
    context_object_name = "celebrities"
    filterset_class = CelebrityFilter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CelebrityFilter(self.request.GET, queryset=self.get_queryset())
        update_rank(self.request)
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
        update_rank(self.request)
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
        update_rank(self.request)

        return context


class SearchCelebrityView(ListView):
    model = Celebrity
    template_name = 'celebrity_list.html'
    context_object_name = "celebrities"


    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.all()
        q = self.model.objects.filter(
            Q(full_name__icontains=search_text)
        )
        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')
        update_rank(self.request)
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

