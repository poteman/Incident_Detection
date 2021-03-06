# -*- coding: UTF-8 -*-
# 需要导入的库：
import csv
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

####################################################################################
# 特征值读取
# featureList
allElectronicsData=open(r'F:\TrafficFlow\pems\7606\7606bu.csv','rb')#****bu.csv特征值文件
reader=csv.reader(allElectronicsData)
headers=reader.next()
temp1=[]
# temp2=[]
for row in reader:
    c1=[]
    c2=[]
    for i in range(1,9):#读取第2列到第9列
        b=0
        b=float(row[i])-float(row[i+8])
        c1.append(b)
    temp1.append(c1)
    # for i in range(9,17):#读取第10列到第16列
    #     b=0
    #     b=float(row[i])
    #     c2.append(b)
    # temp2.append(c2)
# print("temp1:")
# print(temp1)

# print("temp2:")
# print(temp2)
n=len(temp1)
# print(n)
featureList1=[]
for i in range(0,n-4):
    k1=[]
    k1=temp1[i]
    k2=temp1[i+1]
    k3=temp1[i+2]
    k4=temp1[i+3]
    k5=temp1[i+4]

    k1.extend(k2)
    k1.extend(k3)
    k1.extend(k4)
    k1.extend(k5)

    featureList1.append(k1)
featureList1=np.array(featureList1)
# print("featureList1:")
# temp1=np.array(temp1)
# print(featureList1.shape)
# print(len(featureList))
# print("temp2:")
# temp2=np.array(temp2)
# print(temp2)
# featureList=temp1-temp2

# print(featureList.shape)

# f=open('featurelist.txt','w')
# f.write(str(featureList))
# f.close()


####################################################################################
# 特征值读取
# featureList
allElectronicsData=open(r'F:\TrafficFlow\pems\6080\6080bu.csv','rb')#****bu.csv特征值文件
reader=csv.reader(allElectronicsData)
headers=reader.next()
temp1=[]
# temp2=[]
for row in reader:
    c1=[]
    c2=[]
    for i in range(1,9):#读取第2列到第9列
        b=0
        b=float(row[i])-float(row[i+8])
        c1.append(b)
    temp1.append(c1)
    # for i in range(9,17):#读取第10列到第16列
    #     b=0
    #     b=float(row[i])
    #     c2.append(b)
    # temp2.append(c2)
# print("temp1:")
# print(temp1)

# print("temp2:")
# print(temp2)
n=len(temp1)
# print(n)
featureList2=[]
for i in range(0,n-4):
    k1=[]
    k1=temp1[i]
    k2=temp1[i+1]
    k3=temp1[i+2]
    k4=temp1[i+3]
    k5=temp1[i+4]

    k1.extend(k2)
    k1.extend(k3)
    k1.extend(k4)
    k1.extend(k5)

    featureList2.append(k1)
featureList2=np.array(featureList2)
# print("featureList2:")
# temp1=np.array(temp1)
# print(featureList2.shape)
# print(len(featureList))
# print("temp2:")
# temp2=np.array(temp2)
# print(temp2)
# featureList=temp1-temp2

# print(featureList.shape)

# f=open('featurelist.txt','w')
# f.write(str(featureList))
# f.close()
featureList=np.vstack((featureList1,featureList2))
# print(featureList.shape)

##########################################################################################
# 标签读取
# labelList
incidentData=open(r'F:\TrafficFlow\pems\7606\7606label.csv','rb')#****label.csv标签文件
label=csv.reader(incidentData)
headers=label.next()
# print(headers)
labelList1=[]
for row in label:
    labelList1.append(row[len(row)-1])
    # print(row[len(row)-1])
# print(labelList1)
lb=preprocessing.LabelBinarizer()
dummyY1=lb.fit_transform(labelList1)
# dummyY=np.array(dummyY)
# print(dummyY)
# print(len(dummyY))
# print("dummyY:"+str(dummyY1))



##########################################################################################
# 标签读取
# labelList
incidentData=open(r'F:\TrafficFlow\pems\6080\6080label.csv','rb')#****label.csv标签文件
label=csv.reader(incidentData)
headers=label.next()
# print(headers)
labelList2=[]
for row in label:
    labelList2.append(row[len(row)-1])
# print(labelList)
lb=preprocessing.LabelBinarizer()
dummyY2=lb.fit_transform(labelList2)
# dummyY=np.array(dummyY)
# print(dummyY)
# print(len(dummyY))
# print("dummyY:"+str(dummyY))
dummyY=np.vstack((dummyY1,dummyY2))

# print(dummyY.shape)

# 将数据拆分成训练样本和测试样本：
X_train, X_test, y_train, y_test = train_test_split(featureList, dummyY, test_size=0.1)

# 训练模型：
print("Fitting the classifier to the training set---->")
clf=SVC(kernel='rbf',C=1e3,gamma=0.001)
clf.fit(X_train,y_train)
########################################################


####################################################
# 测试模型过程
print("Road 1 ---------->")
predictions=[]
for x in range(len(X_test)):
    result=clf.predict(X_test[x])
    predictions.append(result)
    print('>predicted= '+repr(result)+',actual='+repr(y_test[x][-1]))

# 模型矩阵
y_pred = clf.predict(X_test)
conm=confusion_matrix(y_test, y_pred, labels=range(2))
print(conm)

# 准确率：
a=float(conm[0][0])
b=float(conm[0][1])
c=float(conm[1][0])
d=float(conm[1][1])

DR=(a/(a+c))
DR=DR*100

FAR=(b/(a+b))
FAR=FAR*100
print('Detection rate: '+repr(DR)+'%')
print('False alarm rate: '+repr(FAR)+'%')
# print(accuracy)
############################################################

