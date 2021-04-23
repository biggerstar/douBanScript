from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
####---------------INIT----------------####
# options =  Options()
# # options.add_argument("--incognito")
# # options.add_argument('--headless')
# wd = webdriver.Chrome(r'D:\chromedriver.exe',options=options )
# wd.implicitly_wait(12)
#
from selenium.webdriver.common.keys import Keys

from douBanFunc.DouBanFunc import globalWatchErr


class submitTopic:
    def __init__(self,wd,url):
        self.wd=wd
        self.url=url

    def run(self):
        self.wd.get(self.url)
        globalWatchErr(self.wd)
        self.clickNewPost()

    def clickNewPost(self):
        try:
            sleep(3)
            self.wd.find_element_by_xpath('//*[@href="new_topic"]').click()
            sleep(3)
        except:
            print('找话题的发言按钮失败！')

        self.wd.find_element_by_xpath('//*[@class ="editor-title"]').click()
        sleep(3)
        self.wd.find_element_by_xpath('//*[@class ="editor-title"]//textarea').send_keys('没啥事就想发一条动态')
        sleep(3)
        self.wd.find_element_by_xpath('//*[@class="DRE-wrapper"]').click()
        sleep(3)
        # self.wd.find_element_by_xpath('//*[@class="DRE-wrapper"]//*[@data-text="true"]').send_keys(''
        #                    '没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一'
        #                      '条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态'
        #                      '没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态'
        #                      '没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态'
        #                       '没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态没啥事就想发一条动态')
        #

        editMain=self.wd.find_element_by_xpath('//*[@class="DRE-wrapper"]//*[@data-text="true"]')

        editMain.send_keys(Keys.CONTROL, 'v')

        # editMain.send_keys('这是一段文字')
        # sleep(2)
        # editMain.send_keys(Keys.ENTER)
        # sleep(2)
        # editMain.send_keys('这是2段文字')
        # sleep(1)
        # editMain.send_keys('这是3段文字')
        # editMain.send_keys(Keys.ENTER)
        # editMain.send_keys('这是4段文字')
        #
        # editMain.send_keys(Keys.ENTER)
        #
        # editMain.send_keys('这是5段文字')
        # sleep(2)
        # editMain.send_keys(Keys.CONTROL,'a')
        # sleep(1)
        # self.wd.find_element_by_xpath('//*[@class="DRE-toolbar-selector-active"]').click()
        # sleep(1)
        # self.wd.find_element_by_xpath('//*[@class="DRE-toolbar-selector-list"]// *[text() = "标题1"]').click()

        sleep(12)







