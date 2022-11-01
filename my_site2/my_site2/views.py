from os import stat, stat_result
from telnetlib import STATUS
from django.shortcuts import render

def view_404(request, exception):

    return render (request, 'error_view.html', status=404)