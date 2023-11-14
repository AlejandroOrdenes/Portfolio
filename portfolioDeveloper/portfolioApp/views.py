from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
def index(request):
    p =  _("I'm a")
    return render(request, 'index.html', {'text' : p})

def textTraductions(request):
    return render()