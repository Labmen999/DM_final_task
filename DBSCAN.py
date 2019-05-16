import numpy as np
from random import choice
from sklearn import metrics

# 获取txt文件中的数据集，并将属性与标签分开
def get_dataset():
    data = np.loadtxt('./breast.txt')
    label = data[:,-1]
    data = np.delete(data,-1,axis=1)
    return data,label


# 获取两点之间的欧式距离
def get_distance(p1,p2):
    dist = np.linalg.norm(p1-p2)
    return dist


# 获取一个的点的领域子样本集合
def get_neighbourhoodset(index):
    neighSet = []
    for i in range(len(data)):
        if index == i:
            continue
        if get_distance(data[index], data[i]) < maxRange:
            neighSet.append(i)
    return neighSet


maxRange = 5.2  # 参数，邻域的范围
minPts = 301 # 参数，成为核心对象的最小子样本个数
data, labels_true = get_dataset()
neighsetList = []  # 各个点的邻域子对象集合的集合
coreObjList = []  # 核心对象样本集合
unvisitedSet = list(range(len(data))) # 初始化未访问集合为整个数据集
clusterList = [] # 聚类得到的簇列表

# 遍历数据集，得到所有点的领域子对象的集合，并得到核心对象集合
for i in range(len(data)):
    neighset = get_neighbourhoodset(i)
    neighsetList.append(neighset)
    if len(neighset)>=minPts:
        coreObjList.append(i)

while len(coreObjList) != 0:
    # 每一轮循环将要进行的初始化工作
    curCluster = []  # 当前簇样本集合
    curClusterCore = []  # 当前簇核心对象集合
    core = choice(coreObjList)  # 随机选取一个核心对象
    curCluster.append(core)  # 将该核心对象加入到当前簇列表当中
    curClusterCore.append(core)  # 将该核心对象加入到当前簇核心对象集合当中
    unvisitedSet.remove(core)   # 从未访问的集合中将该对象移除

    # 遍历当前簇核心对象集合，找到每一个密度可达点
    while len(curClusterCore) != 0:
        _core = curClusterCore[0]  # 从当前簇核心对象中选取一个作为当前核心对象
        _set = list(set(neighsetList[_core]).intersection(set(unvisitedSet)))  # 取出当前核心对象的未被访问的密度直达点
        curCluster = list(set(curCluster).union(set(_set)))  # 将上一步找到的点加入到当前簇样本集合当中
        unvisitedSet = list(set(unvisitedSet).difference(set(_set)))  # 将找到的点从未访问点集中移除
        curClusterCore = list((set(curClusterCore).union(set(_set).intersection(set(coreObjList)))).difference(set([_core])))  # 将找到的点中的核心点加入到当前核心样本集合当中
    clusterList.append(curCluster)
    coreObjList = list(set(coreObjList).difference(set(curCluster)))

labels_pred = [0 for n in range(len(data))]
for i in clusterList[0]:
    labels_pred[i] = 1
np.savetxt('labelsPRED.txt',labels_pred)
NMI = metrics.adjusted_mutual_info_score(labels_true, labels_pred)
print(NMI)




