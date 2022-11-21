import cv2
import numpy as np

# img = cv2.imread('./0110.png')
img = cv2.imread('./33.jpg')
# img = cv2.imread('./2.png')
# img = cv2.cvtColor(imgorig, cv2.COLOR_BGR2RGB)
# print(img.shape, img[1,1])
cv2.imshow('my', img)
# cv2.waitKey(0)

res = cv2.resize(img, (int(img.shape[1]/5),int(img.shape[0]/5)), cv2.INTER_CUBIC)
# print(res.shape)
# cv2.imshow('my1', res)
# cv2.waitKey(0)
# res1 = res[10:110, 20:120]
# res1 = res
# cv2.imshow('my2', res1)
# cv2.waitKey(0)
# print(res1.shape)
yadro = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
# yadro = np.array([[1,0,-1],[2,0,-2],[1,0,-1]]) # sobel
# yadro = np.array([[0,0,0],[1,1,1],[0,0,0]])/3
# print(np.sum(yadro*res1[0:3,0:3,0]))
size = (int)(res.shape[0]-2)
res2 = np.zeros((size,size,3))
for i in range(size):
    for j in range(size):
        for k in range(3):
            res2[i,j,k] = np.sum(yadro*res[i:i+3,j:j+3,k])
cv2.imshow('my3', res2)
# cv2.waitKey(0)
half_size = int(size/2)+2
res3 = np.zeros((half_size,half_size,3))
for i in range(0,size,2):
    for j in range(0,size,2):
        for k in range(3):
            res3[i//2,j//2,k] = np.sum(res2[i:i+2,j:j+2,k])
cv2.imshow('my4', res3)
cv2.waitKey(0)

cv2.destroyAllWindows()