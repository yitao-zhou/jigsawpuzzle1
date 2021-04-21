from django.shortcuts import render


def puzzle(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'puzzle.html', context)
