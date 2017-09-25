from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from miniBond.models import *
from django.template.loader import render_to_string
import os


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

	templateName="index.html"
	staticView(contextDict, templateName,templateName)
	return render(request, "static/"+templateName)


def staticView(contextDict, templateName,staticFileName):
	static_html = 'templates/static/' + staticFileName
	if not os.path.exists(static_html):
		content = render_to_string('miniBond/' + templateName, contextDict)
		with open(static_html, 'w', encoding="utf-8") as static_file:
			static_file.write(content)

def toWx(request,uuid):
	toWxItem=LinkToWx.objects.filter(platForm__id=uuid).first()
	contextDict={'wxText':toWxItem.wxText,'imgName':toWxItem.platForm.name}

	templateName = "linkToWx.html"
	staticFileName=toWxItem.platForm.name+".html"
	staticView(contextDict, templateName,staticFileName)
	return render(request, "static/" + staticFileName)
