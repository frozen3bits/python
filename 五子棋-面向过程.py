import copy

def printqp():
    print('  ',1,' ',2,' ',3,' ',4,' ',5,' ',6,' ',7,' ',8,' ',9,' ',10,'',11,'',12,'',13,'',14,'',15)
    for i in range(15):
        if(i<9):
            print('',i+1,'',end='')
        else:
            print(i+1,'',end='')
        for j in range(15):
            print(z[i][j],end='   ')
        print("\n")
        
def wj1():
    print("轮到玩家1")    
    x=int(input("请输入横坐标"))-1
    y=int(input("请输入纵坐标"))-1
    z[x][y]='O'
    w=2
def wj2():
    print("轮到玩家2")    
    x=int(input("请输入横坐标"))-1
    y=int(input("请输入纵坐标"))-1
    z[x][y]='X'
    w=1
#def win(x,y):
 #   if(x<=4):
        
a=['+','+','+','+','+','+','+','+','+','+','+','+','+','+','+']
z=['+','+','+','+','+','+','+','+','+','+','+','+','+','+','+']
for i in range(15):
    z[i]=copy.copy(a)
printqp()
w=1
while(1):
    wj1()
    printqp()
    wj2()
    printqp()
