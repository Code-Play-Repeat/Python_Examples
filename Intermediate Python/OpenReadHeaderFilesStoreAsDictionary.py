import numpy as np
rf = open('raster.hdr')
rDict = {}

for line in rf:
    line = line.strip('\n')
    line = line.split()
    rDict [line[0]] = line[-1]
rf.close()

if (rDict['PIXELTYPE'] == 'FLOAT'):
    arr = np.empty((int(rDict['NROWS']), int(rDict['NCOLS'])),np.float32)
elif (rDict['PIXELTYPE'] == 'INT'):
    arr = np.empty((int(rDict['NROWS']), int(rDict['NCOLS'])),np.int)
print (arr.shape)
