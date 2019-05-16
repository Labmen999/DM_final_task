import numpy as np
import matplotlib.pyplot as plt


# 获取txt文件中的数据集，并将属性与标签分开
def get_dataset():
    data = np.loadtxt('./breast.txt')
    label = data[:,-1]
    data = np.delete(data,-1,axis=1)
    return data,label


def get_distance(p1,p2):
    dist = np.sqrt(np.sum(np.square(p1 - p2)))
    return dist


def get_distance_matrix(dataset):
    dist_matrix = []
    for i in range(len(dataset)):
        dist_list = []
        for j in range(len(dataset)):
            if i != j:
                dist_list.append(get_distance(dataset[i], dataset[j]))
        dist_list.sort()
        dist_matrix.append(dist_list)
    return np.array(dist_matrix)


def draw_scatter_diagram(datalist):
    sorted_datalist =np.sort(datalist)
    tmp = np.argsort(datalist)
    colors = ['r','g']
    plt.figure()
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(len(datalist)):
        plt.scatter(i,sorted_datalist[i],c=colors[int(label[tmp[i]]/2-1)])
    plt.show()


# 观察k距离的矩阵得到k值
k = 300
data, label = get_dataset()
matrix = get_distance_matrix(data)
draw_scatter_diagram(matrix[:,k-1])