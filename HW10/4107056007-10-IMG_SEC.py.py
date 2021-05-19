from decimal import Decimal
readfile = open('input10.txt','r')
line1 = readfile.readline().split(' ',1)
line2 = readfile.readline().split(' ',1)
line3 = readfile.readline().split(' ',1)
line4 = readfile.readline().split(' ',1)
x0, rx = Decimal(line1[0]),Decimal(line1[1][:-1])
y0, ry = Decimal(line2[0]),Decimal(line2[1][:-1])
seed, N = Decimal(line3[0]), Decimal(line3[1][:-1])
L = Decimal(line4[0][:-1])
print("x0 = {}, rx = {}".format(x0,rx))
print("y0 = {}, ry = {}".format(y0,ry))
print("seed = {}, N = {}".format(seed, N))
print("L = ",L)
#print(line1)
#print(line2)
#print(line3)
#print(line4)
import random
import math
random.seed(seed)
random_list = []
for i in range(100):
    if len(random_list) == 3:
        break
    r = random.randrange(1,N)
    if r not in random_list:
        random_list.append(r)
# print(random_list)
temp = []
x = rx * x0 * (1 - x0)
# print(x)
temp.append(x)
# print(temp)
for i in range(1,6):
    x = rx * temp[i-1] * (1 - temp[i-1])
    temp.append(x)
# print("x5 = ",temp[4])
x5 = temp[4]

temp.clear()
y = ry * y0 * (1 - y0)
temp.append(y)
for i in range(1,18):
    y = ry * temp[i-1] * (1 - temp[i-1])
    temp.append(y)
y18 = temp[17]
#print("y18 = ",temp[17])

spacex = math.ceil(x5 / L)
spacey = math.ceil(y18 / L)
a = random_list[0] + spacex
b = random_list[1] + spacey
# print(spacex)
# print(spacey)
print("a = {},b = {}".format(a,b))
import json
writefile = open('Output10.txt','w')
writefile.write(str(x0) + " " + str(rx) )
writefile.write("\n")
writefile.write(str(y0) + " " + str(ry) + "\n")
writefile.write(str(seed) + " " + str(N) + "\n")
writefile.write(str(L)+ "\n")
writefile.write(str(random_list[0]) + " " + str(random_list[1]) + " " + str(random_list[2])+ "\n")
writefile.write(str(x5) + " " + str(y18)+ "\n")
writefile.write(str(a) + " " + str(b)+ "\n")
