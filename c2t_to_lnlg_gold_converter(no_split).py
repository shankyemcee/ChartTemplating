# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:51:01 2020

@author: shankar
"""

# import csv
# import json


# with open('1-1921-1.html.csv') as file:
#     reader = csv.DictReader(file, delimiter=",")
#     ab = list(reader)




import pandas as pd

import numpy as np

#save each file with # delimiter and convert each value to string format

from os import listdir
from os.path import isfile, join
mypath="..\Chart2Text\dataset\data"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    data_file=pd.read_csv(join(mypath, file), header = None, encoding='utf8')
    np.savetxt(join("./data/all_csv",file), data_file, delimiter='#', fmt='%s',encoding='utf8')


