from hashlib import sha1
import numpy as np
import cv2

img = cv2.imread('./smile.png',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(img),"\n",img)

kernel = np.array(
    [
        [-1, -1, -1],
        [-1, 13, -1],
        [-1, -1, -1],
        ])
print("kernel: ",type(kernel),"\n",kernel)
img_len = len(img)
b = np.resize(img, [3, 3])
print(b)


for y in range(img_len-2):
    for x in range(img_len-2):
        for yn in range(3):
            for xn in range(3):
                img[yn][xn]