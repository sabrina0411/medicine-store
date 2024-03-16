from django.shortcuts import render


def home(request):
    context = {
        'name': 'Sabrina Islam'
    }
    return render(request, 'index.html', context)
