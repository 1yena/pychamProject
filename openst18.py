

import cv2
import matplotlib.pyplot as plt


# cv2.boundingRect(contour) : contour를 포함하는 사각형을 그림
# 사각형의 x, y 좌표와 너비, 높이를 반환합니다.

image = cv2.imread('digit_img.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold()를 이용해서 밝기(픽셀의 값)가 230 이상은 255(흰색), 아니면 0(검정색)을 줌
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)

# bitwise_not() : 흰색과 검정색을 반전 시킴
thresh = cv2.bitwise_not(thresh)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
# 모든(-1) 컨투어를 초록색((0, 255, 0))으로 그림
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

contour = contours[0]
x, y, w, h = cv2.boundingRect(contour)
# rectangle()를 이용하여 빨간((0, 0, 255)) 사각형을 그림
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()






