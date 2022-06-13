
import cv2
import matplotlib.pyplot as plt


# cv2.findContours(image, mode, method): 이미지에서 Contour들을 찾는 함수
# 이미지 안에서 어떠한 사물의 테두리를 구분할 때 사용.
#   - mode: Contour들을 찾는 방법
#       1) RETR_EXTERNAL: 바깥쪽 Line만 찾기
#       2) RETR_LIST: 모든 Line을 찾지만, Hierarchy 구성 X
#       3) RETR_TREE: 모든 Line을 찾으며, 모든 Hierarchy 구성 O

#   - method: Contour들을 찾는 근사치 방법
#       1) CHAIN_APPROX_NONE: 모든 Contour 포인트 저장
#       2) CHAIN_APPROX_SIMPLE: Contour Line을 그릴 수 있는 포인트만 저장
# 입력 이미지는 Gray Scale Threshold(흑백) 전처리 과정이 필요합니다.

# Contours 그리기
# cv2.drawContours(image, contours, contour_index, color, thickness): Contour들을 그리는 함수
# contour_index: 그리고자 하는 Contours Line (전체: -1)


image = cv2.imread('gray_img.jpg')

# 해당 이미지를 그레이 형태로 불러옴
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold()를 이용해 이진화 처리해줌
# (흑백으로 구분함 -> 127값보다 큰 값들은 전부 다 255(white)로 설정하고 그렇지 않은 값들은 0(black)으로 설정함)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

# threshold에 대해서 컨투어를 찾게 만듦
# RETR_TREE : 모든 컨투어를 찾게 함
# RETR_EXTERNAL : 바깥쪽의 라인만 찾게 함
# contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
# contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# -1 : 모든 컨투어를 출력
# ('0'으로 줄 경우 첫 번째의 외곽만 그려짐)
# ('1'로 줄 경우 두 번째 외관 2는 세 번째 ~~)
# image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)
image = cv2.drawContours(image, contours, 0, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()










