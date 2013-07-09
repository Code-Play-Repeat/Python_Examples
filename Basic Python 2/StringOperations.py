#a
s = '  remote sensing  '
s1 = s.__len__()
print (s1)

#b
s = '  remote sensing  '
s2 = s.strip(' ')
print (s2)

#c
s = '  remote sensing '
s2 = s.strip(' ')
s3 = s2.split(' ', 2)
print (s3)

#d
s = '  remote sensing '
s4 = s.swapcase()
print (s4)
