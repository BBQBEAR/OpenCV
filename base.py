import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


# # 讀取圖片(檔案位置, 讀取方式 1:一般(不含透明度) 0:灰階 -1:完整(含透明度)
# rp = cv2.imread("picture/color3.jpg", 1)
# # 會以3維陣列形式表示
# print(rp)
# # 第一維:高
# print(len(rp))
# # 第二維:寬
# print(len(rp[0]))
# # 第三維:色彩值 [藍,綠,紅]
# print(rp[50,100],rp[150,50],rp[150,150])
# # shape->(高,寬,色彩通道(3為彩色,4為有透明值的色彩)
# print(rp.shape)

rp = cv2.imread("picture/color3.jpg", 0)
# # 灰階只有2維
# print(rp)
# # 黑 0~255 白
# print(rp[50,100],rp[150,50],rp[150,150])
# # shape->(高,寬)
# print(rp.shape)

# rp = cv2.imread("picture/cookies.png", -1)
# # 第4個為透明值
# print(rp[0,0])


# # 色彩空間轉換
# rp = cv2.imread("picture/color3.jpg", 1)
# print(rp[50,100])
# # BGR轉HSV
# rp = cv2.cvtColor(rp, cv2.COLOR_BGR2HSV)
# # HSV->[色彩,飽和值,亮度]
# print(rp[50,100])
# # BGR轉HLS
# rp = cv2.cvtColor(rp, cv2.COLOR_BGR2HLS)
# # BGR轉灰階
# rp = cv2.cvtColor(rp, cv2.COLOR_BGR2GRAY)
# # 灰階轉BGR
# rp = cv2.cvtColor(rp, cv2.COLOR_GRAY2BGR)


# # PNG支援透明色 ,JPG則無 但可壓縮(破壞型壓縮)
# # 存檔PNG格式(檔名,圖檔) JPG格式(黨名,圖檔,設定參數)
# cv2.imwrite("picture/cookies_gray_p.png", rp)
# # [cv2.IMWRITE_JPEG_QUALITY, 畫質比率0~100]越低壓縮越好但畫值低
# cv2.imwrite("picture/cookies_gray_j.jpg", rp, [cv2.IMWRITE_JPEG_QUALITY,90])
# cv2.imwrite("picture/cookies_gray_j2.jpg", rp, [cv2.IMWRITE_JPEG_QUALITY,10])


# 建圖:全彩((高,寬,色彩空間通道數),(BGR值),色彩空間都是8bit)
# rp = np.full((500, 500, 3), (250,20,30), np.uint8)
# # 灰階 ((高,寬),(色值),色彩陣列形式)
# rp = np.full((200,200), (50), np.uint8)
# # 畫線 (圖檔,起座標,終座標,色彩,粗細)
# rp = cv2.line(rp,(0,0),(140,140),(50,20,30),2)
# # 畫矩形
# rp = cv2.rectangle(rp,(0,0),(140,140),(50,20,30),2)
# # 畫圓形 (圖檔,中心座標,半徑,色彩,粗細)
# rp = cv2.circle(rp,(140,140),70,(50,20,30),2)

# # 寫字
# pen = Image.fromarray(rp)
# # 設定文字(TTF字型檔位置, 文字大小)
# font = ImageFont.truetype("kaiu.ttf",30)
# # .text(文字位置, 要寫的文字, 顏色, 文字設定)
# ImageDraw.Draw(pen).text((200,150),"大餅",(50,20,30),font)
# # 轉換回去
# rp = np.array(pen)


# # 顯示視窗(視窗名,圖片) 只認得BGR,灰階
# cv2.imshow("Img1", rp)
# # delay 不設置or設置0會等待使用者按下任意建
# cv2.waitKey(0)
# # 關閉所有視窗
# cv2.destroyAllWindows()