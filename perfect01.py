
import cv2


# 주임님 열화상 + 가시광 코드 !!!!!!!


# 열화상 카메라 불러옴
cap1 = cv2.VideoCapture(0)
# 가시광 카메라 불러옴
cap2 = cv2.VideoCapture(1)

while 1:
    # 영상 읽기
    ret0, img0 = cap1.read()
    ret1, img1 = cap2.read()

    # 사이즈 설정
    image1 = cv2.resize(img0, (640, 480))
    image2 = cv2.resize(img1, (640, 480))

    # 투명도를 조작해 두 영상을 합치기
    func = cv2.addWeighted(image1, 0.3, image2, 0.7, 0)

    if (cap1):
        cv2.imshow('add', func)

    # 처리시간 0.03초
    k = cv2.waitKey(30)

    # 27 : esc 유니코드 -> esc 누르면 종료됨
    if k == 27:
        break

cap1.release()

cv2.destroyAllWindows()






