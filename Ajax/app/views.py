from django.shortcuts import render,HttpResponse

# Create your views here.

def index(requst):

    return render(requst,'index.html')




def ajax_recieve(requst):


    if requst.method == 'POST':
        print('POST Request')

    return HttpResponse('hello')



def ajax_register(requst):

    if requst.method == 'POST':
        username = requst.POST.get('username')

        if username == 'alex':

            return HttpResponse('ajax_register 200 ok')

        return HttpResponse('ajax_register error')

    return render(requst,'register.html')