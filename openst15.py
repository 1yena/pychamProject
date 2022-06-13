
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 다각형 그리기
# cv2.polylines(image, points, is_closed, color, thickness) : 하나의 다각형을 그리는 함수
#   - points : 꼭짓점들
#   - is_closed : 닫힌 도형 여부

image = np.full((512, 512, 3), 255, np.uint8)

# 각각의 꼭짓점(4사형 -> 4개)을 2차원 형태로 배열에 담음
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (0, 255, 0), 4)

plt.imshow(image)
plt.show()


























