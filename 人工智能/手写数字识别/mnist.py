import numpy as np
import matplotlib.pyplot as plt

dataFile = open("mnist_train_100.csv")
dataList = dataFile.readlines()
print(len(dataList))
dataFile.close()

record0 = dataList[0].split(',')           #0号样本以逗号为分割存入数组
#imageArray = np.asfarray(record0[1:]).reshape((28,28))      # 
#plt.imshow(imageArray, cmap='Greys', interpolation='None')  #显示28*28像素灰度图
#plt.show()                                                  #

onode = 10
train = np.zeros(onode) + 0.01
train[int(record0[0])] = 0.99
print(train)


