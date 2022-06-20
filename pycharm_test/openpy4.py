# 이진화 : grayscale 이미지를 흰색과 검은색으로 구성된 바이너리 이미지(binary image)로 변환시킴
# 영상처리 알고리즘을 적용하기 전에 전 처리 단계
# 배경과 오브젝트를 분리하는 것도 가능

import cv2

def nothing(x):
    pass

cv2.namedWindow('Binary')

cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 98)

img_color = cv2.imread('apple.jpg', cv2.IMREAD_COLOR)

cv2.imshow('Color', img_color)
cv2.waitKey(0)


img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGRA2GRAY)

cv2.imshow('Gray', img_gray)
cv2.waitKey(0)


while(True):
    low = cv2.getTrackbarPos('threshold', 'Binary')

    # 첫 번째 아규먼트 : 이진화할 대상 이미지(grayscale 이미지여야 함)
    # 두 번째 아규먼트 : 쓰레스홀드 - 이 값을 기준으로 결과 픽셀이 검은색 또는 흰색으로 나옴
    # 그레이스케일 이미지에선 값이 높을수록 픽셀은 밝게 보임
    # 이진화된 이미지는 임계값을 기준으로 그레이스케일 이미지 픽셀을 두 개의 영역으로 나눔
    # THRESH_BINARY_INV : 이미지 흑백 색을 반전시켜줌
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Binary", img_binary)

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    cv2.imshow('Result', img_result)

    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.destroyAllWindows()











