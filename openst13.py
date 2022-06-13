
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 사각형 그리기
# cv2.rectangle(image, start, end, color, thickness) : 하나의 사각형을 그리는 함수

image = np.full((512, 512 ,3), 255, np.uint8)
image = cv2.rectangle(image, (20, 20), (255, 255), (0, 0, 255), 3)

# 두께에 "-1" 값을 넣으면 사각형을 채움
# image = cv2.rectangle(image, (20, 20), (255, 255), (0, 0, 255), -1)

plt.imshow(image)
plt.show()









