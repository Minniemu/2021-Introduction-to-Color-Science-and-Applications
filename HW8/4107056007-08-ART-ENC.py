from PIL import Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave
read_file = open("ART-ENC-input08.txt","r")
write_file = open("ART-ENC-output08.txt","w")
lines = read_file.read().splitlines()
lst = [ln.split(' ')[0] for ln in lines]
lst2 = [ln.split(' ')[1] for ln in lines]
lst3 = [ln.split(' ')[2] for ln in lines]
#print("lst = ",lst)
#print("lst2 = ",lst2)
#print("lst3 = ",lst3)
period = [0,0,0,0,0]
for i in range(len(lst)):
    #print("file",i)
    im_original = array(Image.open(str(lst[i]))) 
    im = array(Image.open(str(lst[i])))   
    N = im.shape[0]
    y,x = meshgrid(range(N),range(N))
    if str(lst2[i]) == '+':
        xmap = (x+y) % N
        ymap = (x+2*y) % N
    else:
        xmap = (2*x-y) % N
        ymap = (y-x) % N
    for j in range(N+1):
        result = Image.fromarray(im)
        im = im[xmap,ymap]
        if j == int(lst3[i]):
            file_name = "ART" + str(lst2[i]) + str(lst3[i]) + "_" + str(lst[i])
            print(file_name)
            result.save(str(file_name)) 

        if (im == im_original).all():
            #print("i",i)
            period[i] = j+1
            break
    line = file_name + str(lst2[i]) + " " + str(lst3[i]) + " " + str(period[i])

    write_file.write(line)   
    write_file.write('\n')         
