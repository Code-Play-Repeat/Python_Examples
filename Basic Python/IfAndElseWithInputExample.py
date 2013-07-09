print ("Please input a slope:")
u_in = input()
inputSlope= int(u_in)
if inputSlope >= 360:
 rstType = "Nice Spin"
elif inputSlope == 180:
    rstType = "180 Flip"
elif inputSlope >= 45:
    rstType = "Steep Slope"
elif inputSlope >= 10:
    rstType = "Moderate Slope"
elif inputSlope > 0:
    rstType = "Gentle Slope"
elif inputSlope == 0:
    rstType = "No Slope"
elif inputSlope < 0:
    rstType = "Negative Slope"
print (rstType)
