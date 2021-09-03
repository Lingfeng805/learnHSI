import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.stats import chi2
import spectral as spy

imgX = loadmat('D:\高光谱\learnHSI/hsi2D.mat')['X']
imgd = loadmat('D:\高光谱\learnHSI/hsi2D.mat')['d']
imgGt = loadmat('D:\高光谱\learnHSI/hsi2D.mat')['groundtruth']
# gt = loadmat("./data/Salinas_gt.mat")['salinas_gt']
print(imgX.shape,imgd.T.shape,imgGt.shape)