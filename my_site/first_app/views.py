from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
import datetime
from django.urls import reverse

# Create your views here.
articles = {
    'phones' : 'info about newest phones, tests, etc',
    "laptops":"latest info concerning laptops",
    "consoles":"console\'s vis-a-vis between best market offers",
    "earphones":"all about earphones",
    "sound bars":"ready to get loud? Today is a best chance for it",
    "pc":"make up your pc set-up right here"
}

def device_view(request, topic):
    try:
        if(topic == "datetime"):
            return render(request, 'first_app/exmpl.html')
            #return HttpResponse(current_datetime(topic))
             #load html                        
        else:
            result = articles[topic]
            return HttpResponse(result)
    except:
        return HttpResponseNotFound("PAGE NOT FOUND. SORRY....")
        #raise Http404("404 PAGE NOT FOUND") # 404.html

def add_view(request, num1, num2):
    #domain.com/first_app/num1/num2 --> num1+num2
    result = num1 + num2
    return HttpResponse(str(result))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><h1>It is now %s.</h1></html>" % now
    return HttpResponse(html)

def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    if ((topics_list.__len__()) > num_page):
        topic = topics_list[num_page]
        return HttpResponseRedirect(reverse("topic-page", args=[topic]))
    else:
        return HttpResponseNotFound("REQUESTED PAGE DOESN\'T EXIST")
    