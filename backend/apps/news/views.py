from django.shortcuts import redirect, render
from backend.apps.accounts.models import User
from .models import News, Comment
from django.views.generic import DetailView, ListView, View
from django.http import Http404
from .forms import NewsCommentForm
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
# Create your views here.

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = "news"

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    paginate_by = 1
    context_object_name = "news_list"

@csrf_exempt
def get_news_detail(request, pk):
    try:
        news = News.objects.get(id=pk)
        comments = Comment.objects.filter(news=news)
    except News.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = NewsCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.news = news
            user = User.objects.filter(id=request.user.id)
            value = int(request.user.experience)+1
            user.update(experience=str(value))
            instance.save()
        return redirect('news_detail', pk=news.id)
    else:
        form = NewsCommentForm()
    context = {
            'news':news,
            'comments':comments,
            'form':form
        }
    return render(request, 'news_detail.html', context)





class SearchNewsView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    paginate_by = 1


    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.all()
        q = self.model.objects.filter(
            Q(title__icontains=search_text)


        )
        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')
        return context