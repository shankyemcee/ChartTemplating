# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:41:28 2020

@author: shank
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:44:05 2020

@author: shank
"""

import pandas as pd
from collections import Counter
from os import listdir
from os.path import isfile, join
import copy
import json
from statistics import mean, stdev


max_len=0
all_list=[]
generatedScores=[]
#train_data_load
mypath="data/all_csv/"
program_output_path="./data/untemplatized_gold/"
#datafiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open(program_output_path + 'field_infusing_system_summaries.json',encoding="utf8") as f:
            output_test_summaries = json.load(f)



generatedList=[]

for table in output_test_summaries:
    d = pd.read_csv(mypath + table, sep='#',encoding='utf8')
    data_list =  [str(cell).lower() for row in d.values.tolist() for  cell in row]
    recordLength=len(data_list)
    generatedList=[]
    for token in output_test_summaries[table][0].split():
            if token.lower() in data_list:
                data_list.remove(token.lower())
                generatedList.append(token.lower())
    generatedRatio = len(generatedList) / recordLength       
    generatedScores.append(generatedRatio)       


print(round(mean(generatedScores)*100,2))
print(round(stdev(generatedScores)*100,2))





'''
with open('data/train_lm.json',encoding="utf8") as f:
            gold_train = json.load(f)
all_list = all_list + [str(token) for row in gold_train.values() for  ref in row[0] if type(ref)==str for token in ref.split()]



with open('data/test_lm.json',encoding="utf8") as f:
            gold_test = json.load(f)
all_list = all_list + [str(token) for row in gold_test.values() for  ref in row[0] if type(ref)==str for token in ref.split()]


with open('data/val_lm.json',encoding="utf8") as f:
            gold_val = json.load(f)
all_list = all_list + [str(token) for row in gold_val.values() for  ref in row[0] if type(ref)==str for token in ref.split()]






cnt = Counter()
for word in all_list:
    cnt[word] += 1



full_vocab_list = [ent[0] for ent in cnt.most_common()]



full_vocab_dict={"<PAD>": 0,
               	 "<SEP>": 1,
               	 "<SOS>": 2,
               	 "<EOS>": 3,
               	 "<UNK>": 4,
                 "#0": 5
                 }

k=6
for i in range(max_len):
    full_vocab_dict["#"+str(i+1)] = k;k+=1

vocab_dict=copy.deepcopy(full_vocab_dict)


for key in full_vocab_list:
    full_vocab_dict[key]=k
    if k < len(full_vocab_list)*.3:
        vocab_dict[key]=k
    k+=1;
    

with open('./data/full_vocab.json', 'w') as json_file:
        json.dump(full_vocab_dict, json_file)    


with open('./data/vocab.json', 'w') as json_file:
        json.dump(vocab_dict, json_file)    

'''
