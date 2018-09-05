from django.shortcuts import render,HttpResponse,render_to_response,redirect
import datetime
# Create your views here.


def index(requst):

    print(requst.path)
    print(requst.GET)

    if requst.method == "POST":

        user = requst.POST.get("user")
        pwd = requst.POST.get("pwd")

        if user == "aaa" and pwd == "111":
            return  HttpResponse("登录成功")

    # 渲染
    # return render(requst, "login.html")
    # return  render(requst,"new.html")

    alex = "you are  welcome"
    xialv = "XXXX"
    # return  render_to_response("new.html",{"name":alex,"name1":xialv}) #render_to_response
    # return render_to_response("new.html",locals())  #本地变量
    # return redirect("http://wwww.baidu.com")    #重定向


# def login(requst):
#
#     if requst.method == "POST":
#         if 1:
#             return render(requst,"new.html")
#         return redirect("/mysite/login")
#
#     return render(requst,"login.html")

def cur_time(requst):

    time = datetime.datetime.now()

    # date = '.........%s......'%time


    # return HttpResponse(date)
    return render(requst,"cur_time.html",{"abc":time})