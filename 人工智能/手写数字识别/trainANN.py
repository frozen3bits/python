import numpy as np
import matplotlib.pyplot as plt
from  ANN import ANN

inode = 784
hnode = 100
onode = 10

lr = 0.2    #学习率

ann = ANN(inode, hnode, onode, lr)

dataFile = open('mnist_train.csv')
dataList = dataFile.readlines()
dataFile.close()

for record in dataList:
    recordx = record.split(',')
    inputT = (np.asfarray(recordx[1:])/255.0 * 0.99 + 0.01)
    train = np.zeros(onode) + 0.01
    train[int(recordx[0])] = 0.99
    #开始训练
    ann.trainNet(inputT,train)

testDataFile = open('mnist_test_10.csv')
testDataList = testDataFile.readlines()
testDataFile.close()

match = 0
no_match = 0
for record in testDataList:
    recordz = record.split(',')
    labelz = int(recordz[0])

    inputz = (np.asfarray(recordz[1:])/255.0 * 0.99) + 0.01
    outputz = ann.textNet(inputz)
    max_value = np.argmax(outputz)
    if max_value == labelz:
        match += 1
    else:
        no_match += 1
print('success match rate = ',float(match)/float(match + no_match))
#    print('output for label = ',labelz)
#    print(outputz)
