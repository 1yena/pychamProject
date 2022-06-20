import cv2

# imread : 이미지 읽기
img_basic = cv2.imread('images.jpg', cv2.IMREAD_COLOR)

# imshow : 이미지를 화면에 보이게 출력
cv2.imshow('Image Basic', img_basic)

# waitKey : 이미지가 바로 꺼지지 않고 유지하게 함.
# argument를 '0'으로 하면 시간이 무한.
cv2.waitKey(0)

# imwrite : 이미지를 다른 파일 형식으로 저정함
cv2.imwrite('cat.png', img_basic)


# destroyAllWindows : 첫 번째 이미지 파일을 닫고 두 번째 이미지 파일 실행
cv2.destroyAllWindows()


# cvtColor : 이미지를 회색(흑백)으로 체인지.
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGRA2GRAY)
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)
cv2.imwrite('cat_Gray.png', img_gray)












