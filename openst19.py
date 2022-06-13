

import cv2
import matplotlib.pyplot as plt


# cv2.convexHull(contour): Convex Hull 알고리즘으로 외곽을 구하는 함수
#   - 대략적인 형태의 Contour 외곽을 빠르게 구할 수 있습니다. (단일 Contour 반환)
#   - 여러개의 벡터(포인트)가 있을 때 외곽으로만 구성된 다각형을 찾음

image = cv2.imread('digit_img.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

contour = contours[0]
hull = cv2.convexHull(contour)

# 파란 다각형을 그림
image = cv2.drawContours(image, [hull], -1, (255, 0, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()















