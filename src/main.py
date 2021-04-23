from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from login.douBanLogin import douBanLogin
from Topic.findTopic import findTopic

from Topic.submitTopic import submitTopic
####---------------INIT----------------####
options =  Options()
options.add_argument("--incognito")
# options.add_argument('--headless')
wd = webdriver.Chrome(r'D:\chromedriver.exe',options=options )
wd.implicitly_wait(12)
###########################################

####----------获取验证码登录-----------####
# D_login = douBanLogin(wd,"https://accounts.douban.com/passport/login?source=music")
# D_login.mode_One_GetNumCodeLogin('17895965885')
###########################################

####----------使用密码登录-----------####
# D_login = douBanLogin(wd,"https://accounts.douban.com/passport/login?source=music")
# D_login.mode_Tow_PasswordLogin('17895965885','shy15544')
#
# ###########################################
####----------使用cookie登录-----------####
D_login = douBanLogin(wd,"https://www.douban.com")
D_login.mode_Three_CookieLogin('15159669885')

###########################################

####------进入发布话题富文本框发布话题------####

submitTopicArticle = submitTopic(wd, 'https://www.douban.com/group/716676/')
submitTopicArticle.run()

###########################################
# 221231400
# 221400000
####--------------加入小组--------------####
# nowId = "221235230"
# findTopic = findTopic(wd)
# findTopic.isRandNextId(True)
# findTopic.run(nowId,20)





###########################################



####----------运行完成，收尾工作-----------####
wd.switch_to.default_content()
sleep(60)
# wd.quit()
############################################




