import cv2 as cv

# 이미지 불러오기 (처음부터 흑백 그레이스케일 모드로 읽기)
img = cv.imread('Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

# 오추 이진화(Otsu Thresholding) 적용
# 픽셀 밝기 분포를 분석해 가장 이상적인 흑/백 분리 임계값(Threshold)을 자동으로 찾아줍니다.
ret, binary_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

print("자동 계산된 임계값:", ret)

# 결과 출력
cv.imshow('Original', img)
cv.imshow('Otsu Thresholding', binary_img)

cv.waitKey(0)
cv.destroyAllWindows()