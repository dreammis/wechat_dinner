# -*- coding:utf-8 -*-
from django.db import models

# 食品实体
'''
id，名字， 单价， 货物状态
'''


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True, verbose_name='食品名称')
    price = models.FloatField(verbose_name='单价/元')
    active = models.BooleanField(default=True, verbose_name='货物状态')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"食品"
        ordering = ['name']

# 订单实体
'''
id，openId， 购买清单，购买时间，核销状态
'''

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    openId = models.CharField(max_length=60, verbose_name='微信用户', blank=False)
    order_list = models.CharField(max_length=1000, verbose_name='订单信息', blank=False)
    total = models.FloatField(blank=True, verbose_name='合计')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='订单时间')
    accounted = models.BooleanField(default=False, verbose_name='核销状态')

    class Meta:
        verbose_name_plural = u"订单信息"
        ordering = ['-date_time']
