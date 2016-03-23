### 微信点餐系统——Python/Django实践

------
#### 简介
环境：py 2.7，django 1.4，前端用到的开源项目[HTML5 UI design based on Google Material](https://github.com/Daemonite/material)。
项目部署在sae（须进行实名认证，否则返回会带一段js的，影响到和微信服务器的交互）。
通过django接入微信进行二次开发，页面中选餐后，生成都买二维码，扫一扫即可完成购买。
项目演示地址：http://wres.sinaapp.com/res/
#### 参考资料
[The Django Book 2.0--中文版](http://docs.30c.org/djangobook2/)
[django+sae微信开发－简单的鹦鹉学舌功能](http://ningning.today/2015/02/09/python/django-sae%E5%BE%AE%E4%BF%A1%E5%BC%80%E5%8F%91%EF%BC%8D%E7%AE%80%E5%8D%95%E7%9A%84%E9%B9%A6%E9%B9%89%E5%AD%A6%E8%88%8C%E5%8A%9F%E8%83%BD/)

------

#### 部署注意事项
1. 代码通过svn上传到sae，并建立好sae上的MySQL服务，而数据库表是在本地上通过工具转储 SQL，sae官方提供了PHPMyAdmin管理数据库的，直接在那里导入就好。我不知道，在sae这种情况下如何运行manage.py.
2. 微信接入的url是 http://host/wechat/, 以我的为例 http://wres.sinaapp.com/wechat/ 。Token为weixincourse，可以在setting.py中修改，如果是用自己的vps的话，切记微信接入暂时只是支持80端口的。
3. 扫一扫功能需要通过微信的工具菜单栏进行，所以无论是测试号还是订号都须要生成菜单栏才行。本项目使用到了 微信的扫一扫等待功能（scancode_waitmsg），自由通过这种形式的扫码才能进行购买。
4. 后台默认用户名：admin，密码：123456

------

#### 项目结构介绍
1. 项目分为两个app，一个是接入微信的wechat，一个是点餐信息管理系统res。
2. wechat部分主要完成了对微信事件和信息的封装，还有一些对微信xml包解析的工具类，还接入了图灵自动聊天机器人。
3. res部分主要是建立实体食品（Food）订单（Order），还有购买罗辑。
4. 测试包，自己写的测试，模拟微信发送xml请求。
5. 配置好静态资源路径和模板路径。
6. 前台指示实现了简单的购物车功能和二维码生成。

------

Mail: mrsimpletjx@gmail.com
人生苦短，码不停蹄 :-)
