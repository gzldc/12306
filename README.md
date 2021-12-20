###ps：又要过年了
   我看最近12306登陆方式改成短信验证了，加上又要过年了，最近会抽空更新一版。【2021.12.20】

#### 写在前面：
 
​	视频教程：https://www.bilibili.com/video/BV1mK4y1V7cd

​	项目原地址：https://github.com/testerSunshine/12306   

​	因作为没有维护，本人进行二次开发，现在可以用【2020-12-24】。有问题可以关注公众号:罐子里的茶，会有群二维码回复，有问题必定解答！最后祝大家都抢到过年的票。

![qrcode_for_gh_0626c7a906e9_258](https://gitee.com/gzldc/images/raw/master/2020-12-04/qrcode_for_gh_0626c7a906e9_258.jpg)

公众号二维码:https://gitee.com/gzldc/images/raw/master/2020-12-04/qrcode_for_gh_0626c7a906e9_258.jpg




   - 

启动命令：
   1.安装依赖包:  pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
   2.加入cdn:    python3 run.py c
   3.启动脚本:    python3 run.py r  

## IP 代理池
推荐一个ip代理池的项目：https://github.com/Python3WebSpider/ProxyPool
简单使用方法：`docker-compose up`

## 本地云打码平台搭建（基于docker)
在安装好docker环境下，运行如下命令：
```angular2html
docker run -d -p 8080:80 --name 12306 yinaoxiong/12306_code_server
```

## (可选)配置 sre24 免费推送消息到 微信/短信/邮箱 提醒

推送 token 值通过微信免费扫码登录 https://sre24.com 「设置」页面获取，修改根目录配置文件 TickerConfig.py

    SRE24_TOKEN = "xxx"

保存后重启生效。

备注：sre24 推送支持免费一对多推送消息到 微信/短信/邮箱 提醒，可以设置一个 SRE24_TOKEN 代替分别设置 EMAIL_CONF 和 SERVER_CHAN_CONF 。
