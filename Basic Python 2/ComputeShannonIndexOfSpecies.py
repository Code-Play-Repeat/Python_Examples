import numpy as np
# part B
def get_SI(arr):
    N = 0.0
    H = 0.0
    for i in range (0,len(arr)):
        N = N + float(arr[i])
    for i in range(0,len(arr)):
        H = H + ((arr[i]/N) * np.log(arr[i]/N))
    return (-H)
  
# part A
rf = open ('Species.csv')
header = rf.readline().split(',')
inNum = np.empty((6),int)
numList = []
for num in rf:
    num = num.split(',')
    numList.append(int(num[1]))
rf.close()
m = 0
n = 0

for i in range(0,6):
    inNum[i] = int(numList[i])
arr = np.array([10,20,40])

print (get_SI(arr))
