from .models import Film
def get_films(request):
    films = Film.objects.all()
    return {"films":films[:13]}