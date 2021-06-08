from PIL import Image
import csv 
import pandas as pd
import math
import numpy as np
from numpy import mean
from tqdm import tqdm
directory_orig = ['01_Airplane.bmp','02_Baboon.bmp','03_Lena.bmp','04_Peppers.bmp','05_Sailboat.bmp','06_Splash.bmp']
directory_en = ['01_Airplane_en.bmp','02_Baboon_en.bmp','03_Lena_en.bmp','04_Peppers_en.bmp','05_Sailboat_en.bmp','06_Splash_en.bmp']
HD_list_orig = []
VD_list_orig = []
DD_list_orig = []
for a in tqdm(range(len(directory_orig))):

    path = 'Origi_image/' + directory_orig[a]
    image = Image.open(path)
    (H,V) = image.size
    temp_H = {}
    # print("H = {},V = {}".format(H,V))
    #RGB-Original
    R = G = B = 0
    R_list_orig = [None]*512
    G_list_orig = [None]*512
    B_list_orig = [None]*512
    for i in range(0,H):
        # print(i)
        R_temp = []
        G_temp = []
        B_temp = []
        for j in range(0,V):
            value = image.getpixel((j,i))
            R_temp.append(value[0])
            G_temp.append(value[1])
            B_temp.append(value[2])
        R_list_orig[511-i] = R_temp
        G_list_orig[511-i] = G_temp
        B_list_orig[511-i] = B_temp

    # value = image.getpixel((0,0))
    # print("pixel({},{}) = {}".format(0,0,value[0]))
    # value = image.getpixel((0,1))
    # print("pixel({},{}) = {}".format(0,1,value[0]))

    ###HD
    HD_X_R = []
    HD_X_G = []
    HD_X_B = []
    HD_Y_R = []
    HD_Y_G = []
    HD_Y_B = []
    x_bar_R = x_bar_G = x_bar_B = 0
    y_bar_R = y_bar_G = y_bar_B = 0
    #HD_X
    for i in range(0,H):
        for j in range(0,V-1):
            HD_X_R.append(R_list_orig[i][j])
            HD_X_G.append(G_list_orig[i][j]) 
            HD_X_B.append(B_list_orig[i][j])
            HD_Y_R.append(R_list_orig[i][j+1])
            HD_Y_G.append(G_list_orig[i][j+1]) 
            HD_Y_B.append(B_list_orig[i][j+1])

    #average
    x_bar_R = mean(HD_X_R)
    x_bar_G = mean(HD_X_G)
    x_bar_B = mean(HD_X_B)
    y_bar_R = mean(HD_Y_R)
    y_bar_G = mean(HD_Y_G)
    y_bar_B = mean(HD_Y_B)
    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
    L = len(HD_X_R)

    #var
    var_x_R = np.var(HD_X_R)
    var_x_G = np.var(HD_X_G)
    var_x_B = np.var(HD_X_B)
    var_y_R = np.var(HD_Y_R)
    var_y_G = np.var(HD_Y_G)
    var_y_B = np.var(HD_Y_B)
    # print("var_x_R = {},var_x_G = {},var_x_B = {}".format(var_x_R,var_x_G,var_x_B))
    # print("var_y_R = {},var_y_G = {},var_y_B = {}".format(var_y_R,var_y_G,var_y_B))

    #cov
    cov_R = cov_G = cov_B = 0
    for i in range(L):
        cov_R += (HD_X_R[i]-x_bar_R)*(HD_Y_R[i]-y_bar_R)
        cov_G += (HD_X_G[i]-x_bar_G)*(HD_Y_G[i]-y_bar_G)
        cov_B += (HD_X_B[i]-x_bar_B)*(HD_Y_B[i]-y_bar_B)
    # print(cov_R,cov_G,cov_B)
    cov_R = cov_R/(L-1)
    cov_G = cov_G/(L-1)
    cov_B = cov_B/(L-1)

    #Correlation
    cor_R = cov_R/math.sqrt(var_x_R*var_y_R)
    cor_G = cov_G/math.sqrt(var_x_G*var_y_G)
    cor_B = cov_B/math.sqrt(var_x_B*var_y_B)

    temp_H['R'] = [x_bar_R,y_bar_R,var_x_R,var_y_R,cov_R,cor_R]
    temp_H['G'] = [x_bar_G,y_bar_G,var_x_G,var_y_G,cov_G,cor_G]
    temp_H['B'] = [x_bar_B,y_bar_B,var_x_B,var_y_B,cov_B,cor_B]
    HD_list_orig.append(temp_H)
    # print(HD_list_orig)

    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
    # print("cov_R = {},cov_G = {},cov_B = {}".format(cov_R,cov_G,cov_B))
    # print("cor_R = {},cor_G = {},cor_B = {}".format(cor_R,cor_G,cor_B))
    ###VD
    VD_X_R = []
    VD_X_G = []
    VD_X_B = []
    VD_Y_R = []
    VD_Y_G = []
    VD_Y_B = []
    temp_V = {}
    x_bar_R = x_bar_G = x_bar_B = 0
    y_bar_R = y_bar_G = y_bar_B = 0
    #VD_X
    for i in range(0,H-1):
        for j in range(0,V):
            VD_X_R.append(R_list_orig[i][j])
            VD_X_G.append(G_list_orig[i][j]) 
            VD_X_B.append(B_list_orig[i][j])
            VD_Y_R.append(R_list_orig[i+1][j])
            VD_Y_G.append(G_list_orig[i+1][j]) 
            VD_Y_B.append(B_list_orig[i+1][j])
    # print(len(VD_X_R),len(VD_Y_R))

    #average
    x_bar_R = mean(VD_X_R)
    x_bar_G = mean(VD_X_G)
    x_bar_B = mean(VD_X_B)
    y_bar_R = mean(VD_Y_R)
    y_bar_G = mean(VD_Y_G)
    y_bar_B = mean(VD_Y_B)
    L = len(VD_X_R)
    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
 
    #var
    var_x_R = np.var(VD_X_R)
    var_x_G = np.var(VD_X_G)
    var_x_B = np.var(VD_X_B)
    var_y_R = np.var(VD_Y_R)
    var_y_G = np.var(VD_Y_G)
    var_y_B = np.var(VD_Y_B)

    #cov
    cov_R = cov_G = cov_B = 0
    for i in range(L):
        cov_R += (VD_X_R[i]-x_bar_R)*(VD_Y_R[i]-y_bar_R)
        cov_G += (VD_X_G[i]-x_bar_G)*(VD_Y_G[i]-y_bar_G)
        cov_B += (VD_X_B[i]-x_bar_B)*(VD_Y_B[i]-y_bar_B)
    cov_R = cov_R/(L-1)
    cov_G = cov_G/(L-1)
    cov_B = cov_B/(L-1)

    #Correlation
    cor_R = cov_R/math.sqrt(var_x_R*var_y_R)
    cor_G = cov_G/math.sqrt(var_x_G*var_y_G)
    cor_B = cov_B/math.sqrt(var_x_B*var_y_B)
    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
    # print("cov_R = {},cov_G = {},cov_B = {}".format(cov_R,cov_G,cov_B))
    # print("cor_R = {},cor_G = {},cor_B = {}".format(cor_R,cor_G,cor_B))
    temp_V['R'] = [x_bar_R,y_bar_R,var_x_R,var_y_R,cov_R,cor_R]
    temp_V['G'] = [x_bar_G,y_bar_G,var_x_G,var_y_G,cov_G,cor_G]
    temp_V['B'] = [x_bar_B,y_bar_B,var_x_B,var_y_B,cov_B,cor_B]
    VD_list_orig.append(temp_V)
    # print(temp_V)
    # print(sum(VD_X_R))

    #DD
    temp_D = {}
    DD_X_R = []
    DD_X_G = []
    DD_X_B = []
    DD_Y_R = []
    DD_Y_G = []
    DD_Y_B = []
    x_bar_R = x_bar_G = x_bar_B = 0
    y_bar_R = y_bar_G = y_bar_B = 0
    #DD_X
    for i in range(0,H-1):
        for j in range(0,V-1):
            DD_X_R.append(R_list_orig[i][j])
            DD_X_G.append(G_list_orig[i][j]) 
            DD_X_B.append(B_list_orig[i][j])
            DD_Y_R.append(R_list_orig[i+1][j+1])
            DD_Y_G.append(G_list_orig[i+1][j+1]) 
            DD_Y_B.append(B_list_orig[i+1][j+1])
    #average
    x_bar_R = mean(DD_X_R)
    x_bar_G = mean(DD_X_G)
    x_bar_B = mean(DD_X_B)
    y_bar_R = mean(DD_Y_R)
    y_bar_G = mean(DD_Y_G)
    y_bar_B = mean(DD_Y_B)
    L = len(DD_X_R)

    #var
    var_x_R = np.var(DD_X_R)
    var_x_G = np.var(DD_X_G)
    var_x_B = np.var(DD_X_B)
    var_y_R = np.var(DD_Y_R)
    var_y_G = np.var(DD_Y_G)
    var_y_B = np.var(DD_Y_B)

    #cov
    cov_R = cov_G = cov_B = 0
    for i in range(L):
        cov_R += (DD_X_R[i]-x_bar_R)*(DD_Y_R[i]-y_bar_R)
        cov_G += (DD_X_G[i]-x_bar_G)*(DD_Y_G[i]-y_bar_G)
        cov_B += (DD_X_B[i]-x_bar_B)*(DD_Y_B[i]-y_bar_B)
    cov_R = cov_R/(L-1)
    cov_G = cov_G/(L-1)
    cov_B = cov_B/(L-1)

    #Correlation
    cor_R = cov_R/math.sqrt(var_x_R*var_y_R)
    cor_G = cov_G/math.sqrt(var_x_G*var_y_G)
    cor_B = cov_B/math.sqrt(var_x_B*var_y_B)

    temp_D['R'] = [x_bar_R,y_bar_R,var_x_R,var_y_R,cov_R,cor_R]
    temp_D['G'] = [x_bar_G,y_bar_G,var_x_G,var_y_G,cov_G,cor_G]
    temp_D['B'] = [x_bar_B,y_bar_B,var_x_B,var_y_B,cov_B,cor_B]
    # print(sum(DD_X_R))

    DD_list_orig.append(temp_D)
