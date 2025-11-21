from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    cond = now.month == 12 and (now.day >=1 and now.day <= 31)
    res = "Yes" if cond else "No"
    return render(request, "newyear/index.html",{
        "res": res
    })