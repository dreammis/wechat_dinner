# coding=utf-8
from django.http import HttpResponse
import json


class JsonUtil(object):

    @staticmethod
    def obj2json(obj):
        result = None
        try:
            result = json.dumps(obj.__dict__, encoding='UTF-8', ensure_ascii=False)
        except Exception as e:
            print e
        finally:
            return result