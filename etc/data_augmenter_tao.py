# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:32:35 2020

@author: shank
"""
from os import listdir
from os.path import isfile, join
import pandas as pd

captionPath = '../dataset/captions/'
dataPath = '../dataset/data/'
titlePath = '../dataset/titles/'
data_outputPath = '../data_tao/'

#data_tao= data title augmentation only



datafiles = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]






def append_title(data_frame,title_list,caption_list):
    for title in title_list:
        row_list = ["title",title]
        row_list = row_list + ((data_frame.shape[1] - len(row_list) ) * ["title"])
        data_frame.loc[len(data_frame)] = row_list 
    
    return data_frame





# def append_title(data_frame,title_list,caption_list):
#     for title in title_list:
#         data_frame.loc[len(data_frame)]=["title",title]
    
#     return data_frame



for count in range(len(datafiles)):
    with open(captionPath + str(count) + ".txt", 'r', encoding='utf-8') as captionFile, \
         open(titlePath + str(count) + ".txt", 'r', encoding='utf-8') as titleFile:
         caption_list=captionFile.readlines()
         data_frame=pd.read_csv(dataPath + str(count) + ".csv")
         title_list=titleFile.readlines()
         data_frame=append_title(data_frame,title_list,caption_list)
         data_frame.to_csv(data_outputPath + str(count) + ".csv",index=False)
         
         
         





multicaptionPath = '../dataset/multiColumn/captions/'
multidataPath = '../dataset/multiColumn/data/'
multititlePath = '../dataset/multiColumn/titles/'
multidata_outputPath = '../data_multicolumn_tao/'





datafiles = [f for f in listdir(multidataPath) if isfile(join(multidataPath, f))]





for count in range(len(datafiles)):
    with open(multicaptionPath + str(count) + ".txt", 'r', encoding='utf-8') as captionFile, \
         open(multititlePath + str(count) + ".txt", 'r', encoding='utf-8') as titleFile:
         caption_list=captionFile.readlines()
         data_frame=pd.read_csv(multidataPath + str(count) + ".csv")
         title_list=titleFile.readlines()
         data_frame=append_title(data_frame,title_list,caption_list)
         data_frame.to_csv(multidata_outputPath + str(count) + ".csv",index=False)


