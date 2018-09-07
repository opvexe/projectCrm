from django.shortcuts import render,HttpResponse

# Create your views here.

def index(requst):

    return render(requst,'index.html')




def ajax_recieve(requst):


    if requst.method == 'POST':
        print('POST Request')

    return HttpResponse('hello')