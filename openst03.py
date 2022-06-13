
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('cat2.jpg')

# ROI 추출 및 복사(이미지 관심(interest) : 이미지를 추출할 때 해당 영역을 interest한 공간이라고 함)
# Numpy Slicing: ROI 처리 가능
roi = image[200:350, 50:200]

# ROI 단위로 이미지 복사하기
# 앞에 0:150 -> shape가 복사한 크기 0 ~ 150
# 뒤에 0:150 -> 복사한 이미지 붙여넣을 크기 0 ~ 150
# but. 복사한 크기와 붙여넣을 크기가 같아야 오류 안 남!
image[0:150, 0:150] = roi

# 이렇게 복사한 크기보다 붙여넣을 크기가 더 큰 경우 오류남
# image[0:150, 0:155] = roi

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()