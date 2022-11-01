from django.http.response import HttpResponse
from django.shortcuts import render
import calendar

def home_view(request):
    return render(request, 'my_site/some_page.html')