from django.shortcuts import render

from .models import Film


# SELECT * FROM Film
def film_list(request):
    
    films = Film.objects.all()
    
    return render(request, 'app/index.html', context = {'films': films})
