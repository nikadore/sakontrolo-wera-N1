from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def films(request):
    movies = [
        {'title': 'king-kong', 'rating': 7.0},
        {'title': 'hatefull eight', 'rating': 10.0},
        {'title': 'dark knight', 'rating': 9.9},
    ]
    return render(request, 'films.html', {'movies': movies})
