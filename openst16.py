
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 텍스트 그리기
# cv2.putText(image, text, position, font_type, font_scale, color): 하나의 텍스트를 그리는 함수
#   - position: 텍스트가 출력될 위치
#   - font_type: 글씨체
#   - font_scale: 글씨 크기 가중치 (글씨체 크기)


image = np.full((512, 512, 3), 255, np.uint8)
# 0, 200 위치에서
# FONT_ITALIC : 이탤릭체로
# 2 : 글자 크기
# (255, 0, 0) : 레드
image = cv2.putText(image, 'Hello World', (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))

plt.imshow(image)
plt.show()







