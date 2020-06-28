
#三层ANN类

import numpy as np

class ANN:
    def __init__(self, inode, hnode, onode, lr):#初始化输入、隐藏、输出节点数和学习率
        self.inode = inode
        self.onode = onode
        self.hnode = hnode
        self.lr = lr

        mean = 1/(pow((inode + hnode + onode), 0.5))   #总结点数平方根的倒数

        stdev = 0.333   #生成随机权重矩阵的标准差

        #生成输入到隐藏权重矩阵
        self.wtgih = np.random.normal(mean, stdev, [hnode, inode])
#        print('wtgih')
#        print(self.wtgih)
#        print('')

        # 生成隐藏到输出权重矩阵
        self.wtgho = np.random.normal(mean, stdev, [onode, hnode])
#        print('wtgho')
#        print(self.wtgho)
#        print('')

    def textNet(self, input):
        input = np.array(input, ndmin=2).T   #将输入转为向量

        hInput = np.dot(self.wtgih, input)   #相乘

        hOutput = 1/(1 + np.exp(-hInput))    #带入sigmoid函数

        oInput = np.dot(self.wtgho, hOutput)

        oOutput = 1/(1 + np.exp(-oInput))

        return oOutput

    def trainNet(self, inputT, train):
        self.inputT = np.array(inputT, ndmin=2).T
        self.train = np.array(train, ndmin=2).T

        self.hInputT = np.dot(self.wtgih, self.inputT)

        self.hOutputT = 1/(1 + np.exp(-self.hInputT))

        self.oInputT = np.dot(self.wtgho, self.hOutputT)

        self.oOutputT = 1 / (1 + np.exp(-self.oInputT))

        self.eOutput = self.train - self.oOutputT   #计算输出误差

        self.hError = np.dot(self.wtgho.T, self.eOutput)

        self.wtgho += self.lr * np.dot((self.eOutput * self.oOutputT * (1 - self.oOutputT)), self.hOutputT.T)
        self.wtgih += self.lr * np.dot((self.hError * self.hOutputT * (1 - self.hOutputT)), self.inputT.T)
#        print('updated wtgih')
 #       print(self.wtgih)
#        print('')
#        print('updated wtgho')
#        print(self.wtgho)
 #       print('')

