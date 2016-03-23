# -*- coding:utf-8 -*-
import json
import time
import urllib
import urllib2
import datetime

from wechatUtil import MessageUtil
from wechatReply import TextReply

from res.views import buy

class RobotService(object):
    """Auto reply robot service"""
    KEY = 'd92d20bc1d8bb3cff585bf746603b2a9'
    url = 'http://www.tuling123.com/openapi/api'

    @staticmethod
    def auto_reply(req_info):
        query = {'key': RobotService.KEY, 'info': req_info.encode('utf-8')}
        headers = {'Content-type': 'text/html', 'charset': 'utf-8'}
        data = urllib.urlencode(query)
        req = urllib2.Request(RobotService.url, data)
        f = urllib2.urlopen(req).read()
        return json.loads(f).get('text').replace('<br>', '\n')


class WechatService(object):
    @staticmethod
    def processRequest(request):
        requestMap = MessageUtil.parseXml(request)
        fromUserName = requestMap.get(u'FromUserName')
        toUserName = requestMap.get(u'ToUserName')
        createTime = requestMap.get(u'CreateTime')
        msgType = requestMap.get(u'MsgType')
        msgId = requestMap.get(u'MsgId')

        respContent = u'默认'

        textReply = TextReply()
        textReply.setToUserName(fromUserName)
        textReply.setFromUserName(toUserName)
        textReply.setCreateTime(time.time())
        textReply.setMsgType(MessageUtil.RESP_MESSAGE_TYPE_TEXT)

        if msgType == MessageUtil.REQ_MESSAGE_TYPE_TEXT:
            content = requestMap.get('Content')
            #respContent = u'您发送的是文本消息:' + content
            respContent = RobotService.auto_reply(content)
        elif msgType == MessageUtil.REQ_MESSAGE_TYPE_IMAGE:
            respContent = u'您发送的是图片消息！'
        elif msgType == MessageUtil.REQ_MESSAGE_TYPE_VOICE:
            respContent = u'您发送的是语音消息！'
        elif msgType == MessageUtil.REQ_MESSAGE_TYPE_VIDEO:
            respContent = u'您发送的是视频消息！'
        elif msgType == MessageUtil.REQ_MESSAGE_TYPE_LOCATION:
            respContent = u'您发送的是地理位置消息！'
        elif msgType == MessageUtil.REQ_MESSAGE_TYPE_LINK:
            respContent = u'您发送的是链接消息！'
        elif msgType == MessageUtil.REQ_MESSAGE_TYPE_EVENT:
            # 事件推送
            eventType = requestMap.get(u'Event')
            if eventType == MessageUtil.EVENT_TYPE_SUBSCRIBE:
                respContent = u'^_^谢谢您的关注,人生苦短，码不停蹄;-)'
            elif eventType == MessageUtil.EVENT_TYPE_UNSUBSCRIBE:
                pass
            elif eventType == MessageUtil.EVENT_TYPE_SCANCODE_WAITMSG:
                print "扫码带提示"
                mOrder = requestMap.get(u'ScanCodeInfo').get(u'ScanResult')
                mOpenId = requestMap.get(u'FromUserName')
                respstr =  buy(None, openId=mOpenId, order=mOrder)
                respContent = respstr#unicode(respstr,'utf-8')
            elif eventType == MessageUtil.EVENT_TYPE_SCANCODE_PUSH:
                print "扫码推事件"
                respContent = u'扫码推事件'
            elif eventType == MessageUtil.EVENT_TYPE_CLICK:
                respContent = u'菜单栏点击'

        textReply.setContent(respContent)
        respXml = MessageUtil.class2xml(textReply)

        return respXml

        """
        if msgType == 'text':
            content = requestMap.get('Content')
            # TODO

        elif msgType == 'image':
            picUrl = requestMap.get('PicUrl')
            # TODO

        elif msgType == 'voice':
            mediaId = requestMap.get('MediaId')
            format = requestMap.get('Format')
            # TODO

        elif msgType == 'video':
            mediaId = requestMap.get('MediaId')
            thumbMediaId = requestMap.get('ThumbMediaId')
            # TODO

        elif msgType == 'location':
            lat = requestMap.get('Location_X')
            lng = requestMap.get('Location_Y')
            label = requestMap.get('Label')
            scale = requestMap.get('Scale')
            # TODO

        elif msgType == 'link':
            title = requestMap.get('Title')
            description = requestMap.get('Description')
            url = requestMap.get('Url')
        """
