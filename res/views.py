# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from models import Food, Order
from django.views.decorators.csrf import csrf_exempt
from vo import Result
from utils import JsonUtil
from django.core.exceptions import ObjectDoesNotExist
import json
import datetime


def index(request):
    c = Context({"foods": Food.objects.filter(active=True)})
    return render(request, "shop.html", c)


@csrf_exempt
def food_list(request):
    callback = request.GET.get(u'callback', None)
    response_list = []
    for n in Food.objects.filter(active=True):
        tmp = {}
        tmp['id'] = n.id
        tmp['name'] = n.name
        tmp['price'] = n.price
        response_list.append(tmp)
    result = json.dumps(response_list, encoding='UTF-8', ensure_ascii=False)
    return HttpResponse(callback + "(" + result + ")");


def buy(request, **kw):
    ret_str = u""
    if kw['order'] is None or kw['openId'] is None:
        mOrder = request.GET.get(u'order', None)
        mOpenId = request.GET.get(u'openId', None)
    else:
        mOrder = kw['order']
        mOpenId = kw['openId']
    print mOpenId, " ", mOrder
    if (mOrder == '' or mOrder is None or mOpenId == '' or mOpenId is None):
        result = JsonUtil.obj2json(Result('error', '非法订单'))
        return HttpResponse(result, mimetype="text/html")
    mTotal = getTotal(mOrder)
    if mTotal == -1:
        result = Result('error', '非法订单！请重新购买.')
        ret_str += unicode(result.getData(), 'utf-8')
    else:
        o = Order(openId=mOpenId, order_list=mOrder, total=mTotal)
        o.save()
        result = Result('success', '点餐成功')
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        ret_str += unicode(result.getData(), 'utf-8') + u',购买时间:' + now + u'  谢谢您的惠顾:-)'
    if request is None:
        return ret_str
    else:
        return HttpResponse(result, mimetype="text/html")


def getTotal(str):
    total = 0
    try:
        for n in str.split('_'):
            m = n.split('*')
            mFood = Food.objects.get(id=m[0])
            total += mFood.price * int(m[1])
    except:
        total = -1
    return total

