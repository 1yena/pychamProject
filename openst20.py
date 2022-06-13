

import cv2
import matplotlib.pyplot as plt

# 유사 다각형 만들기

# cv2.approxPolyDP(curve, epsilon, closed): 근사치 Contour를 구합니다.
#   - curve: Contour
#   - epsilon: 최대 거리 (클수록 Point 개수 감소)
#   - closed: 폐곡선 여부

image = cv2.imread('digit_img.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

contour = contours[0]

# epsilon : 해당 컨투어의 길이값으로부터 유추할 수 있도록 만듦
# epsilon = 0.01 * cv2.arcLength(contour, True)
# 값을 줄일수록 섬세한 다각형 그려짐.
epsilon = 0.001 * cv2.arcLength(contour, True)

# approxPolyDP()를 사용해 초록색 유사 다각형 그림
approx = cv2.approxPolyDP(contour, epsilon, True)
image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()



