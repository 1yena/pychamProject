

import cv2
import numpy as np
import matplotlib.pyplot as plt


# 직선 그리기
# cv2.line(image, start, end, color, thickness) : 하나의 직선을 그리는 함수
# start : 시작 좌표(2차원)
# end : 종료 좌표(2차원)
# color : 선 색깔
# thickness : 선 두께

# 가로*세로 길이가 512
# 3 : rgb 세 가지 색상을 가지게 함
# 255 : 모든 값을 255로 full() 함수를 이용해 초기화함.
# np.uint8 : 8비트 값을 가지게 해서 255까지의 값을 가지게 함
image = np.full((512, 512, 3), 255, np.uint8)

# 0*0 ~ 255*255까지의 직선.
# (0, 255, 0) : 색깔은 그린.
# 3 : 두께는 3.
image = cv2.line(image, (0, 0), (255, 255), (0, 255, 0), 3)

plt.imshow(image)
plt.show()














