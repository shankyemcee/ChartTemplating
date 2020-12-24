# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:21:55 2020

@author: shank
"""
import json

filter_list=[67,72,189,245,370,427,585,654,784,836,872,883,
             989,1066,1121,1122,1196,1271,1335,1408,1411,1439,
             1447,1514,1662,1710,1891,2073,2118,2119,2140,2177,
             2178,2234,2248,2480,2867,2974,3209,3358,3375,3394,
             3500,3537,3677,3793,3831,3867,4009,4010,4036,4078,
             4175,4219,4224,4248,4283,4288,4331,4370,4406,4446,
             4462,4468,4487,4499,4517,4552,4578,4596,4597,4636,
             4638,4645,4652,4693,4710,4743,4786,5481]


with open('data/train_lm.json',encoding="utf8") as f:
            gold_train = json.load(f)
        

for key in filter_list:
    out= gold_train.pop(str(key)+".csv", None)
    



with open('./data/failure_removed_golds/train_lm.json', 'w') as json_file:
        json.dump(gold_train, json_file)    
