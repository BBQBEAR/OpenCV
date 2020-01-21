# pip-> numpy, opencv-python, opencv-contrib-python
# 讀入圖放picture/input下面, 輸出picture/output
import cv2
import numpy as np
import os

# 讀入後灰階才可二階化 二階化後可取輪廓 再取胎心音圖及宮縮圖
# 抓資料夾內圖片檔名
for filename in os.listdir(r"./picture/input/"):
    # 讀picture/input下的圖片
    m1 = cv2.imread("picture/input/" + filename, 1)
    # 灰階
    m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
    # 二階化
    t1, m3 = cv2.threshold(m2, 130, 255, cv2.THRESH_OTSU)
    # 取輪廓
    c1, t1 = cv2.findContours(m3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # 暫存圖片用
    m5 = []
    # [0]為圖片邊框 故從1開始
    for i in range(1, len(c1)):
        # 取得輪廓點矩型
        x, y, w, h = cv2.boundingRect(c1[i])
        # 塞選過小的輪廓
        if w > h and w > 850:
            # 取座標
            m5.append((x, y, w, h))

    baby = m5[1]
    mon = m5[0]
    m6_h = mon[1] - baby[1] + mon[3]
    m6_w = baby[2]
    m6 = m1[baby[1]:baby[1] + m6_h, baby[0]:baby[0] + m6_w]
    try:
        # 存檔 存在picture/output資料夾內
        cv2.imwrite(f"picture/output/full_{filename}", m6, [cv2.IMWRITE_JPEG_QUALITY, 100])
    except:
        pass

# cv2.imshow("m1", m1)
# cv2.imshow("m6", m6)
# cv2.waitKey(0)
# cv2.destroyAllWindows()