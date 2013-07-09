flag1 = True
flag2 = False
results1 = flag1 and flag1 # True
results2 = flag2 and flag2 # False
results3 = flag1 or flag1  # True
results4 = flag2 or flag2  #False
results5 = flag1 or flag2  # True
results6 = not(flag2) and flag2 # False
results7 = not (flag2 and flag2) # True
results8 = not( flag1) or flag2 # False
results9 = flag1 and flag1 or flag2 # True
results10 = not( flag2) or flag1 and flag2 # True
print (results1)
print (results2)
print (results3)
print (results4)
print (results5)
print (results6)
print (results7)
print (results8)
print (results9)
print (results10)
