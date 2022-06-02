from django.shortcuts import redirect, render
from .models import News, Comment
from django.views.generic import DetailView, ListView, View
from django.http import Http404
from .forms import NewsCommentForm
from django.views.decorators.csrf import csrf_exempt
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
            instance.save()
        return redirect('news_detail', pk = news.id)
    else:
        form = NewsCommentForm()
    context = {
            'news':news,
            'comments':comments,
            'form':form
        }
    return render(request, 'news_detail.html', context)
