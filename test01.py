
import numpy as np
import cv2 as cv
import os
import cv2
from matplotlib import pyplot as plt



# 현재 디렉토리 확인
# os.getcwd()

# 현재 작업 디렉토리를 동영상 파일 위치로 변경
# os.chdir('')
# os.getcwd()


# 카메라 불러오기 
# capture1 = cv2.VideoCapture(0)
# capture2 = cv2.VideoCapture(1)
# 
# capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# 
# capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# 
# while cv2.waitKey(1) < 0:
#     ret, frame = capture1.read()
#     ret, frame = capture2.read()
#     cv2.imshow("VideoFrame1", frame)
#     cv2.imshow("VideoFrame2", frame)
# 
# capture1.release()
# capture2.release()
# cv2.destroyAllWindows()



# 영상 불러오기
# 열화상
cap1 = cv.VideoCapture('otter1.avi')

# 가시광
cap2 = cv.VideoCapture('otter2.avi')

# 각각의 영상 크기 정보 출력
print(cap1.shape)
print(cap1.shape)

# 영상 크기 조절
dst = cv2.resize(cap1, dsize=(640, 480), interpolation=cv2.INTER_CUBIC)
dst = cv2.resize(cap2, dsize=(640, 480), interpolation=cv2.INTER_AREA)

# 영상 합치기1
# result = cv2.add(cap1, cap2)
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.show()

# 영상 합치기2
# result = cap1 + cap2
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.show()

# 영상 합치기3
cv2.addWeighted(cap1, 0.5, cap2, 0.5, 0.0)





