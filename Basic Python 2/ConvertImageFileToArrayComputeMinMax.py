import numpy as np
import re
rf = open ('Image.asc', 'r')
size = rf.readline()
size = re.split('[^0-9]*', size)
size.pop(-1) # the split splits it into 4 elements 2 are empty space
size.pop(0)  # these pops are to remove these extra elements so only the dimensions are left
x = int(size[0])
y = int(size[1])
myArr = np.empty((y,x),int) #create an empty 2-dimensional int array of length 50
numList = []
for num in rf:
    num  = num.split()
    numList.append(num)
rf.close()

m = 0
n = 0
for i in range(0,y):
    for j in range (0,x):
        myArr[i][j] = int(numList[i][j])
print (myArr)
print (np.max(myArr))
print (np.min(myArr))
