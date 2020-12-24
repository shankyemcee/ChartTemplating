# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:15:57 2020

@author: shank
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:32:35 2020

@author: shank
"""
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy
import copy

captionPath = '../dataset/captions/'
dataPath = '../dataset/data/'
titlePath = '../dataset/titles/'
data_outputPath = '../data_stsao/'

#data_tao= data statistical data augmentation only



datafiles = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]



#compute_frame[col].str.replace(',', '')

def append_stats(data_frame,title_list,caption_list):
    compute_frame=copy.deepcopy(data_frame)
    compute_frame=compute_frame.loc[:,compute_frame.columns != compute_frame.columns[0]]
    for col in compute_frame.columns:
            #compute_frame[col]=compute_frame[col].replace('-', '0')
            if str(type(compute_frame[col][0])) == "<class 'str'>":
                compute_frame[col]=compute_frame[col].str.replace(',', '')
                compute_frame[col]=compute_frame[col].str.replace('-', '0')
                compute_frame[col]=compute_frame[col].str.replace('%', '')
                compute_frame[col]=compute_frame[col].str.replace('$', '')
                compute_frame[col]=compute_frame[col].str.replace('€', '')
                compute_frame[col]=compute_frame[col].str.replace('£', '')
                compute_frame[col]=compute_frame[col].apply(lambda x: numpy.float64(x))
    stat_frame = compute_frame.describe()
    stat_frame.reset_index(level=0, inplace=True)
    stat_frame = stat_frame.rename(columns={'index': data_frame.columns[0]})
    return data_frame.append(stat_frame, ignore_index=True)
            




for count in range(len(datafiles)):
    with open(captionPath + str(count) + ".txt", 'r', encoding='utf-8') as captionFile, \
         open(titlePath + str(count) + ".txt", 'r', encoding='utf-8') as titleFile:
         caption_list=captionFile.readlines()
         data_frame=pd.read_csv(dataPath + str(count) + ".csv")
         title_list=titleFile.readlines()
         data_frame=append_stats(data_frame,title_list,caption_list)
         data_frame.to_csv(data_outputPath + str(count) + ".csv",index=False)
         
         
         





multicaptionPath = '../dataset/multiColumn/captions/'
multidataPath = '../dataset/multiColumn/data/'
multititlePath = '../dataset/multiColumn/titles/'
multidata_outputPath = '../data_multicolumn_stsao/'





datafiles = [f for f in listdir(multidataPath) if isfile(join(multidataPath, f))]





for count in range(len(datafiles)):
    with open(multicaptionPath + str(count) + ".txt", 'r', encoding='utf-8') as captionFile, \
         open(multititlePath + str(count) + ".txt", 'r', encoding='utf-8') as titleFile:
         caption_list=captionFile.readlines()
         data_frame=pd.read_csv(multidataPath + str(count) + ".csv")
         title_list=titleFile.readlines()
         data_frame=append_stats(data_frame,title_list,caption_list)
         data_frame.to_csv(multidata_outputPath + str(count) + ".csv",index=False)


