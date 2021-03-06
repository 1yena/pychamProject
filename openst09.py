
import cv2
import matplotlib.pyplot as plt


# 임계점(한계점, 문턱) 처리하기
# cv2.threshold(image, thresh, max_value, type) : 임계값을 기준으로 흑/백을 분류하는 함수
#   - image : 처리할 gray scale 이미지
#   - thresh : 임계값 (전체 픽셀에 적용) --한계치
#   - max_value : 임계값을 넘었을 때 적용할 값
#   - type : 임계점을 처리하는 방식
#       - THRESH_BINARY : 임계값보다 크면 max_value, 작으면 0
#       - THRESH_BINARY_INV : 임계값보다 작으면 max_value, 크면 0
#       - THRESH_TRUNC : 임계값보다 크면 임계값, 작으면 그대로
#       - THRESH_TOZERO : 임계값보다 크면 그대로, 작으면 0
#       - THRESH_TOZERO_INV : 임계값보다 크면 0, 작으면 그대로


image = cv2.imread('sky.jpg', cv2.IMREAD_GRAYSCALE)

images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
    plt.show()

# ////////////////////////////////////////////////    ////////////////////////////////////////////////////

image = cv2.imread('sky.jpg')

images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
    plt.show()









