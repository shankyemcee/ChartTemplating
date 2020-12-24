# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:15:47 2020

@author: shank
"""


import json

##################################train_set#################################

labelPath = '../C2T_data/train/trainSummaryLabel.txt'
summaryPath = '../C2T_data/train/trainOriginalSummary.txt'


summary_count=0;
token_count=0;
count=0;
train_dict={}
templated_summary=[]

with open(summaryPath, 'r', encoding='utf-8') as summaryFile:
    templatedsummaryFile = summaryFile.readlines()




with open(labelPath, 'r', encoding='utf-8') as labelFile, open(summaryPath, 'r', encoding='utf-8') as summaryFile:
    for labels, summary in zip(labelFile.readlines(), summaryFile.readlines()):
        templated_summary=[]
        for label,token in zip(labels.split(),summary.split()):
            if label == '1':
               train_dict["template[%d]" % token_count]= token
               templated_summary.append("template[%d]" % token_count)
               token_count+=1
            else:
               templated_summary.append(token)
            
            
        templatedsummaryFile[summary_count]=" ".join(templated_summary);summary_count+=1





with open('trainSummary.txt', 'w',encoding="utf-8") as f:
    for item in templatedsummaryFile:
        f.write("%s\n" % item)


with open('train_ents.json', 'w') as json_file:
        json.dump(train_dict, json_file)    





##################################valid_set#################################

labelPath = '../C2T_data/valid/validSummaryLabel.txt'
summaryPath = '../C2T_data/valid/validOriginalSummary.txt'


summary_count=0;
token_count=0;
count=0;
valid_dict={}
templated_summary=[]

with open(summaryPath, 'r', encoding='utf-8') as summaryFile:
    templatedsummaryFile = summaryFile.readlines()




with open(labelPath, 'r', encoding='utf-8') as labelFile, open(summaryPath, 'r', encoding='utf-8') as summaryFile:
    for labels, summary in zip(labelFile.readlines(), summaryFile.readlines()):
        templated_summary=[]
        for label,token in zip(labels.split(),summary.split()):
            if label == '1':
               valid_dict["template[%d]" % token_count]= token
               templated_summary.append("template[%d]" % token_count)
               token_count+=1
            else:
               templated_summary.append(token)
            
            
        templatedsummaryFile[summary_count]=" ".join(templated_summary);summary_count+=1





with open('validSummary.txt', 'w',encoding="utf-8") as f:
    for item in templatedsummaryFile:
        f.write("%s\n" % item)


with open('valid_ents.json', 'w') as json_file:
        json.dump(valid_dict, json_file)    





##################################test_set#################################

labelPath = '../C2T_data/test/testSummaryLabel.txt'
summaryPath = '../C2T_data/test/testOriginalSummary.txt'


summary_count=0;
token_count=0;
count=0;
test_dict={}
templated_summary=[]

with open(summaryPath, 'r', encoding='utf-8') as summaryFile:
    templatedsummaryFile = summaryFile.readlines()




with open(labelPath, 'r', encoding='utf-8') as labelFile, open(summaryPath, 'r', encoding='utf-8') as summaryFile:
    for labels, summary in zip(labelFile.readlines(), summaryFile.readlines()):
        templated_summary=[]
        for label,token in zip(labels.split(),summary.split()):
            if label == '1':
               test_dict["template[%d]" % token_count]= token
               templated_summary.append("template[%d]" % token_count)
               token_count+=1
            else:
               templated_summary.append(token)
            
            
        templatedsummaryFile[summary_count]=" ".join(templated_summary);summary_count+=1





with open('testSummary.txt', 'w',encoding="utf-8") as f:
    for item in templatedsummaryFile:
        f.write("%s\n" % item)


with open('test_ents.json', 'w') as json_file:
        json.dump(test_dict, json_file)    