# print(HD_list_orig)
# print(VD_list_orig)
# print(DD_list_orig)

#encrypt
HD_list_en = []
VD_list_en = []
DD_list_en = []
for a in tqdm(range(len(directory_en))):
    path = 'Encry_image/' + directory_en[a]
    image = Image.open(path)
    (H,V) = image.size
    temp_H = {}
    # print("H = {},V = {}".format(H,V))
    #RGB-Original
    R = G = B = 0
    R_list_orig = [None]*512
    G_list_orig = [None]*512
    B_list_orig = [None]*512
    for i in range(0,H):
        # print(i)
        R_temp = []
        G_temp = []
        B_temp = []
        for j in range(0,V):
            value = image.getpixel((j,i))
            R_temp.append(value[0])
            G_temp.append(value[1])
            B_temp.append(value[2])
        R_list_orig[511-i] = R_temp
        G_list_orig[511-i] = G_temp
        B_list_orig[511-i] = B_temp

    # value = image.getpixel((0,0))
    # print("pixel({},{}) = {}".format(0,0,value[0]))
    # value = image.getpixel((0,1))
    # print("pixel({},{}) = {}".format(0,1,value[0]))

    ###HD
    HD_X_R = []
    HD_X_G = []
    HD_X_B = []
    HD_Y_R = []
    HD_Y_G = []
    HD_Y_B = []
    x_bar_R = x_bar_G = x_bar_B = 0
    y_bar_R = y_bar_G = y_bar_B = 0
    #HD_X
    for i in range(0,H):
        for j in range(0,V-1):
            HD_X_R.append(R_list_orig[i][j])
            HD_X_G.append(G_list_orig[i][j]) 
            HD_X_B.append(B_list_orig[i][j])
            HD_Y_R.append(R_list_orig[i][j+1])
            HD_Y_G.append(G_list_orig[i][j+1]) 
            HD_Y_B.append(B_list_orig[i][j+1])

    #average
    x_bar_R = mean(HD_X_R)
    x_bar_G = mean(HD_X_G)
    x_bar_B = mean(HD_X_B)
    y_bar_R = mean(HD_Y_R)
    y_bar_G = mean(HD_Y_G)
    y_bar_B = mean(HD_Y_B)
    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
    L = len(HD_X_R)

    #var
    var_x_R = np.var(HD_X_R)
    var_x_G = np.var(HD_X_G)
    var_x_B = np.var(HD_X_B)
    var_y_R = np.var(HD_Y_R)
    var_y_G = np.var(HD_Y_G)
    var_y_B = np.var(HD_Y_B)
    # print("var_x_R = {},var_x_G = {},var_x_B = {}".format(var_x_R,var_x_G,var_x_B))
    # print("var_y_R = {},var_y_G = {},var_y_B = {}".format(var_y_R,var_y_G,var_y_B))

    #cov
    cov_R = cov_G = cov_B = 0
    for i in range(L):
        cov_R += (HD_X_R[i]-x_bar_R)*(HD_Y_R[i]-y_bar_R)
        cov_G += (HD_X_G[i]-x_bar_G)*(HD_Y_G[i]-y_bar_G)
        cov_B += (HD_X_B[i]-x_bar_B)*(HD_Y_B[i]-y_bar_B)
    # print(cov_R,cov_G,cov_B)
    cov_R = cov_R/(L-1)
    cov_G = cov_G/(L-1)
    cov_B = cov_B/(L-1)

    #Correlation
    cor_R = cov_R/math.sqrt(var_x_R*var_y_R)
    cor_G = cov_G/math.sqrt(var_x_G*var_y_G)
    cor_B = cov_B/math.sqrt(var_x_B*var_y_B)

    temp_H['R'] = [x_bar_R,y_bar_R,var_x_R,var_y_R,cov_R,cor_R]
    temp_H['G'] = [x_bar_G,y_bar_G,var_x_G,var_y_G,cov_G,cor_G]
    temp_H['B'] = [x_bar_B,y_bar_B,var_x_B,var_y_B,cov_B,cor_B]
    HD_list_en.append(temp_H)
    # print(HD_list_orig)

    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
    # print("cov_R = {},cov_G = {},cov_B = {}".format(cov_R,cov_G,cov_B))
    # print("cor_R = {},cor_G = {},cor_B = {}".format(cor_R,cor_G,cor_B))
    ###VD
    VD_X_R = []
    VD_X_G = []
    VD_X_B = []
    VD_Y_R = []
    VD_Y_G = []
    VD_Y_B = []
    temp_V = {}
    x_bar_R = x_bar_G = x_bar_B = 0
    y_bar_R = y_bar_G = y_bar_B = 0
    #VD_X
    for i in range(0,H-1):
        for j in range(0,V):
            VD_X_R.append(R_list_orig[i][j])
            VD_X_G.append(G_list_orig[i][j]) 
            VD_X_B.append(B_list_orig[i][j])
            VD_Y_R.append(R_list_orig[i+1][j])
            VD_Y_G.append(G_list_orig[i+1][j]) 
            VD_Y_B.append(B_list_orig[i+1][j])
    # print(len(VD_X_R),len(VD_Y_R))

    #average
    x_bar_R = mean(VD_X_R)
    x_bar_G = mean(VD_X_G)
    x_bar_B = mean(VD_X_B)
    y_bar_R = mean(VD_Y_R)
    y_bar_G = mean(VD_Y_G)
    y_bar_B = mean(VD_Y_B)
    L = len(VD_X_R)
    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
 
    #var
    var_x_R = np.var(VD_X_R)
    var_x_G = np.var(VD_X_G)
    var_x_B = np.var(VD_X_B)
    var_y_R = np.var(VD_Y_R)
    var_y_G = np.var(VD_Y_G)
    var_y_B = np.var(VD_Y_B)

    #cov
    cov_R = cov_G = cov_B = 0
    for i in range(L):
        cov_R += (VD_X_R[i]-x_bar_R)*(VD_Y_R[i]-y_bar_R)
        cov_G += (VD_X_G[i]-x_bar_G)*(VD_Y_G[i]-y_bar_G)
        cov_B += (VD_X_B[i]-x_bar_B)*(VD_Y_B[i]-y_bar_B)
    cov_R = cov_R/(L-1)
    cov_G = cov_G/(L-1)
    cov_B = cov_B/(L-1)

    #Correlation
    cor_R = cov_R/math.sqrt(var_x_R*var_y_R)
    cor_G = cov_G/math.sqrt(var_x_G*var_y_G)
    cor_B = cov_B/math.sqrt(var_x_B*var_y_B)
    # print("x_bar_R = {},x_bar_G = {},x_bar_B = {}".format(x_bar_R,x_bar_G,x_bar_B))
    # print("y_bar_R = {},y_bar_G = {},y_bar_B = {}".format(y_bar_R,y_bar_G,y_bar_B))
    # print("cov_R = {},cov_G = {},cov_B = {}".format(cov_R,cov_G,cov_B))
    # print("cor_R = {},cor_G = {},cor_B = {}".format(cor_R,cor_G,cor_B))
    temp_V['R'] = [x_bar_R,y_bar_R,var_x_R,var_y_R,cov_R,cor_R]
    temp_V['G'] = [x_bar_G,y_bar_G,var_x_G,var_y_G,cov_G,cor_G]
    temp_V['B'] = [x_bar_B,y_bar_B,var_x_B,var_y_B,cov_B,cor_B]
    VD_list_en.append(temp_V)
    # print(temp_V)
    # print(sum(VD_X_R))

    #DD
    temp_D = {}
    DD_X_R = []
    DD_X_G = []
    DD_X_B = []
    DD_Y_R = []
    DD_Y_G = []
    DD_Y_B = []
    x_bar_R = x_bar_G = x_bar_B = 0
    y_bar_R = y_bar_G = y_bar_B = 0
    #DD_X
    for i in range(0,H-1):
        for j in range(0,V-1):
            DD_X_R.append(R_list_orig[i][j])
            DD_X_G.append(G_list_orig[i][j]) 
            DD_X_B.append(B_list_orig[i][j])
            DD_Y_R.append(R_list_orig[i+1][j+1])
            DD_Y_G.append(G_list_orig[i+1][j+1]) 
            DD_Y_B.append(B_list_orig[i+1][j+1])
    #average
    x_bar_R = mean(DD_X_R)
    x_bar_G = mean(DD_X_G)
    x_bar_B = mean(DD_X_B)
    y_bar_R = mean(DD_Y_R)
    y_bar_G = mean(DD_Y_G)
    y_bar_B = mean(DD_Y_B)
    L = len(DD_X_R)

    #var
    var_x_R = np.var(DD_X_R)
    var_x_G = np.var(DD_X_G)
    var_x_B = np.var(DD_X_B)
    var_y_R = np.var(DD_Y_R)
    var_y_G = np.var(DD_Y_G)
    var_y_B = np.var(DD_Y_B)

    #cov
    cov_R = cov_G = cov_B = 0
    for i in range(L):
        cov_R += (DD_X_R[i]-x_bar_R)*(DD_Y_R[i]-y_bar_R)
        cov_G += (DD_X_G[i]-x_bar_G)*(DD_Y_G[i]-y_bar_G)
        cov_B += (DD_X_B[i]-x_bar_B)*(DD_Y_B[i]-y_bar_B)
    cov_R = cov_R/(L-1)
    cov_G = cov_G/(L-1)
    cov_B = cov_B/(L-1)

    #Correlation
    cor_R = cov_R/math.sqrt(var_x_R*var_y_R)
    cor_G = cov_G/math.sqrt(var_x_G*var_y_G)
    cor_B = cov_B/math.sqrt(var_x_B*var_y_B)

    temp_D['R'] = [x_bar_R,y_bar_R,var_x_R,var_y_R,cov_R,cor_R]
    temp_D['G'] = [x_bar_G,y_bar_G,var_x_G,var_y_G,cov_G,cor_G]
    temp_D['B'] = [x_bar_B,y_bar_B,var_x_B,var_y_B,cov_B,cor_B]
    # print(sum(DD_X_R))

    DD_list_en.append(temp_D)
