

import cv2
import matplotlib.pyplot as plt


# Gaussian Blur


image = cv2.imread('gray_img.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# kernel_size: 홀수
dst = cv2.GaussianBlur(image, (5, 5), 0)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()
