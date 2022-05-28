from .models import Trailer, News

def get_trailers(request):
    trailers = Trailer.objects.all()
    return {'trailers':trailers[:7]}

def get_news(request):
    news = News.objects.all()
    return {'news_list':news[:2]}