with open('Output13.csv','w',newline='') as csvfile:
    fieldnames = ['Image Name','Mode','Channel','x_bar','y_bar','VAR(X)',' VAR(Y)','COV(X,Y)','Correlation(X,Y)']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(HD_list_orig)):
        color = ['R','G','B']
        #origi
        for c in color:
            writer.writerow({'Image Name':directory_orig[i],'Mode':'HD','Channel':c + 'Channel','x_bar':round(HD_list_orig[i][c][0],2),'y_bar':round(HD_list_orig[i][c][1],2),'VAR(X)':round(HD_list_orig[i][c][2],2),' VAR(Y)':round(HD_list_orig[i][c][3],2),'COV(X,Y)':round(HD_list_orig[i][c][4],2),'Correlation(X,Y)':round(HD_list_orig[i][c][5],6)})
        for c in color:
            writer.writerow({'Image Name':directory_orig[i],'Mode':'VD','Channel':c + 'Channel','x_bar':round(VD_list_orig[i][c][0],2),'y_bar':round(VD_list_orig[i][c][1],2),'VAR(X)':round(VD_list_orig[i][c][2],2),' VAR(Y)':round(VD_list_orig[i][c][3],2),'COV(X,Y)':round(VD_list_orig[i][c][4],2),'Correlation(X,Y)':round(VD_list_orig[i][c][5],6)})
        for c in color:
            writer.writerow({'Image Name':directory_orig[i],'Mode':'DD','Channel':c + 'Channel','x_bar':round(DD_list_orig[i][c][0],2),'y_bar':round(DD_list_orig[i][c][1],2),'VAR(X)':round(DD_list_orig[i][c][2],2),' VAR(Y)':round(DD_list_orig[i][c][3],2),'COV(X,Y)':round(DD_list_orig[i][c][4],2),'Correlation(X,Y)':round(DD_list_orig[i][c][5],6)})
        #EN
        for c in color:
            writer.writerow({'Image Name':directory_en[i],'Mode':'HD','Channel':c + 'Channel','x_bar':round(HD_list_en[i][c][0],2),'y_bar':round(HD_list_en[i][c][1],2),'VAR(X)':round(HD_list_en[i][c][2],2),' VAR(Y)':round(HD_list_en[i][c][3],2),'COV(X,Y)':round(HD_list_en[i][c][4],2),'Correlation(X,Y)':round(HD_list_en[i][c][5],6)})
        for c in color:
            writer.writerow({'Image Name':directory_en[i],'Mode':'VD','Channel':c + 'Channel','x_bar':round(VD_list_en[i][c][0],2),'y_bar':round(VD_list_en[i][c][1],2),'VAR(X)':round(VD_list_en[i][c][2],2),' VAR(Y)':round(VD_list_en[i][c][3],2),'COV(X,Y)':round(VD_list_en[i][c][4],2),'Correlation(X,Y)':round(VD_list_en[i][c][5],6)})
        for c in color:
            writer.writerow({'Image Name':directory_en[i],'Mode':'DD','Channel':c + 'Channel','x_bar':round(DD_list_en[i][c][0],2),'y_bar':round(DD_list_en[i][c][1],2),'VAR(X)':round(DD_list_en[i][c][2],2),' VAR(Y)':round(DD_list_en[i][c][3],2),'COV(X,Y)':round(DD_list_en[i][c][4],2),'Correlation(X,Y)':round(DD_list_en[i][c][5],6)})
        