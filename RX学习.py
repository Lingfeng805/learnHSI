import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.stats import chi2
import spectral as spy

img = loadmat('./data/Salinas_corrected.mat')['salinas_corrected']
gt = loadmat("./data/Salinas_gt.mat")['salinas_gt']

# RX异常检测器使用平方马氏距离作为像素相对于假定背景的异常程度的度量。SPy.rx（）函数计算图像像素矩阵的rx分数。
# 如果没有背景统计信息被传递给rx函数，背景统计信息将从要计算RX分数的像素矩阵中进行估计。
rxvals = spy.rx(img)

# 要将像素声明为异常，我们需要指定一个阈值RX分数，例如，可以选择相对于背景而言RX分数小于0.001的所有图像像素；
nbands = img.shape[-1]
P = chi2.ppf(0.999, nbands)   # P作为阈值
view1 = spy.imshow(img,(29,19,9),title='Picture')    # 原图
view2 = spy.imshow(1 * (rxvals > P),title='rxvals>P')    # 将像素中大于P=272的部分作为异常显示出来

# 除了为异常像素指定阈值，还可以简单地查看原始RX分数的图像，其中较亮的像素被认为是“更异常的”
view3 = spy.imshow(rxvals,title='rxvals')

# 对于样本图像，在RX分数的图像中只有几个像素的是可见的，因为使用了线性色标，且只有极少数像素的RX分数比其他像素高的多，从RX分数的直方图可以明显看出这一点。
f = plt.figure(num='RX直方图')    # 新建画布
h = plt.hist(rxvals.ravel(), 200, log=True)    # rxvals.ravel()返回一维数组，将rxvals中所有元素按顺序展开为一维数据；
h = plt.grid()    # 添加网格线
# 异常值在直方图中并不明显，打印它们的值如下：
print(np.sort(rxvals.ravel())[-10:])    # 打印排在后10个异常值
# 为了查看RX图像中的更多细节，我们可以调整图像显示的下限和上限。由于我们主要对最异常的像素感兴趣，因此我们将把黑色级别设置为RX值累积直方图的第99个百分位，并把白点设置为第99.99个百分位：
view4 = spy.imshow(rxvals, stretch=(0.99, 0.9999))    # 即rxvals元素按顺序排列后分成100分，其中排在前99%的元素显示成黑色，排在99.99及之后的显示白色。

'''
为了计算每个像素的本地背景统计信息，rx函数接受一个可选的窗口参数，该参数指定一个内/外窗口，在该窗口内计算每个被评估像素的背景统计信息。外部窗口是计算背景统计信息的窗口。
内部窗口是一个较小的窗口（在外部窗口内），指示要忽略像素的排除区。内部窗口的目的是防止潜在的异常/目标像素“污染”背景统计数据。
例如，要使用从21×21像素窗口计算的关于被评估像素的背景统计信息计算RX分数，使用5×5像素的排除窗口，函数调用如下：
'''
rxvalsNew = spy.rx(img, window=(5,21))    # 局部窗口背景
# view5 = spy.imshow(1*(rxvalsNew > P),title='window')
# print(rxvalsNew)
'''
虽然使用窗口背景通常会改善包含多个背景材质的图像的效果，但这样做的代价是引入两个问题。首先，必须指定内窗口和外窗口的大小，以便得到的协方差具有满秩。
也就是说，如果w{in}和w{out}分别表示内窗口和外窗口的像素宽度，那么w{out}^2-w{in}^2必须至少与图像带的数量一样大。
其次，重新计算图像中每个像素的估计背景协方差使得magnitue的RX分数计算阶数的计算复杂度更大。
作为固定背景和重新计算每个像素的平均值和协方差之间的折衷，除了窗口参数外，rx还可以传递全局协方差估计。在这种情况下，仅对每个像素重新计算窗口内的背景平均值。
这大大减少了加窗算法的计算时间，并消除了窗口的大小限制（外部窗口必须大于内部窗口除外）。
例如，由于我们的样本图像标记了地面覆盖物类别，因此我们可以计算这些地面覆盖物类别的平均协方差，并将结果用作全局协方差的估计。
'''
# C = spy.cov_avg(img, gt)    # 计算已标记的样本图像的平均协方差；
# rxvalsCpv = spy.rx(img, window=(5,21), cov=C)
# view6 = spy.imshow(1*(rxvalsCpv > P),title='Cov')

plt.pause(60)
