from django.shortcuts import render

def ranking_response(request):
    return render(request, 'ranking.html')
