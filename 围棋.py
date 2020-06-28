import copy
def printqp():
    for i in range(19):
        print(z[i],"\n")
def wj1():
    print("轮到玩家1")    
    x=int(input("请输入横坐标"))-1
    y=int(input("请输入纵坐标"))-1
    z[x][y]=1
    w=2
def wj2():
    print("轮到玩家2")    
    x=int(input("请输入横坐标"))-1
    y=int(input("请输入纵坐标"))-1
    z[x][y]=2
    w=1
a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
z=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(19):
    z[i]=copy.copy(a)
printqp()
w=1
while(1):
    wj1()
    printqp()
    wj2()
    printqp()

