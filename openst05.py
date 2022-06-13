
import cv2
import matplotlib.pyplot as plt


# 보간법(interpolation) : 이미지 사이즈가 변할 때 픽셀 사이의 값을 조절하는 방법.
# (이미지(픽셀)를 늘릴 때 확대되는 이미지가 깨짐 없이 분포대로 매끄럽게 처리되도록 함.)
# cv2.resize(image, dsize, fx, fy, interpolation) : 이미지 크기를 조절함.
#     - dsize : Manual size
#     - fx : 가로 비율
#     - fy : 세로 비율
#     - interpolation : 사용항 보간법의 알고리즘
#          - INTER_CUBIC : 사이즈를 크게 할 때 사용
#          - INTER_AREA : 사이즈를 작게 할 때 사용


# 이미지를 읽어온 후
# matplotlib 라이브러리에선 RGB형식을 사용하기 때문에 기존의 BGR형식을 RGB로 전환
image = cv2.imread('cat2.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# 이미지 크기를 가로, 세로 2배씩 커지게 함
expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
plt.imshow(cv2.cvtColor(expand, cv2.COLOR_BGR2RGB))
plt.show()

# 이미지 크기를 가로, 세로 20%씩 줄임
shrink = cv2.resize(image, None, fx= 0.8, fy=0.8, interpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB))
plt.show()














