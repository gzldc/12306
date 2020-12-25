# -*- coding=utf-8 -*-
import copy
import sys
import time
from collections import OrderedDict
from time import sleep
import TickerConfig
from inter.GetPassCodeNewOrderAndLogin import getPassCodeNewOrderAndLogin1
from inter.GetRandCode import getRandCode
from inter.LoginAysnSuggest import loginAysnSuggest
from inter.LoginConf import loginConf
from myException.UserPasswordException import UserPasswordException


class GoLogin:
    def __init__(self, session, is_auto_code, auto_code_type):
        self.session = session
        self.randCode = ""
        self.is_auto_code = is_auto_code
        self.auto_code_type = auto_code_type

    def auth(self):
        """
        :return:
        """
        self.session.httpClint.send(self.session.urls["loginInitCdn1"])
        uamtkStaticUrl = self.session.urls["auth"]
        uamtkStaticData = {"appid": "otn"}
        return self.session.httpClint.send(uamtkStaticUrl, uamtkStaticData)

    def codeCheck(self):
        """
        验证码校验
        :return:
        """
        codeCheckUrl = copy.deepcopy(self.session.urls["codeCheck1"])
        codeCheckUrl["req_url"] = codeCheckUrl["req_url"].format(self.randCode, int(time.time() * 1000))
        fresult = self.session.httpClint.send(codeCheckUrl)
        if not isinstance(fresult, str):
            print("登录失败")
            return
        fresult = eval(fresult.split("(")[1].split(")")[0])
        if "result_code" in fresult and fresult["result_code"] == "4":
            print(u"验证码通过,开始登录..")
            return True
        else:
            if "result_message" in fresult:
                print(fresult["result_message"])
            sleep(1)
            self.session.httpClint.del_cookies()

    def baseLogin(self, user, passwd):
        """
        登录过程
        :param user:
        :param passwd:
        :return: 权限校验码
        """

        if 0 == 0:
            tk = TickerConfig.tk
            if 0 == 0:
                return tk
            else:
                return False
        elif 'result_message' in tresult and tresult['result_message']:
            messages = tresult['result_message']
            if messages.find(u"密码输入错误") is not -1:
                raise UserPasswordException("{0}".format(messages))
            else:
                print(u"登录失败: {0}".format(messages))
                print(u"尝试重新登陆")
                return False
        else:
            return False

    def getUserName(self, uamtk):
        """
        登录成功后,显示用户名
        :return:
        """
        if not uamtk:
            return u"权限校验码不能为空"
        else:
            uamauthclientUrl = self.session.urls["uamauthclient"]
            data = {"tk": uamtk}
            uamauthclientResult = self.session.httpClint.send(uamauthclientUrl, data)
            if uamauthclientResult:
                if "result_code" in uamauthclientResult and uamauthclientResult["result_code"] == 0:
                    print(u"欢迎 {} 登录".format(uamauthclientResult["username"]))
                    return True
                if "result_code" in uamauthclientResult and uamauthclientResult["result_code"] == 2:
                    print("tk失效 请更新")
                    sys.exit()
            else:
                self.session.httpClint.send(uamauthclientUrl, data)
                url = self.session.urls["getUserInfo"]
                self.session.httpClint.send(url)

    def go_login(self):
        """
        登陆
        :param user: 账户名
        :param passwd: 密码
        :return:
        """
        user, passwd = TickerConfig.USER, TickerConfig.PWD
        if not user or not passwd:
            raise UserPasswordException(u"温馨提示: 用户名或者密码为空，请仔细检查")
        login_num = 0
        while True:
            uamtk = self.baseLogin(user, passwd)
            if uamtk:
                self.getUserName(uamtk)
                break
            else:
                loginAysnSuggest(self.session, username=user, password=passwd)
                login_num += 1
                break

