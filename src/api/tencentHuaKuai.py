from time import sleep
from selenium.webdriver import ActionChains

class tencentHuaKuai:
    ###----腾讯滑块验证码破解(2021.5)可用---###
    # 使用方法：
    #       初始化传入iframeNode,也就是验证码框的元素节点
    #       直接调用 run（offsetX，offsetY） X和Y偏移量
    #######################################
    def __init__(self,iframeNode):
        self.iframeNode = iframeNode
    def randOffset(self,distance):
        #使滑块模拟人的滑动有平滑加速度
        self.tracks = [] # 移动轨迹
        current = 0 # 当前位移
        mid = distance * 1 / 2 # 减速阈值
        t = 0.4 # 计算间隔
        v = 0  # 初速度
        while current < distance:
            if current < mid:
                a = 10   # 加速度为2
            else:
                a = -3  # 加速度为-2
            v0 = v
            v = v0 + a * t   # 当前速度
            move = v0 * t + 1 / 2 * a * t * t    # 移动距离
            current += move # 当前位移
            self.tracks.append(round(move)) # 加入轨迹

    def is_Dom_Display(self):
        #判断验证码框是否存在
        print('判断验证码框是否存在！ ')
        try:
            self.element = self.iframeNode.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
            print(self.element)
            print("验证码框存在！")
            return True
        except:
            print("检测验证码框不存在！")
            return False

    def tryChangeSliderCode(self):
        #尝试切换到验证码框，超时一分钟结束
        for i in range(20):
            print('尝试切换到验证码框')
            sleep(3)
            if self.is_Dom_Display():
                print('已经切换到验证码框')
                self.iframeNode.switch_to.frame(self.element) #验证码框存在，切换到该元素
                break

    def SlideblockFunc(self):
        print('进行滑动验证码滑块!')
        slideblock = self.iframeNode.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
        ActionChains(self.iframeNode).click_and_hold(slideblock).perform()
        sleep(1)
        self.randOffset(self.offsetX)
        print(self.tracks)
        for x in self.tracks:
            ActionChains(self.iframeNode).move_by_offset(xoffset=x, yoffset=0).perform()
        sleep(0.3)
        ActionChains(self.iframeNode).pause(2)
        ActionChains(self.iframeNode).click(slideblock).perform()
        ActionChains(self.iframeNode).release()
        print('验证码滑块滑动结束！!')
        sleep(5)
        self.iframeNode.switch_to.default_content()
    def run(self,offsetX=210,offsetY=0):
        self.offsetX = offsetX
        self.offsetY = offsetY
        print('过滑块验证码开始执行！')
        self.tryChangeSliderCode()  # 尝试切换进验证码框
        self.SlideblockFunc()  #滑动验证码
        for i in range(10):
            if not self.is_Dom_Display() and i==0:
                print("找不到验证码所在的标签")
            elif  self.is_Dom_Display():  #如果验证码框还存在，说明没验证成功，刷新图片
                self.tryChangeSliderCode()
                self.iframeNode.find_element_by_xpath('//div[@class="tc-action-icon"]').click() #刷新图片
                print("刷新图片!")
                sleep(3)
                self.SlideblockFunc()  #再次滑动验证码滑块
                if i>=9:
                    print("超过10次滑动失败！已结束！")
                    return False
            else:
                print('破解滑动验证码成功！')
                return True