# Road Two

####################################################################################
# 特征值读取
# featureList
allElectronicsData=open(r'F:\TrafficFlow\pems\3245\3245bu.csv','rb')#****bu.csv特征值文件
reader=csv.reader(allElectronicsData)
headers=reader.next()
temp1=[]
# temp2=[]
for row in reader:
    c1=[]
    c2=[]
    for i in range(1,9):#读取第2列到第9列
        b=0
        b=float(row[i])-float(row[i+8])
        c1.append(b)
    temp1.append(c1)
    # for i in range(9,17):#读取第10列到第16列
    #     b=0
    #     b=float(row[i])
    #     c2.append(b)
    # temp2.append(c2)
# print("temp1:")
# print(temp1)

# print("temp2:")
# print(temp2)
n=len(temp1)
# print(n)
featureList1=[]
for i in range(0,n-4):
    k1=[]
    k1=temp1[i]
    k2=temp1[i+1]
    k3=temp1[i+2]
    k4=temp1[i+3]
    k5=temp1[i+4]

    k1.extend(k2)
    k1.extend(k3)
    k1.extend(k4)
    k1.extend(k5)

    featureList1.append(k1)
featureList1=np.array(featureList1)
# print("featureList1:")
# temp1=np.array(temp1)
# print(featureList1.shape)
# print(len(featureList))
# print("temp2:")
# temp2=np.array(temp2)
# print(temp2)
# featureList=temp1-temp2

# print(featureList.shape)

# f=open('featurelist.txt','w')
# f.write(str(featureList))
# f.close()


####################################################################################
# 特征值读取
# featureList
allElectronicsData=open(r'F:\TrafficFlow\pems\6080\6080bu.csv','rb')#****bu.csv特征值文件
reader=csv.reader(allElectronicsData)
headers=reader.next()
temp1=[]
# temp2=[]
for row in reader:
    c1=[]
    c2=[]
    for i in range(1,9):#读取第2列到第9列
        b=0
        b=float(row[i])-float(row[i+8])
        c1.append(b)
    temp1.append(c1)
    # for i in range(9,17):#读取第10列到第16列
    #     b=0
    #     b=float(row[i])
    #     c2.append(b)
    # temp2.append(c2)
# print("temp1:")
# print(temp1)

# print("temp2:")
# print(temp2)
n=len(temp1)
# print(n)
featureList2=[]
for i in range(0,n-4):
    k1=[]
    k1=temp1[i]
    k2=temp1[i+1]
    k3=temp1[i+2]
    k4=temp1[i+3]
    k5=temp1[i+4]

    k1.extend(k2)
    k1.extend(k3)
    k1.extend(k4)
    k1.extend(k5)

    featureList2.append(k1)
featureList2=np.array(featureList2)
# print("featureList2:")
# temp1=np.array(temp1)
# print(featureList2.shape)
# print(len(featureList))
# print("temp2:")
# temp2=np.array(temp2)
# print(temp2)
# featureList=temp1-temp2

# print(featureList.shape)

# f=open('featurelist.txt','w')
# f.write(str(featureList))
# f.close()
featureList=np.vstack((featureList1,featureList2))
# print(featureList.shape)

##########################################################################################
# 标签读取
# labelList
incidentData=open(r'F:\TrafficFlow\pems\3245\3245label.csv','rb')#****label.csv标签文件
label=csv.reader(incidentData)
headers=label.next()
# print(headers)
labelList1=[]
for row in label:
    labelList1.append(row[len(row)-1])
# print(labelList)
lb=preprocessing.LabelBinarizer()
dummyY1=lb.fit_transform(labelList1)
# dummyY=np.array(dummyY)
# print(dummyY)
# print(len(dummyY))
# print("dummyY:"+str(dummyY))



##########################################################################################
# 标签读取
# labelList
incidentData=open(r'F:\TrafficFlow\pems\6080\6080label.csv','rb')#****label.csv标签文件
label=csv.reader(incidentData)
headers=label.next()
# print(headers)
labelList2=[]
for row in label:
    labelList2.append(row[len(row)-1])
# print(labelList)
lb=preprocessing.LabelBinarizer()
dummyY2=lb.fit_transform(labelList2)
# dummyY=np.array(dummyY)
# print(dummyY)
# print(len(dummyY))
# print("dummyY:"+str(dummyY))
dummyY=np.vstack((dummyY1,dummyY2))

# print(dummyY.shape)

# 将数据拆分成训练样本和测试样本：
X_train, X_test, y_train, y_test = train_test_split(featureList, dummyY, test_size=0.1)

# 训练模型：
print("Fitting the classifier to the training set---->")
clf=SVC(kernel='rbf',C=1e3,gamma=0.001)
clf.fit(X_train,y_train)
########################################################


####################################################
# 测试模型过程
print("Road 2 ---------->")
predictions=[]
for x in range(len(X_test)):
    result=clf.predict(X_test[x])
    predictions.append(result)
    print('>predicted= '+repr(result)+',actual='+repr(y_test[x][-1]))

# 模型矩阵
y_pred = clf.predict(X_test)
conm=confusion_matrix(y_test, y_pred, labels=range(2))
print(conm)

# 准确率：
a=float(conm[0][0])
b=float(conm[0][1])
c=float(conm[1][0])
d=float(conm[1][1])

DR=(a/(a+c))
DR=DR*100

FAR=(b/(a+b))
FAR=FAR*100
print('Detection rate: '+repr(DR)+'%')
print('False alarm rate: '+repr(FAR)+'%')
# print(accuracy)
############################################################
