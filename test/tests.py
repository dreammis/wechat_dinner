# -*- coding:utf-8 -*-
import requests
import codecs

f = codecs.open(u'post.xml', u'r', u'utf-8')
content = u''.join(f.readlines())
f.close()

posturl = u'http://localhost:8000/wechat/'
#posturl = u'http://localhost:8000/res/'
res = requests.post(posturl, data=content.encode(u'utf-8'))
print res.text
