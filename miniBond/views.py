from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from miniBond.models import *


def hello(request):
	message = 'hello'
	return HttpResponse("Hello world")

def myname(request,offset):
	name = "wqfaa"
	return render(request,'miniBond/sample.html', locals())

def index(request):
	allpfs=Platform.objects.filter(isValid=True)
	pfs=[p for p in allpfs if p.promotioninfo_set.filter(isValid=True).count()>0 or (hasattr(p,'linktowx') and p.linktowx.isValid)]
	contextDict={'pfs':pfs}
	return render(request,'miniBond/index.html',contextDict)

def toWx(request,uuid):
	toWxItem=LinkToWx.objects.filter(platForm__id=uuid).first()
	contextDict={'wxText':toWxItem.wxText,'imgName':toWxItem.platForm.name}
	return render(request,'miniBond/linkToWx.html',contextDict)