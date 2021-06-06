from os import rename
from PIL import Image
import csv 
import pandas as pd
import math
import numpy as np
from tqdm import tqdm
directory_orig = ['01_Airplane.bmp','02_Baboon.bmp','03_Lena.bmp','04_Peppers.bmp','05_Sailboat.bmp','06_Splash.bmp']
directory_en = ['01_Airplane_en.bmp','02_Baboon_en.bmp','03_Lena_en.bmp','04_Peppers_en.bmp','05_Sailboat_en.bmp','06_Splash_en.bmp']
#Original image
NPCR_R_list = []
NPCR_G_list = []
NPCR_B_list = []
UACI_R_list = []
UACI_G_list = []
UACI_B_list = []
for a in tqdm(range(len(directory_orig))):
    path = 'Origi_image/' + directory_orig[a]
    image = Image.open(path)
    (H,V) = image.size
    # print("H = {},V = {}".format(H,V))
    #RGB-Original
    R = G = B = 0
    R_list_orig = []
    G_list_orig = []
    B_list_orig = []
    for i in range(0,H):
        R_temp = []
        G_temp = []
        B_temp = []
        for j in range(0,V):
            value = image.getpixel((i,j))
            R_temp.append(value[0])
            G_temp.append(value[1])
            B_temp.append(value[2])
        R_list_orig.append(R_temp)
        G_list_orig.append(G_temp)
        B_list_orig.append(B_temp)
    #RGB-Original
    path = 'Encry_image/' + directory_en[a]
    image = Image.open(path)
    R = G = B = 0
    R_list_en = []
    G_list_en = []
    B_list_en = []
    for i in range(0,H):
        R_temp = []
        G_temp = []
        B_temp = []
        for j in range(0,V):
            value = image.getpixel((i,j))
            R_temp.append(value[0])
            G_temp.append(value[1])
            B_temp.append(value[2])
        R_list_en.append(R_temp)
        G_list_en.append(G_temp)
        B_list_en.append(B_temp)
    #compute NPCR
    NPCR_R = NPCR_G = NPCR_B = 0
    for i in range(0,H):
        for j in range(0,V):
            if R_list_orig[i][j] != R_list_en[i][j]:
                NPCR_R += 1
            if G_list_orig[i][j] != G_list_en[i][j]:
                NPCR_G += 1
            if B_list_orig[i][j] != B_list_en[i][j]:
                NPCR_B += 1
    NPCR_R_list.append(round(NPCR_R/(H*V)*100,4))
    NPCR_G_list.append(round(NPCR_G/(H*V)*100,4))
    NPCR_B_list.append(round(NPCR_B/(H*V)*100,4))
    #compute UACI
    UACI_R = UACI_G = UACI_B = 0
    for i in range(0,H):
        for j in range(0,V):
            UACI_R += abs(R_list_orig[i][j] - R_list_en[i][j])
            UACI_G += abs(G_list_orig[i][j] - G_list_en[i][j])
            UACI_B += abs(B_list_orig[i][j] - B_list_en[i][j])
    UACI_R_list.append(round((UACI_R/(H*V*255))*100,4))
    UACI_G_list.append(round((UACI_G/(H*V*255))*100,4))
    UACI_B_list.append(round((UACI_B/(H*V*255))*100,4))
# print(NPCR_R_list)
# print(NPCR_G_list)
# print(NPCR_B_list)
# print(UACI_R_list)
# print(UACI_G_list)
# print(UACI_B_list)

with open('Output12.csv','w',newline='') as csvfile:
    fieldnames = ['No','ORI Images','ENC Image','NPCR(R)','NPCR(G)','NPCR(B)',' UACI(R)','UACI(G)','UACI(B)']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(NPCR_R_list)):
        writer.writerow({'No':i+1,'ORI Images':directory_orig[i],'ENC Image':directory_en[i],'NPCR(R)':NPCR_R_list[i],'NPCR(G)':NPCR_G_list[i],'NPCR(B)':NPCR_B_list[i],' UACI(R)':UACI_R_list[i],'UACI(G)':UACI_G_list[i],'UACI(B)':UACI_B_list[i]})
