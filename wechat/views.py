# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from wechatUtil import checkSignature
from wechatService import WechatService


class WechatInterfaceView(View):
    def get(self, request):
        echostr = request.GET.get(u'echostr', None)
        if checkSignature(request):
            return HttpResponse(echostr)

    def post(self, request):
        return HttpResponse(WechatService.processRequest(request))