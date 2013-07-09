#2
def read_hdr(hf):
    rDict = {}
    for line in hf:
        line = line.strip('\n')
        line = line.split()
        rDict [line[0]] = line[-1]
    hf.close()
    return rDict


#3
def write_hdr(d):
    hf = open ('write_hdr.hdr','w')
    for i in d.keys():
        hf.write(i + '  ' + d[i] + '\n')
    hf.close()
    return hf

#3
rf = open('raster.hdr')
h = read_hdr(rf)
rf.close()
wf = write_hdr(h)
