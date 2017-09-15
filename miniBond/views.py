from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from miniBond.models import *


def hello(request):
	message = 'hello'
	return HttpResponse("Hello world")

def myname(request):
	name = "wqfaa"
	return render(request,'miniBond/sample.html', locals())

def index(request):
	pfs=Platform.objects.all()
	contextDict={'pfs':pfs}
	return render(request,'miniBond/index.html',contextDict)