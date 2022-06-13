
import cv2
import matplotlib.pyplot as plt



# 적응 임계점 처리 : 하나의 이미지에 다수의 조면 상태가 존재하는 경우 적용하면 좋음.
# 전체 이미지에 대해서 여러개의 필터를 사용하요 임계점을 처리.

# cv2.adaptiveThreshold(image, max_value, adaptive_method, type, block_size, C) :적응 임계점 처리 함수
#   - max_value : 임계값을 넘었을 때 적용할 값
#   - adaptive_method : 임계값을 결정하는 계산 방법
#           - ADAPTIVE_THRESH_MEAN_C : 주변 영역의 평균값으로 결정
#           - ADAPTIVE_THRESH_GAUSSIAN_C : 정규분포 형태
#   - type : 임계점 처리 방식
#   - block_size : 임계값을 적용할 영역의 크기
#   - C : 평균이나 가중 평균에서 차감할 값


image = cv2.imread('hand_writing.jpg', cv2.IMREAD_GRAYSCALE)

ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# ADAPTIVE_THRESH_MEAN_C : 사용자가 값을 직접 입력하는 게 아니라 자동으로 이미지에서 임계점을 찾아줌
# 21, 3 : 필터의 크기
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres1, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres2, cv2.COLOR_GRAY2RGB))
plt.show()

















