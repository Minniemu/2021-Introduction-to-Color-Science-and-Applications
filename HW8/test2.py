from PIL import Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave

# load image
im_original = array(Image.open("cat_enc.jpg"))
im = array(Image.open("cat_enc.jpg"))
N = im.shape[0]

# create x and y components of Arnold's cat mapping
y,x = meshgrid(range(N),range(N))
xmap = (2*x-y) % N
ymap = (y-x) % N
period = 1
for i in range(20):
    result = Image.fromarray(im)
    im = im[xmap,ymap]
    print("i = ",i)
    '''comparison = im_original == im
                equal_arrays = comparison.all()'''
    
result.save("cat_dec.jpg")
print("period",period)