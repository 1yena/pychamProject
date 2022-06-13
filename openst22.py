
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 직접 커널을 생성하여 필터 적용하기


# 이미지에 커널을 적용하여 이미지를 흐리게(Blurring = Smoothing) 처리할 수 있습니다.
# 이미지를 흐리게 만들면 노이즈 및 손상을 줄일 수 있습니다.
# 특정한 이미지에서 커널(Kernel, 윈도우)을 적용해 컨볼루션 계산하여 필터링을 수행할 수 있습니다.


image = cv2.imread('gray_img.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()


# 1/16 1/16 1/16 1/16
# 1/16 1/16 1/16 1/16
# 1/16 1/16 1/16 1/16

size = 4
kernel = np.ones((size, size), np.float32) / (size ** 2)
print(kernel)

# filter2D() : 주변에 있는 4*4 영역을 확인한 다음 그것의 평균값을 해당 픽셀의 값으로 적용
dst = cv2.filter2D(image, -1, kernel)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()




