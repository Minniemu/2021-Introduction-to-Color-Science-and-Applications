import numpy as np
import random
import csv

with open('input09.txt','r') as readfile:
    for line in readfile:
        listWords = line.split(" ")
    print(listWords)
x0 = float(listWords[0])
r = float(listWords[1])
N = int(listWords[2])
seed = int(listWords[3])
random_1 = []
x = r * x0 * (1 - x0)
x = round(x,6)
random_1.append(x)
for i in range(0,20):
    x = r * random_1[i] * (1 - random_1[i])
    x = round(x,6)
    random_1.append(x)
print(random_1)
mean_1 = round(np.mean(random_1),6)
std_1 = round(np.std(random_1),6)

random_2 = []
random.seed(seed)
for i in range(0,20):
    x = random.random()
    x = round(x,6)
    random_2.append(x)
print(random_2)
mean_2 = round(np.mean(random_2),6)
std_2 = round(np.std(random_2),6)

with open('output09.csv', 'w') as csvfile: # can save file in any format CSV or TSV
    writer = csv.writer(csvfile, delimiter=',')
    fieldnames = ["x0", "r", "N","seed"]
    writer.writerow(fieldnames)
    writer.writerow(listWords)
    for i in range(20):
        list_1 = [i+1,random_1[i],random_2[i]]
        writer.writerow(list_1)
    line1 = ['mean',' ',mean_1, mean_2]
    line2 = ['std', ' ',std_1, std_2]
    writer.writerow(line1)
    writer.writerow(line2)