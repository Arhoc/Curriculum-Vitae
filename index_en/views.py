from django.shortcuts import render

# Create your views here.
def index_en(request):
    return render(request, 'index_en.html', {})