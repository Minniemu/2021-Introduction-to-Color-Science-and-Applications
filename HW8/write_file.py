from PIL import Image

read_file = open("ART-DEC-input08.txt","r",encoding="utf-8")
lines = read_file.read().splitlines()
lst = [ln.split('_')[1].split(' ')[0] for ln in lines]
lst2 = [ln.split(' ')[1] for ln in lines]
lst3 = [ln.split(' ')[2] for ln in lines]
#file_name = "ART" + str(lst2[0]) + "_" + str(lst3[0])[:-4] + ".bmp"

print(lst)
print(lst2)
print(lst3)
