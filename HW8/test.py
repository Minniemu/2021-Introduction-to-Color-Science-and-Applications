from PIL import Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave

# load image
im_original = array(Image.open("Alschair-1000.bmp"))
im = array(Image.open("Alschair-1000.bmp"))
N = im.shape[0]

# create x and y components of Arnold's cat mapping
y,x = meshgrid(range(N),range(N))
xmap = (x+y) % N
ymap = (x+2*y) % N
period = 1
for i in range(20):
    result = Image.fromarray(im)
    im = im[xmap,ymap]
    print("i = ",i)
    '''comparison = im_original == im
                equal_arrays = comparison.all()'''
    
result.save("cat_enc.jpg")
print("period",period)