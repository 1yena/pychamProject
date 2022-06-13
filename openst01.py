
import cv2


# imread : 이미지를 읽어 Numpy 객체로 만드는 함수
# - cv2.imread(file_name, flag)
# - file_name : 읽어올 이미지 이름.
# - flag : 이미지를 어떻게 읽을 건지 이미지 읽는 방법 설정
#       - IMAGE_COLOR : 이미지를 칼라로 읽고, 투명한 부분은 무시
#       - IMAGE_GRAYSCALE : 이미지를 흑백으로 읽음
#       - IMAGE_UNCHANGED : 이미지를 칼라로 읽고, 투명한 부분도 읽음(Alpah).

# 반환값 : Numpy 객체 (행, 열, 색상 : BGR을 따름)
# 일반적으론 RGB로 처리하지만 OPENCV에서는 B와 R의 순서가 바뀜



# imshow : 이미지를 화면에 보이도록 출력
# - cv2.imshow(title, image)
# - title : 윈도우 창의 제목
# - image : 출력할 이미지 객체



# imwrite : 이미지를 파일로 저장하는 함수
# - cv2.imwrite(file_name, image)


# cv2.waitKey(time) : 키보드 입력을 처리하는 함수로 사용한 지정한 시간까지 이미지를 띄워줌
# '0'을 입력하면 무한대기



# cv2.destroyAllWindows() : 화면의 모든 윈도우를 닫는 함수



# 칼라 이미지로 출력
img_basic = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

# 'cat_img'이란 이름으로 이미지 보여줌
cv2.imshow('cat_img', img_basic)

cv2.waitKey(0)

cv2.destroyAllWindows()

# 'cat.png'로 다시 파일 저장
cv2.imwrite('cat.png', img_basic)


# cvtColor : 읽어들인 이미지에 특정한 속성을 부여함.
# 이미지를 흑백으로 전환
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('cat_gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()






