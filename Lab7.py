import matplotlib.pyplot as plt
import numpy as np
import urllib.request

def grayscale(filename):
    img = plt.imread(filename)
    plt.imshow( img )
    img[:,:,0]=1-img[:,:,0]
    img[:,:,1]=1-img[:,:,1]
    img[:,:,2]=1-img[:,:,2]
    imgCopy = np.copy(img)
    imgCopy[:,:,0]=0.229*img[:,:,0]+0.587*img[:,:,1]+0.114*img[:,:,2]
    imgCopy[:,:,1]=0.229*img[:,:,0]+0.587*img[:,:,1]+0.114*img[:,:,2]
    imgCopy[:,:,2]=0.229*img[:,:,0]+0.587*img[:,:,1]+0.114*img[:,:,2]
    plt.imshow( imgCopy )
    plt.title('Grayscale')
    plt.show()



def magnify(filename):
    img3d = plt.imread( filename)
    img3d.crop( (0,125,200,200))
plt.subplot(2,1,1)
plt.title ('Orignal')
imgOrig = plt.imread('gwinn-commons.png')
plt.imshow( imgOrig )
plt.subplot(2,1,2)
plt.title ('Magnification')
zoom = plt.imread('gwinn-commons.png')
plt.imshow(zoom[0:125,0:200],interpolation='nearest' )
plt.show()


def getMaxMinTemp(year,month,day):
    url = 'http://www.atmos.washington.edu/climate/clisea/'+str(year)+str(month)+str(day)+'.clisea'
    page = urllib.request.urlopen( url )
    rawBytes = page.read()
    chars = rawBytes.decode()
    lines = chars.split('\n')
    for line in lines:
        if 'MAXIMUM TEMPERATURE' in line:
            maxTemp = line.split()[3]
        if 'MINIMUM TEMPERATURE' in line:
            minTemp = line.split()[3]
    print(minTemp, maxTemp)
        
    
    
    
    
    
