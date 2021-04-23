import os
import traceback
import urllib.error
import urllib.request
import cv2

temp_dir = os.path.realpath(__file__) + '../temp/'
def download_img(url, file):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
    })
    try:
        res = urllib.request.urlopen(req)
        fp = open(temp_dir + file, "wb")
        fp.write(res.read())
    except urllib.error.HTTPError:
        print('download img error!')  # 完整图片很大概率会下载失败，要多次下载
        download_img(url, file)
# 计算滑块偏移量
def calculate(url, debug=False):
    try:
        download_img(url, 'bg.jpg')  # 滑块背景图片
        download_img(url.replace('_1_', '_0_'), 'full.jpg')  # 滑块图
        download_img(url.replace('_1_', '_2_'), 'fg.png')  # 完整图片
        bg = cv2.imread(temp_dir + 'bg.jpg', 0)
        full = cv2.imread(temp_dir + 'full.jpg', 0)
        template = cv2.imread(temp_dir + 'fg.png', 0)
        img = cv2.absdiff(full, bg)  # 完整图-背景图
        cv2.imshow('ret', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)  # 查找滑块位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if debug:
            h, w = template.shape[:2]
            left_top = max_loc  # 左上角
            right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
            ret = cv2.rectangle(bg, left_top, right_bottom, 255, 2)  # 画出矩形位置
            cv2.imshow('ret', ret)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return max_loc[0] / 680 * 330 - 26  # 这里注意计算，主要是看网页打开时，图片大小，这个时自适应的。
    except:
        traceback.print_exc()
        return 100


calculate("https://t.captcha.qq.com/hycdn?index=1&image=937200988422924800?aid=2044348370&sess=s0N2HmfgwhHtzgE2D9a-2lQk1HatwfV_2rtfVqYWCB5BzfMBZoNf-ibLcKFGHPXte47s0phLdvwhnTu7x-1gX1FHK6xZ59BQI274u8Ng2tavkts13XC_OUOJlHWj4Cktdb7t193jNDfdBZi3_2yKOBh8rNdG_aJOD58T0D4ic7vcAPtzO0UuE-mncyEIRUTnuK5wJGwVXzAHi8Zg1BM25CWW0rhEGlYz1H8sxwPDUZ9NuKR1jy4Q4CBTBzhcBHEHL-ZJRY3Z6yyg-HHlx9R85Nmmya2qupVhd5gdX3iN2J3QN3c3Gecyy3kA**&sid=6788533068024565761&img_index=1&subsid=3")


