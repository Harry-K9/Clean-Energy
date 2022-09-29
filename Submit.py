from sys import exc_info
from django_shortcuts import render
import requests

from subprocess import run,PIPE
def button(request):

    return render(request,"index.html")

def output(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data = data.text
    return render(request,"index.html",{"data":data})

def external(request):
    inp= request.POST.get("Murigi")
    out = run([sys.executable,"//mnt//e//work//django_testing//test.py",inp],shell=False,stout=PIPE)

    return render(request,"index.html",{"data1":out})