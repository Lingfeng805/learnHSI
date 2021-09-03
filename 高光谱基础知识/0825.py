from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# imgX = loadmat('D:\高光谱\learnHSI/hsi2D.mat')['X']
# imgd = loadmat('D:\高光谱\learnHSI/hsi2D.mat')['d']

imgX = loadmat('D:\高光谱\目标检测\E_CEM-for-Hyperspectral-Target-Detection\hyperspectral_data/san.mat')['X']    # 数据是浮点数
imgd = loadmat('D:\高光谱\目标检测\E_CEM-for-Hyperspectral-Target-Detection\hyperspectral_data/san.mat')['d']    # 数据是浮点数
imggt= loadmat('D:\高光谱\目标检测\E_CEM-for-Hyperspectral-Target-Detection\hyperspectral_data/san.mat')['groundtruth']    # 数据是浮点数

def cem(img,tgt):
    # Basic implementation of the Constrained Energy Minimization (CEM) detector
    # Farrand, William H., and Joseph C. Harsanyi. "Mapping the distribution of mine tailings
    # in the Coeur d'Alene River Valley, Idaho, through the use of a constrained energy minimization
    # technique." Remote Sensing of Environment 59, no. 1 (1997): 64-76.
    size = img.shape  # get the size of image matrix
    R = np.dot(img, img.T / size[1])  # R = X*X'/size(X,2);
    w = np.dot(np.linalg.inv(R), tgt) # w = (R+lamda*eye(size(X,1)))\d ;
    w = w/np.dot(tgt.T,w)
    result = np.dot(w.T, img).T  # y=w'* X;
    return result

# print(imgd)
# print(imgd.T)
result = cem(imgX,imgd)
print(imgX.shape)
plt.figure()
plt.imshow(result.reshape(200,200),cmap='gray')
plt.figure()
plt.imshow(imggt)
plt.pause(60)