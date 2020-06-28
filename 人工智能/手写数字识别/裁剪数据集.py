file = open('mnist_test.csv')
fileList = file.readlines()
file.close

file = open('mnist_test_10.csv',mode='w')
for i in range(10):
    file.writelines(fileList[i])

exit()
