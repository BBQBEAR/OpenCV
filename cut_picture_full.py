import cv2
import os
import numpy as np
# 讀入後灰階才可二階化 二階化後可取輪廓 再取胎心音圖及宮縮圖
for k, filename in enumerate(os.listdir(r"./picture/input/")):
    #     # 讀圖片
    m1 = cv2.imread("picture/input/" + filename, 1)

    # m1 = cv2.resize(m1,(int(m1.shape[1]*0.3),int(m1.shape[0]*0.3)))
    # 灰階
    m2 = cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)
    # 二階化
    t1, m3 = cv2.threshold(m2, 130, 255, cv2.THRESH_OTSU)
    # 取輪廓
    c1, t1 = cv2.findContours(m3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # 存圖片用
    m5 = []
    x0, y0, w0, h0 = cv2.boundingRect(c1[0])
    # [0]為圖片邊框 故從1開始
    for i in range(1,len(c1)):
        # 取得輪廓點最小矩型
        x, y, w, h = cv2.boundingRect(c1[i])
        # 塞選過小的輪廓
        if w > h and w > int(w0*0.8):
            # 印出矩形
            cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
            # 切!
            m4 = m1[y:y + h, x:x + w]
            # 存
            m5.append(m4)
            # 秀一波
            # cv2.imshow(f"cut!cut!{i}", m4)
    # 寬度微調 讓寬度一樣(以胎音為主)
    m5[0] = cv2.resize(m5[0],(m5[1].shape[1],m5[0].shape[0]))
    # 取2張圖的高
    baby_h = m5[1].shape[0]
    mon_h = m5[0].shape[0]

    # 取2張圖大小 製作空白底圖
    m6_y = baby_h + mon_h
    m6_x = m5[1].shape[1]
    m6 = np.full((m6_y, m6_x, 3), (255,255,255), np.uint8)

    # 貼胎音
    m6[0:baby_h,0:m6_x] = m5[1]
    # 貼宮縮
    m6[baby_h:baby_h+mon_h,0:m6_x] = m5[0]

    # 存檔
    cv2.imwrite(f"picture/output/new-{k}.jpg", m6, [cv2.IMWRITE_JPEG_QUALITY, 100])