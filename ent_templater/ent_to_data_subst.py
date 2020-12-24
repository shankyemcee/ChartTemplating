# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 00:26:57 2020

@author: shank
"""


import json







##################################test_set#################################


generatedsummaryPath='templateOutput-p80.txt'

    
with open('test_ents.json',encoding="utf8") as f:
            test_dict = json.load(f)

  

with open(generatedsummaryPath, 'r', encoding='utf-8') as summaryFile:
    templatedsummaryFile = summaryFile.readlines()






summary_count=0;
untemplated_summary=[]
untemplatedsummaryFile={}

with open(generatedsummaryPath, 'r', encoding='utf-8') as summaryFile:
    for summary in  summaryFile.readlines():
        untemplated_summary=[];
        token_count=0;
        for token in summary.split():
            if token ==  'ENT':
               untemplated_summary.append(test_dict[str(summary_count)][token_count]);
               token_count+=1
               if token_count == len(test_dict[str(summary_count)]):
                     token_count=0  
            else:
               untemplated_summary.append(token)
        
        untemplatedsummaryFile[summary_count]=[" ".join(untemplated_summary)]
        summary_count+=1




# with open('templatedtest.json', 'w') as json_file:
#         json.dump(test_dict, json_file)    


with open('generated-p80.txt', 'w',encoding="utf-8") as f:
    for item in untemplatedsummaryFile:
        f.write("%s\n" % untemplatedsummaryFile[item][0])






