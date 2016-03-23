#coding:utf-8
from django.utils import simplejson
import json
'''
Result 工具类
'''
class Result(object):
    def __init__(self):
        self.data = u''
        self.result = u''

    def __init__(self, result, data):
        self.data = data
        self.result = result

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getResult(self):
        return self.result

    def setResult(self, result):
        self.result = result

    @staticmethod
    def objectNotFound():
        return Result('error', '未找到该对象')
    @staticmethod
    def success():
        return Result('success', '操作成功')

    @staticmethod
    def validataCodeError():
        return Result('error', '您输入的验证码错误')

    @staticmethod
    def passwordError():
        return Result('error', '你输入的密码错误')

    @staticmethod
    def unknowError():
        return Result('error', '未知错误，请联系管理员')