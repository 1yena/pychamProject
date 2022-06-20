# 카메라로 캡처된 이미지로 동영상 만들기
import cv2


cap = cv2.VideoCapture(0)

# 코덱 지정 코드
# 'XVID' : 사용할 코덱 이름
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 첫 번째 아규먼트 : 저장될 동영상 파일 이름
# 두 번째 아규먼트 : 동영상 저장 시 사용되는 코덱
# 세 번째 아규먼트 : 초당 30프레임으로 촬영
# 네 번째 아규먼트 : 저장할 영상의 크기 -> 캡처되는 이미지 크기와 일치해야 함
writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))


while(True):
    ret,img_color = cap.read()

    if ret == False:
        continue

        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    cv2.imshow("coool", img_color)
    cv2.imshow("gray", img_gray)

    writer.write(img_color)

    if cv2.waitKey(1)&0xFF == 27:
        break


cap.release()
writer.release()

cv2.destroyAllWindows()


