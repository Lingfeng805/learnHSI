import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.stats import chi2
import spectral as spy
import numpy as np
import HSITools as hsi


def anomaly_detect_demo(img):
    view1 = spy.imshow(data=img, bands=[76, 46, 25], title="img")    # RGB伪图图像显示
    rxvals = spy.rx(img)  # 马氏距离平方
    nbands = img.shape[-1]
    P = chi2.ppf(0.999, nbands)  # 阈值设为0.001
    # view2 = spy.imshow(1 * (rxvals > P), title='rxvals>P')  # 将像素中大于P=239的部分作为异常显示出来
    view3 = spy.imshow(rxvals,stretch=(0.99,0.9999),title="local")
    # view4 = spy.imshow(rxvals)    # 除了为异常像素指定阈值，还可以简单地查看原始RX分数的图像，其中较亮的像素被认为是“更异常的”


def match_demo(img):
    t = img[750, 645]  # 灰布处
    mf_scores = spy.matched_filter(img, t)
    mask = 1 * (mf_scores > 0.2)  # 匹配值大于0.2时的目标
    view = spy.imshow(data=img, bands=[76, 46, 25], title="result", classes=mask, colors=[255, 0, 0])
    view.set_display_mode("overlay")
    view.class_alpha = 1  # 红色显示为检测到的位置 c/d切换显示模式



filename = "D:/高光谱/data/汽车（含白布）/newrawfile20210810112704_lensCor_ref_flassh.raw"    # 经过预处理后得到的反射率数据
img3D = hsi.ReadRaw(filename,1057,960,176)    # 得到HSI数据立方体
remove_bands = np.hstack((range(125, 176))) # 剔除对应于低质量的波段（125-176）
img3D = np.delete(img3D, remove_bands, axis=2)
img2D = hsi.hyperconvert2d(img3D)

# print(img2D.shape,img3D.shape)
imgmat = hsi.Transformtomat(img2D,img2D[:,489888])
# print(type(imgmat))



# anomaly_detect_demo(img3D)
# match_demo(img3D)
# view1 = spy.imshow(img3D,(29,19,9),title='Picture')    # 原图
# spy.view_cube(img3D, bands=[76, 46, 25])  # 3D立方体显示；显示后会打印相应功能及操作

plt.pause(60)



