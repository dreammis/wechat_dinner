# -*- coding:utf-8 -*-
import codecs
from lxml import etree

f = codecs.open(u'post.xml', u'r', u'utf-8')
content = u''.join(f.readlines())
f.close()

xmlstr = etree.fromstring(content.decode(u'UTF-8'))
dict_xml = {}
for child in xmlstr:
    #print child.tag, ':', child.text
    dict_tmp = {}
    for node in child.getchildren():
        #print '\t', node.tag, ':', node.text
        dict_tmp[node.tag] = node.text
    if any(dict_tmp):
        dict_xml[child.tag] = dict_tmp
    else:
        dict_xml[child.tag] = child.text

print dict_xml
