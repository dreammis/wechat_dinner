#coding=utf-8
str = ('3*4_4*3')
print str
for n in str.split('_'):
    print type(int(n.split('*')[0]))