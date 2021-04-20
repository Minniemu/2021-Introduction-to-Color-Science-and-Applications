from PIL import Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave
write_file = open("ART-DEC-output08.txt","w")
read_file = open("ART-DEC-input08.txt","r",encoding = "utf-8")
lines = read_file.read().splitlines()
output_file_name = [ln.split('_')[1].split(' ')[0] for ln in lines]
lst = [ln.split(' ')[0] for ln in lines]
lst2 = [ln.split(' ')[1] for ln in lines]
lst3 = [ln.split(' ')[2] for ln in lines]
print("lst = ",lst)
print("lst2 = ",lst2)
print("lst3 = ",lst3)
for i in range(len(lst)):
    print("file",i)
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
    for j in range(int(lst3[i])+1):
        result = Image.fromarray(im)
        im = im[xmap,ymap]
    file_name = str(output_file_name[i])
    print(file_name)
    result.save(file_name)    
    line = output_file_name[i]

    write_file.write(line)   
    write_file.write('\n')         
