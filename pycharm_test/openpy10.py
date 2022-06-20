
import cv2
# import matplotlib.pyplot as plt
import time

from matplotlib import pyplot as plt

image = cv2.imread('cat.png')

print(image.shape)
print(image.size)

# cv2.imshow('catIm', image)
# cv2.waitKey(0)

px = image[100, 100]

print(px)
print(px[2])

print('-----------------------')

start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))

...
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))
...

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()













