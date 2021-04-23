from time import sleep
from douBanFunc.DouBanFunc import *
from login.douBanLogin import douBanLogin
from defaultArgument    import baseLoginUrl
from Topic.submitTopic import submitTopic
from random import randint
class findTopic:
    def __init__(self, wd):
        self.wd = wd
        self.nowId = None
        self.groupInfo = None
        self.groupId = None
        self.nextIdNum=1
        self.isRandNextIdBool=False
    def setNextId(self,nextIdNum):
        self.nextIdNum=nextIdNum
    def isRandNextId(self,bool):
        self.isRandNextIdBool= bool

    def getGroupNameAndId(self):
        self.wd.get("https://www.douban.com/group/topic/" + str(self.nowId))
        print("当前访问的话题ID是：", self.nowId)
        try:
            self.groupInfo = self.wd.find_element_by_xpath('//*[@id="g-side-info"] //*[@class="title"]/a')
            print(self.groupInfo.text)
            print(self.groupInfo.get_attribute("href"))
            return True
        except:
            print(self.nowId, "==> 话题不存在！")
            return False

    def followGroup(self):    #加入小组
        #单次执行，单次判断某话题是否能关注
        GroupBottonCss = '//*[@class="member-status"]/*[contains(@class,"bn-join")]'
        try:
            followGroupBotton = self.wd.find_element_by_xpath(GroupBottonCss)
            isHasElem = hasEmement(self.wd, GroupBottonCss)
            if  isHasElem  and followGroupBotton.text=='申请加入小组':      #需要申请加入小组
                print('需要申请加入小组！')
                return False
            if  isHasElem and followGroupBotton.text=='加入小组':  # 是否还没有关注
                followGroupBotton.click()
                return True
            else:
                self.groupId = None
                print('已经关注过该小组了！')
                return False
        except:
            self.groupId = None
            return False    #这里不太严谨，可以不用返回应该不影响

    def putToDB(self):
        pass

    def run(self, nowId,runNum=2):
        self.nowId = int(nowId)
        self.orderLoopSubmitTopic(runNum)  # 顺序循环打开查看某ID的话题并关注发布话题，默认执行一次，可传值执行多次
    def nextId(self, *step):  # 找下一个笔记ID ，step表示ID的步长
        if len(step) == 0:
            self.nowId += 1
        else:
            self.nowId += step[0]
        print('步进',step[0],'步')
    def runNewAccount(self):
        #
        #       这里写注册新账号逻辑
        #
        print('登录新号码！')
        login=douBanLogin(self.wd,baseLoginUrl)
        login.mode_Two_PasswordLogin("15159669885","shy15544")
        # login.mode_Two_PasswordLogin("17895965885","shy15544")

    def orderLoopSubmitTopic(self, loopSum=1):
        Sum = 1
        while Sum <= loopSum:
            globalWatchErr(self.wd)
            if  not checkIsLogin(self.wd)  :
                self.runNewAccount()#重新登录新号码
                Sum -= 1
            if not self.getGroupNameAndId():  # 如果找不到该ID话题
                print("当前话题未找到！")
                Sum -= 1
            else:    #找到话题
                if self.followGroup():  #执行成功的话内部已经进行过关注操作！
                    print('已经进行关注操作！')
                    ##  这里写发布话题的逻辑
                    # submitTopic

                    submitTopicArticle = submitTopic(self.wd, 'https://www.douban.com/group/716676/')
                    submitTopicArticle.run()
                    #####################
                else:
                    print('关注失败！')
            Sum += 1
            if  self.isRandNextIdBool:
                self.setNextId(randint(5, 12))
            self.nextId(self.nextIdNum)
            print('等待10秒找下一个！')
            sleep(10)



