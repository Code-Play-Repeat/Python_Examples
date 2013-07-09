import math

sum_odd =  0
i = 1
while i <= 99:
    sum_odd += (2*i + 1)
    i += 1
print (sum_odd)

avg_odd = sum_odd / 50

print (avg_odd)

squared_diff = 0
i = 1
while i <= 99:
    squared_diff += (avg_odd - (2*i + 1))**2
    i += 1

variance = squared_diff / 50

print (variance)


std = math.sqrt(variance)
print (std)
