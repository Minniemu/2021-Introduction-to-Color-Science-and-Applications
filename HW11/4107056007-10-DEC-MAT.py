from PIL import Image
import csv 
import pandas as pd
import math
import numpy as np
directory = ['01_Airplane.bmp','02_Baboon.bmp','03_Lena.bmp','04_Peppers.bmp','05_Sailboat.bmp','06_Splash.bmp']
#Original image
with open('Output.csv','w') as csvfile:
    fieldnames = ['No','Images','MIR','MIG','MIB','VHR','VHG','VHB','SER','SEG','SEB']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    index = 0
    for d in directory:
        index += 1
        path = 'Origi_image/' + d
        image = Image.open(path)
        (H,V) = image.size
        #Mean of Image
        R = G = B = 0
        R_list = [0 for i in range(0,256)]
        G_list = [0 for i in range(0,256)]
        B_list = [0 for i in range(0,256)]
        for i in range(0,H):
            for j in range(0,V):
                value = image.getpixel((i,j))
                R += value[0]
                G += value[1]
                B += value[2]
                R_list[value[0]] += 1
                G_list[value[1]] += 1
                B_list[value[2]] += 1
        MIR = round(R/(H*V),2)
        MIG = round(G/(H*V),2)
        MIB = round(B/(H*V),2)

        #Variance of Histogram
        ZR = ZG = ZB = 0
        VarR = round(np.var(R_list),2)
        VarG = round(np.var(G_list),2)
        VarB = round(np.var(B_list),2)
        
        #Shannon Entropy
        PR = [0 for i in range(0,256)]
        PG = [0 for i in range(0,256)]
        PB = [0 for i in range(0,256)]
        logR = [0 for i in range(0,256)]
        logG = [0 for i in range(0,256)]
        logB = [0 for i in range(0,256)]
        for i in range(0,256):
            PR[i] = R_list[i]/(H*V)
            PG[i] = G_list[i]/(H*V)
            PB[i] = B_list[i]/(H*V)
            logR[i] = 0 if PR[i] == 0 else math.log(PR[i],2)
            logG[i] = 0 if PG[i] == 0 else math.log(PG[i],2)
            logB[i] = 0 if PB[i] == 0 else math.log(PB[i],2)
        SER = SEG = SEB = 0
        for i in range(0,256):
            SER -= PR[i] * logR[i]
            SEG -= PG[i] * logG[i]
            SEB -= PB[i] * logB[i]
        SER = round(SER,6)
        SEG = round(SEG,6)
        SEB = round(SEB,6)
        
        writer.writerow({'No':index,'Images':d,'MIR':MIR,'MIG':MIG,'MIB':MIB,'VHR':VarR,'VHG':VarG,'VHB':VarB,'SER':SER,'SEG':SEG,'SEB':SEB})
#Encrypt Image.
directory = ['01_Airplane_en.bmp','02_Baboon_en.bmp','03_Lena_en.bmp','04_Peppers_en.bmp','05_Sailboat_en.bmp','06_Splash_en.bmp']

