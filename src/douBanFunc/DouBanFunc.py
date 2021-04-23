def hasEmement(wd,element):
    # 判断元素节点是否存在
    wd.implicitly_wait(1)
    try:
        print("查找 ",element," 元素节点")
        elementDom = wd.find_element_by_xpath(element)
        print("元素节点存在！")
        return True
    except:
        print("元素节点不存在！")
        return False
    finally:
        wd.implicitly_wait(12)
def checkIsLogin(wd):
    # 作用是检查豆瓣账号是否登录，账号已经登录返回True,未登录返回False,login分别是是账号和密码
    if  hasEmement(wd, '//*[@class="nav-login"]') and  wd.find_element_by_xpath('//*[@class="nav-login"]').text=='登录/注册':
        print('检测到未登录!')
        return False
    else:
        return True

def resetCookie(wd,cookie_Str=None):        #把webdriver获取的原生列表，本质是字符串还原到浏览器的cookie储存中
    if  cookie_Str!=None:
        cookies = eval(str(cookie_Str))
        print("放进浏览器前的cookie",cookies)
        wd.delete_all_cookies()
        for i in cookies:
            wd.add_cookie(i)
        print("添加cookie到浏览器成功！")
        return True
    return False

def globalWatchErr(wd):
    try:
        if hasEmement(wd, '//*[contains(@class,"abnormal")]'):
            print('检测到已经被豆瓣反爬虫盯上！')
        if hasEmement(wd, '//*[@class="account-body"]'):
            print('账号异常')
            # 这些异常后登录
    except:
        pass