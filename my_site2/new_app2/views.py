from locale import currency
from multiprocessing import context
from django.shortcuts import render
from .libraries.prsn_exemple import get_person
from .libraries.GetDate import getDate

def simple_view(request):
    curr = {"date":getDate()}
    return render(request, 'new_app2/example.html', context=curr)

def variable_view(request):
    my_var = 34
    asset = get_person()
    asset["date"] = getDate()
    #asset = {'hello':my_var}
    #asset ={"price_before":"299$", "price_after":"399$"}
    return render(request, 'new_app2/variable.html', context = asset)
