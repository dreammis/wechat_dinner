# -*- coding:utf-8 -*-
from  django.contrib import admin
from res.models import Food, Order


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'active')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('openId', 'orders', 'date_time', 'total', 'accounted')
    date_hierarchy = 'date_time'
    def orders(self, obj):
        ret = []
        for v in obj.order_list.split('_'):
            tmp = v.split('*')
            ret.append(Food.objects.get(id=int(tmp[0])).name + "*" + tmp[1])
        return "  ".join(ret)
    orders.short_description = u'订单详情'


class OrderFoodAdmin(admin.ModelAdmin):
    list_display = ('food', 'num')

admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)