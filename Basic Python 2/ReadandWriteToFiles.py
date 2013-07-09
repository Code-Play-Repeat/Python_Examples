results = [] #initialize an empty list
Transect = [] # another empty list
rf = open('Transect.csv','r')
header = rf.readline().split('\n',3) #reads the first line of the file as a header

# part A
sum_density = 0
for i in range(0,128):
    line = rf.readline() #read one line in file
    line = line.rsplit (',', 2)
    results.append(line[1])
for i in range(0,128):
    sum_density += int( results[i])
    

avg_density = sum_density/128

# part B writing to Patch_Gap file
# setup for part B
wf = open('Patch_Gap.csv','w')
wf.write (header[0] + ',Patch_Gap\n')

position = rf.seek(0,0)
header = rf.readline().split('\n',3)
for i in range(0,128):
    line = rf.readline().split('\n',3)
    if int(results[i]) >= avg_density: 
        wf.write(line[0] + ',1\n') 
    else:
        wf.write(line[0] + ',0\n')
rf.close()
wf.close()

