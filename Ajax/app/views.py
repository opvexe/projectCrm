from django.shortcuts import render,HttpResponse

# Create your views here.

def index(requst):

    return render(requst,'index.html')




def ajax_recieve(requst):

    return HttpResponse('hello')