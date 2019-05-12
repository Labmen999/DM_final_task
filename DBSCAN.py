import numpy as np
from random import choice

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
        if index==i:
            continue
        if(get_distance(data[index],data[i]) < maxRange ):
            neighSet.append(i)
    return neighSet


maxRange = 5 # 参数，邻域的范围
minPts = 30  # 参数，成为核心对象的最小子样本个数
data, label = get_dataset()
neighsetList = []  # 各个点的邻域子对象集合的集合
coreObjList = []  # 核心对象样本集合
unvisitedSet = list(range(len(data))) # 初始化未访问集合为整个数据集
clusterList = []

# 遍历数据集，得到所有点的领域子对象的集合，并得到核心对象集合
for i in range(len(data)):
    neighset = get_neighbourhoodset(i)
    neighsetList.append(neighset)
    if len(neighset)>=minPts:
        coreObjList.append(i)

while len(coreObjList)!=0:
    curCluster = []  # 当前簇样本集合
    curClusterCore = []  # 当前出核心对象集合
    core = choice(coreObjList)
    curCluster.append(core)
    curClusterCore.append(core)
    unvisitedSet.remove(core)
    while len(curClusterCore)!=0:
        _core = curClusterCore[0]
        _set = list(set(neighsetList[_core]).intersection(set(unvisitedSet)))
        curCluster = list(set(curCluster).union(set(_set)))
        unvisitedSet = list(set(unvisitedSet).difference(set(_set)))
        curClusterCore = list((set(curClusterCore).union(set(_set).intersection(set(coreObjList)))).difference(set([_core])))
    clusterList.append(curCluster)
    coreObjList = list(set(coreObjList).difference(set(curCluster)))

print(clusterList)




