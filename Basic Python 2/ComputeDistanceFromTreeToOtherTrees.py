import math
import itertools
def distance (p0,p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

rf = open ('Points.csv', 'r')
header = rf.readline().split(',')
dlist = []
for line in rf:
    line = line.split(',',3)
    x,y = int(line[1]),int(line[2])
    dlist += [(x,y)]

distances = []
for p0, p1 in itertools.combinations(dlist,2):
    distances.append(distance(p0,p1))

print (distances)

rf.close()
