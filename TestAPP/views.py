from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    context = {'hello, lvkefan!'}
    return render(request, 'login.html',context)

def book_details(request):
    string = '书名'
    web_list = ["哈利波特与魔法石", "哈利波特与死亡圣器", "哈利波特与阿兹卡班的囚徒"]
    return render(request, 'detial.html', {'book_detail': string, 'ref': web_list})

def book_list(request):
    value = 5
    return render(request, 'list.html', {'value': value})

