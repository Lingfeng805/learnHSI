import numpy as np
import matplotlib.pyplot as plt
import spectral as spy
from scipy.io import savemat

def ReadRaw(filename,rows,cols,bands):
    """
    从Raw文件中读取HSI数据，形成3D数据立方体。
    Usage
        data3d=ReadRaw(filename)
    Inputs
        filename - Raw格式文件路径
    Outputs
        data3d - 3d data cube
    """
    rawRef = np.fromfile(filename,'float32')   # 将Raw文件转换成numpy数组
    # rawShape = rawRef.shape    # 获取元素总数
    hsi3D = np.zeros((rows,cols,bands))
    for row in range(0, rows):
        for dim in range(0, bands):
            hsi3D[row, :, dim] = rawRef[((dim + row * bands) * cols):((dim + 1 + row * bands) * cols)]
            pass
        pass
    return hsi3D

def hyperconvert2d(data3d):
    """
        Hyperconvert2d Convets an HSI cube to a 2D matrix
        Converts a 3D HSI cube to a 2D matrix of points
        Usage
            data3d = hyperconvert2d(data2d)
        Inputs
            inputdata - 3D HSI cube
        Outputs
            outputdata - 2D data matrix
    """
    rows, cols, channels = data3d.shape
    data2d = data3d.reshape(rows * cols, channels, order='F')
    return data2d.transpose()

def Transformtomat(hsi2D,d):
    hsimat = savemat("hsi2D.mat",{'X':hsi2D,'d':d})
    return hsimat