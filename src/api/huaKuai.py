import io
import time
import random
import selenium
from PIL import Image
from selenium.webdriver import ActionChains


def shake_mouse(self):
    """
    模拟人手释放鼠标抖动
    :return: None
    """
    ActionChains(self.driver).move_by_offset(xoffset=-2, yoffset=0).perform()
    ActionChains(self.driver).move_by_offset(xoffset=2, yoffset=0).perform()


def operate_slider(self, track):
    '''
       拖动滑块
    '''
    # 获取拖动按钮
    back_tracks = [-1, -1, -2, -1]
    slider_bt = self.driver.find_element_by_xpath('//div[@tcaptcha_drag_thumb"]')

    # 点击拖动验证码的按钮不放
    ActionChains(self.driver).click_and_hold(slider_bt).perform()

    # 按正向轨迹移动
    for i in track:
        ActionChains(self.driver).move_by_offset(xoffset=i, yoffset=0).perform()
        # 先加速后减速效果也不是很好。
        # 每移动一次随机停顿0-1/100秒之间骗过了极验，通过率很高
        time.sleep(random.random() / 100)
    time.sleep(random.random())
    # 按逆向轨迹移动
    for i in back_tracks:
        time.sleep(random.random() / 100)
        ActionChains(self.driver).move_by_offset(xoffset=i, yoffset=0).perform()
    # 模拟人手抖动
    self.shake_mouse()
    time.sleep(random.random())
    # 松开滑块按钮
    ActionChains(self.driver).release().perform()





