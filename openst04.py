

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('cat2.jpg')

# 모든 픽셀의 빨간색 값을 모두 '0'으로 만듦.
image[:, :, 2] = 0

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()