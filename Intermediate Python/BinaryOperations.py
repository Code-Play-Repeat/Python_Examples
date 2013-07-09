import numpy as np
# binary to decimal converter
def bin_to_dec (b):
    d = 0
    rank = 1
    for i in reverse_int(b):
        d+=rank*int(i)
        rank*=2
    return d

def reverse_int(n):
    return str(n)[::-1]

# example of binary to decimal conversion

print("Example of binary to decimal conversion")
print()
b = int(10101111)
print("Binary Value: ", b)
print("Result: ",(bin_to_dec(b)))


# bit size of four

def bitSize4(b):
    d = []
    bL = []
    temp = []
    bStr = str(b)
    for i in range (0, len(bStr),4):
        if ( i % 4 == 0):
            bL.append('\n')
        if (i  < (len(bStr) - 3)):
            bL.append(bStr[i] + bStr[i + 1] + bStr[i+2] + bStr[i+3])
    for i in bL:
        if i == '\n':
            bL.remove('\n')
    for i in range(0,len(bL)):
        d.append(bin_to_dec(bL[i]))
    return d

# example of values converted from a binary number with bitsize of 4
print()
print("Example of values converted from a binary number with bitsize of 4")
print()
b2 = int(101001101001)
print ("1010|0110|1001 = ", bitSize4(b2))

# Bit size of 2
def bitSize2(b):
    d = []
    bL = []
    temp = []
    bStr = str(b)
    for i in range (0, len(bStr),2):
        if ( i % 2 == 0):
            bL.append('\n')
        if (i  < (len(bStr) - 1)):
            bL.append(bStr[i] + bStr[i + 1] )
    for i in bL:
        if i == '\n':
            bL.remove('\n')
    for i in range(0,len(bL)):
        d.append(bin_to_dec(bL[i]))
    return d

# Creating a 2d array from list
def list2array2d(dL,rows,cols):
    arr = np.empty([rows,cols],int)
    i = 0
    for n in range (0,rows):
        for m in range (0,cols):
            arr[n][m] = dL[i]
            i+=1     
    return arr

# example of representing a binary number of bitsize 2 as a 2d array
print()
print ("Example of representing a binary number of bitsize 2 as a 2d array")
b3 = int(100110111001)
print()
print ("Binary Value: ", b3)
print ("2d Array: ")
print (list2array2d(bitSize2(b3),2,3))

# decimal to binary function
def dec_to_bin (d):
    bStr = ' '
    if d < 0:
        raise ValueError
    if d == 0:
        return '0'
    while (d > 0):
        bStr = str(d%2) + bStr
        d >>= 1
    return int(bStr)

# Example of converting a decimal number to a binary value
print()
print("Example of converting a decimal number to a binary value")
d5 = int(123456)
print()
print ("Decimal Value: ", d5)
print ("Result: ", dec_to_bin(d5))

