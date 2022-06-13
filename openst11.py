
import cv2
import numpy as np


# Tracker
# cv2.createTrackbar(track_bar_name, window_name, value, count, on_change) : 트랙바를 생성하는 함수
# value : 초기 값
# count : max 값(min : 0)
# on_change : 값이 변경될 때 호출되는 Callback 함수


def change_color(x):
    # 각각의 트랙바가 가지고 있는 값을 가져옴(=RGB값을 각각 받아옴)
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")

    # 해당 RGB로 구성되는 background를 나타냄.
    image[:] = [b, g, r]

    # 값이 변경될 때마다 그 이미지를 화면에 출력함
    cv2.imshow('Image', image)

# 단순히 이미지 크기를 600*400 크기로 만듦
image = np.zeros((600, 400, 3), np.uint8)
# 윈도우에 표시될 이름 "Image"
cv2.namedWindow("Image")

# 아래 세가지 트랙바를 "Image"란 이름을 가진 윈도우에 달아줌
# 0 ~ 255까지 변경될 수 있도록 함.
# 사용자가 트랙바를 사용할 때마다 위에서 만든 함수(change_color)값을 가져옴.
cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar("G", "Image", 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

cv2.imshow('Image', image)
cv2.waitKey(0)








