from django.shortcuts import HttpResponse
from django.shortcuts import render
from polls.models import user, cargo, Depot1, Depot2, Depot3


# Create your views here.
# 设置页面函数

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    username = request.POST.get("user")
    user_pwd = user.objects.filter(name=username).first()
    passwd = int(request.POST.get("pwd"))
    if username and passwd == user_pwd.pwd:
        return render(request, 'index.html')

    return render(request, "login.html", {"error_meg": "用户名或密码错误"})


def tpl(request):
    # user.objects.create(id="3", name="f1b", pwd="123")
    # return HttpResponse("ok")
    if request.method == "GET":
        return render(request, 'tpl.html')
    iname = request.POST.get("iname")
    cname = request.POST.get("cname")
    number = request.POST.get("number")
    site = request.POST.get("site")
    if int(site) == 1:
        Depot1.objects.create(iname=int(iname), cname=cname, number=int(number))
    if int(site) == 2:
        Depot2.objects.create(cname=cname, number=int(number))
    if int(site) == 3:
        Depot3.objects.create(iname=int(iname), cname=cname, number=int(number))
    return HttpResponse("oK")


def empty(request):
    return render(request, 'empty.html')


def form(request):
    return render(request, 'form.html')


def morris(request):
    return render(request, 'morris.html')


def table(request):
    return render(request, 'table.html')


def tabpanel(request):
    return render(request, 'tabpanel.html')


