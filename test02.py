

import cv2


# VideoCapture()로 영상을 불러오기
capture1 = cv2.VideoCapture(0)
capture2 = cv2.VideoCapture(1)

# 영상 프레임 사이즈
# 가시광 사이즈 (가로 640 * 세로 480)
capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 열화상 사이즈 (가로 640 * 세로 480)
capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 만약 카메라가 실행되고 있다면
if capture1.isOpened() and capture2.isOpened():
    # ret : True False Value임.
    # a, b는 영상 프레임을 읽어옴.
    ret, a = capture1.read()
    ret, b = capture2.read()

    # 제대로 카메라를 불러오면 반복문 실행
    while ret:
        # 이미지를 보여주는 방식과 같음
        ret, a = capture1.read()
        ret, b = capture2.read()

        cv2.addWeighted(capture1, 0.5, capture2, 0.5, 0.0)

        cv2.imshow("camera", a)
        cv2.imshow("camera", b)

        if cv2.waitKey(1) & 0xFF == 27:
            # 종료 커멘드
            break


# 카메라 사용 종료
capture1.release()
capture2.release()

# 창 닫기
cv2.destroyAllWindows()






