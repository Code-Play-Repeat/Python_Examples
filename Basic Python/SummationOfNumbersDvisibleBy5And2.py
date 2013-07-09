sum_int = 0
i = 1
while i <=100:
    if (i % 2 != 0):
        sum_int += i
    elif(i % 5 != 0):
        sum_int += i
    i+=1

print (sum_int)
