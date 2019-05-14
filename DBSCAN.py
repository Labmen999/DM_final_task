import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics


# 获取txt文件中的数据集，并将属性与标签分开
def get_dataset():
    data = np.loadtxt('./breast.txt')
    label = data[:,-1]
    data = np.delete(data,-1,axis=1)
    return data,label


data, labels_true = get_dataset()
db = DBSCAN(eps=3.5, min_samples=120).fit(data)
labels_pred = db.labels_
labels_pred= np.where(labels_pred==-1,4.0,2.0)
NMI = metrics.adjusted_mutual_info_score(labels_true, labels_pred)
print(NMI)