with open('Output_en.csv','w') as csvfile:
    fieldnames = ['No','Images','MIR','MIG','MIB','VHR','VHG','VHB','SER','SEG','SEB']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    index = 0
    for d in directory:
        index += 1
        path = 'Encry_image/' + d
        image = Image.open(path)
        rgb_im = image.convert('RGB')
        (H,V) = image.size
        #Mean of Image
        R = G = B = 0
        R_list = [0 for i in range(0,256)]
        G_list = [0 for i in range(0,256)]
        B_list = [0 for i in range(0,256)]
        for i in range(0,H):
            for j in range(0,V):
                value = image.getpixel((i,j))
                R += value[0]
                G += value[1]
                B += value[2]
                R_list[value[0]] += 1
                G_list[value[1]] += 1
                B_list[value[2]] += 1
        MIR = round(R/(H*V),2)
        MIG = round(G/(H*V),2)
        MIB = round(B/(H*V),2)

        #Variance of Histogram
        ZR = ZG = ZB = 0
        VarR = round(np.var(R_list),2)
        VarG = round(np.var(G_list),2)
        VarB = round(np.var(B_list),2)
        
        #Shannon Entropy
        PR = [0 for i in range(0,256)]
        PG = [0 for i in range(0,256)]
        PB = [0 for i in range(0,256)]
        logR = [0 for i in range(0,256)]
        logG = [0 for i in range(0,256)]
        logB = [0 for i in range(0,256)]
        for i in range(0,256):
            PR[i] = R_list[i]/(H*V)
            PG[i] = G_list[i]/(H*V)
            PB[i] = B_list[i]/(H*V)
            logR[i] = 0 if PR[i] == 0 else math.log(PR[i],2)
            logG[i] = 0 if PG[i] == 0 else math.log(PG[i],2)
            logB[i] = 0 if PB[i] == 0 else math.log(PB[i],2)
        SER = SEG = SEB = 0
        for i in range(0,256):
            SER -= PR[i] * logR[i]
            SEG -= PG[i] * logG[i]
            SEB -= PB[i] * logB[i]
        SER = round(SER,6)
        SEG = round(SEG,6)
        SEB = round(SEB,6)
        
        writer.writerow({'No':index,'Images':d,'MIR':MIR,'MIG':MIG,'MIB':MIB,'VHR':VarR,'VHG':VarG,'VHB':VarB,'SER':SER,'SEG':SEG,'SEB':SEB})
#Decrypt Image
directory = ['01_Airplane_de.bmp','02_Baboon_de.bmp','03_Lena_de.bmp','04_Peppers_de.bmp','05_Sailboat_de.bmp','06_Splash_de.bmp']

with open('Output_de.csv','w') as csvfile:
    fieldnames = ['No','Images','MIR','MIG','MIB','VHR','VHG','VHB','SER','SEG','SEB']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    index = 0
    for d in directory:
        index += 1
        path = 'Decry_image/' + d
        image = Image.open(path)
        rgb_im = image.convert('RGB')
        (H,V) = image.size
        #Mean of Image
        R = G = B = 0
        R_list = [0 for i in range(0,256)]
        G_list = [0 for i in range(0,256)]
        B_list = [0 for i in range(0,256)]
        for i in range(0,H):
            for j in range(0,V):
                value = image.getpixel((i,j))
                R += value[0]
                G += value[1]
                B += value[2]
                R_list[value[0]] += 1
                G_list[value[1]] += 1
                B_list[value[2]] += 1
        MIR = round(R/(H*V),2)
        MIG = round(G/(H*V),2)
        MIB = round(B/(H*V),2)

        #Variance of Histogram
        ZR = ZG = ZB = 0
        VarR = round(np.var(R_list),2)
        VarG = round(np.var(G_list),2)
        VarB = round(np.var(B_list),2)
        
        #Shannon Entropy
        PR = [0 for i in range(0,256)]
        PG = [0 for i in range(0,256)]
        PB = [0 for i in range(0,256)]
        logR = [0 for i in range(0,256)]
        logG = [0 for i in range(0,256)]
        logB = [0 for i in range(0,256)]
        for i in range(0,256):
            PR[i] = R_list[i]/(H*V)
            PG[i] = G_list[i]/(H*V)
            PB[i] = B_list[i]/(H*V)
            logR[i] = 0 if PR[i] == 0 else math.log(PR[i],2)
            logG[i] = 0 if PG[i] == 0 else math.log(PG[i],2)
            logB[i] = 0 if PB[i] == 0 else math.log(PB[i],2)
        SER = SEG = SEB = 0
        for i in range(0,256):
            SER -= PR[i] * logR[i]
            SEG -= PG[i] * logG[i]
            SEB -= PB[i] * logB[i]
        SER = round(SER,6)
        SEG = round(SEG,6)
        SEB = round(SEB,6)
        
        writer.writerow({'No':index,'Images':d,'MIR':MIR,'MIG':MIG,'MIB':MIB,'VHR':VarR,'VHG':VarG,'VHB':VarB,'SER':SER,'SEG':SEG,'SEB':SEB})
