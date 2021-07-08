import numpy as np
import matplotlib.pyplot as plt
import spectral as spy

imagePath = "D:\高光谱\高光谱数据处理\虎溪河公园/newrawSinglefile20170101001420.raw"
rawImage = np.fromfile(imagePath,'int16')
rawShape = rawImage.shape
# 原始数据为BIL格式，raw存储数据按行存放，保存第一个波段的第一行后接着保存第二个波段的第一行，依次类推。
# 数据量为960*1057*176=178590720
formatImage = np.zeros((1057,960,176))
for row in range(0,1057):
    for dim in range(0,176):
        formatImage[row,:,dim] = rawImage[((dim + row*176)*960):((dim + 1 +row*176)*960)]
        pass
    pass

# PCA主成分分析
def pca_dr (img):
    pc = spy.principal_components(img)
    pc_098 = pc.reduce(fraction=0.98)    # 保留98%的特征值
    print(len(pc_098.eigenvalues))    # 剩下的特征值数量
    spy.imshow(data=pc.cov,title="pc_cov")
    img_pc = pc_098.transform(img)    # 把数据转换成主成分空间
    spy.imshow(img_pc[:,:,:3],stretch_all=True)    # 前三个主成分显示
    return img_pc    # img_pc仍然是numpy数组,形状为（1057,960,16）

img_pca = pca_dr(formatImage)


view1 = spy.imshow(data=formatImage, bands=[76, 46, 25], title="img")  # 图像显示
view2 = spy.imshow(data=img_pca, bands=[15, 10, 5], title="img_pca")  # 图像显示
# # spy.view_cube(formatImage, bands=[76, 46, 25])  # 显示后会打印相应功能及操作
# # unsupervised_demo(formatImage)
plt.pause(180)