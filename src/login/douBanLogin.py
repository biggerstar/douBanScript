from time import sleep
from random import randint
from database.sql import douBanDB
from douBanFunc.DouBanFunc import resetCookie

class douBanLogin:
    def __init__(self,wd,url):
        self.wd = wd
        self.url = url
        self.phone=None
        self.passwd=None
        self.cookie=None
    def putToDB(self):
        douBanPutDb  =  douBanDB()
        self.cookie = self.wd.get_cookies()
        print(self.cookie)
        str(self.cookie)
        if self.cookie != None:
            resStatus=douBanPutDb.DB_insertARecordToDb(self.phone,self.passwd,self.cookie)
            if resStatus:
                print('插入数据成功！')
            else:
                print('插入数据失败！')

    def runSliderCode(self,offsetX=210,offsetY=0):
        from api.tencentHuaKuai import tencentHuaKuai
        self.tencentHuaKuai = tencentHuaKuai(self.wd)
        # self.tencentHuaKuai.run(randint(offsetX-5,offsetX+5),offsetY)
        self.tencentHuaKuai.run(offsetX,offsetY)

    def isRunSliderCode(self):
        # 判断验证码框是否存在
        try:
            self.element = self.wd.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
            print(self.element)
            print("验证码框存在！")
            return True
        except:
            print("检测验证码框不存在！")
            return False


    def mode_One_GetNumCodeLogin(self,phone):
        # 模式一获取验证码登录
        self.phone=phone
        self.wd.get(self.url)
        self.wd.find_element_by_xpath('//*[@name="phone"]').send_keys(self.phone)
        sleep(3)
        self.wd.find_element_by_xpath('//*[@class="account-form-field-code"]/a').click()
        if self.isRunSliderCode():  #判断是否需要滑块验证码
            self.runSliderCode(210,0)  # 执行过滑块验证码
        sleep(30)
        ## 这里缺少获取到手的验证码输入
        self.wd.find_element_by_xpath('//div[@class="account-form-field-submit "]/a').click()
        sleep(10)
        self.putToDB()
    def mode_Two_PasswordLogin(self,phone,password):
        # 模式二用户密码登录
        self.phone=phone
        self.passwd=password
        self.wd.get(self.url)
        self.wd.find_element_by_xpath('//li[@class="account-tab-account"]').click()
        self.wd.find_element_by_xpath('//*[@id="username"]').send_keys(self.phone)
        self.wd.find_element_by_xpath('//*[@id="password"]').send_keys(self.passwd)
        sleep(3)
        self.wd.find_element_by_xpath('//div[@class="account-form-field-submit "]/a').click()
        if self.isRunSliderCode():  #判断是否需要滑块验证码
            self.runSliderCode(210,0)  # 执行过滑块验证码
        sleep(10)
        self.putToDB()
    def mode_Three_CookieLogin(self,phone):
        #   不是登陆页。这里选任意douban.com域名下的网址都可
        self.wd.get(self.url)
        douBanDBObj =   douBanDB()
        findOneCookie = douBanDBObj.DB_findARecord(phone)
        resetCookie(self.wd,findOneCookie[2])
