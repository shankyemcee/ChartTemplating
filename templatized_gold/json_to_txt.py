# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:25:46 2020

@author: shank
"""

import json
import numpy as np



with open('GPT_gpt2_1.95.json',encoding="utf8") as f:
            gen_summs = json.load(f)
        

sum_list=[]


for summ in gen_summs:
    sum_list.append(" ".join(gen_summs[summ][0].split()[:-1]))



new_data_array = np.array(sum_list)
np.savetxt("gpt_generated.txt", new_data_array,comments=None, delimiter="\n",fmt='%s',encoding='utf8')
    
