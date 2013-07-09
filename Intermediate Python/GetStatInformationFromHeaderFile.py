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

        #get the no data value
        noData = numpy.float32(hdr['NODATA'])
        
        #create a masked array to exclude no data values
        marr = numpy.ma.masked_equal(arr,noData)
        #get stats

        mean = marr.mean()
        maximum = marr.max()
        minimum = marr.min()
        std_dev = marr.std()

        return [minimum, maximum, mean, std_dev]

hdr=[]
rf = open('raster.hdr','r')
bf = open('raster.bip','rb')
arr = numpy.fromfile(bf, numpy.float32)

hdr = read_hdr(rf)
print (stats(arr,hdr))
print (arr.shape)
print (hdr)

rf.close()
bf.close()
