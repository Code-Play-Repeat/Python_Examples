import math
import numpy

def read_hdr(rf):

    rDict={}
    
    for line in rf:
        line = line.strip('\n')
        line = line.split(' ')
        rDict[line[0]] = line[-1]
       
    return rDict
def stats(arr, hdr):

        noData = numpy.float32(hdr['NODATA'])
        
        marr = numpy.ma.masked_equal(arr,noData)
        
        mean = marr.mean()
        maximum = marr.max()
        minimum = marr.min()
        std_dev = marr.std()

        return [minimum, maximum, mean, std_dev]
    
def write_hdr(d):
    hf = open ('raster_stat1.hdr','w')
    for i in d.keys():
        hf.write(i + '  ' + d[i] + '\n')
    hf.close()
    return hf

hdr = {}
s = []

rf = open('raster.hdr','r')
bf = open('raster.bip','rb')
bw = open('raster_stat1.bip','wb')

arr = numpy.fromfile(bf,dtype = numpy.float32)
hdr = read_hdr(rf)
s = stats(arr,hdr)
ncols = hdr['NCOLS']
nrows = hdr['NROWS']
arr.shape = (int(nrows),int(ncols))
arr.transpose()
print (arr)

newarr =  numpy.empty([int(nrows),int(ncols)],dtype=numpy.float32) 
rf.close()
bf.close()
avg = s[2]
maxi = s[1]
mini = s[0]
noData = numpy.float32(hdr['NODATA'])

for x in range (0, int(nrows),1):
    for y in range (0, int(ncols), 1):
        if (arr[x][y] == noData):
            newarr[x][y] = noData

        if(arr[x][y] > avg):
            newarr[x][y] = ((arr[x][y]-avg)/(maxi - avg))
        elif( arr[x][y] < avg or arr[x][y] == avg):
        
            newarr[x][y] = ((arr[x][y]-avg)/(avg - mini))
        
            

newarr.ravel()
newarr.tofile(bw)
write_hdr(hdr)

bw.close()
