from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = "accounts/home2.html"
    args = {}
    return render(request,template_name,args)