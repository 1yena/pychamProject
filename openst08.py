

import cv2
import matplotlib.pyplot as plt


# 이미지 합치기
# 1. cv2.add() : saturation 연산을 수행
#   - 0보다 작으면 0, 255보다 크면 255로 표현

# 2. np.add() : Modulo(나머지) 연산을 수행 -- 잘 사용 안 함
#   - 256은 0, 257은 1로 표현



# image_1 = cv2.imread('image_1.jpg')
# image_2 = cv2.imread('image_2.png')

# result = cv2.add(image_1, image_2)
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.show()

# result = image_1 + image_2
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.show()



image_1 = cv2.imread('sky.jpg')
image_2 = cv2.imread('keyboard.jpg')

result = cv2.add(image_1, image_2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()

result = image_1 + image_2
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()















