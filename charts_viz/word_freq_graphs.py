# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:23:08 2020

@author: shank
"""

import csv
import json
from statistics import mean, stdev
#from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance
import sys
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.pyplot import figure


labelPath = '../C2T_data/test/testSummaryLabel.txt'
goldPath = '../C2T_data/test/testOriginalSummary.txt'
summaryPath = '../C2T_data/test/testSummary.txt'
titlePath = '../C2T_data/test/testTitle.txt'

generatedPath = '../C2T_data/results/aug17/generated/'
untemplatedPath = '../C2T_data/results/aug17/generated_untemplated/'
baselinePath = '../C2T_data/results/aug17/generated_baseline/'

fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']

count = 1

generatedScores = []
baselineScores = []
untemplatedScores = []

"""generatedDLDs = []
baselineDLDs = []
untemplatedDLDs = []"""


recall_list=[]
hallucinated_list=[]
other_recalled_list=[]



with open(labelPath, 'r', encoding='utf-8') as labelFile, open(summaryPath, 'r', encoding='utf-8') as summaryFile, \
        open(goldPath, 'r', encoding='utf-8') as goldFile, open(titlePath, 'r', encoding='utf-8') as titleFile:
    for lbls, summary, gold,title in zip(labelFile.readlines(), summaryFile.readlines(), goldFile.readlines(),titleFile.readlines()):
        labelArr = lbls.split()
        summArr = summary.split()
        goldArr = gold.split()
        recordList = []
        for lab, sums, gld in zip(labelArr, summArr, goldArr):
            if lab == '1' and gld.lower() not in fillers and gld.lower() not in recordList:
                recordList.append(gld.lower())
        list1 = recordList
        list2 = recordList
        list3 = recordList
        recordLength = len(recordList)
        generatedList = []
        with open(generatedPath + str(count) + '.json') as generatedFile:
            document1 = json.loads(generatedFile.read())
            summary1 = ''.join(document1['summary'])
            data_string = " | ".join([key+":"+value for item in document1['data'] for key,value in item.items()])
        for token in summary1.split():
            if token.lower() in list1:
                list1.remove(token.lower())
                generatedList.append(token.lower())
                recall_list.append(token.lower())

            elif token.lower() not in title.lower() and token.lower() not in gold.lower() and token.lower() not in data_string.lower():
                hallucinated_list.append(token.lower())
                if token.lower() == "leading": print(count)
            else:
                other_recalled_list.append(token.lower())

        count += 1



# df = pd.DataFrame({'freq': hallucinated_list})
# df.groupby('freq', as_index=False).size().plot(kind='bar')
# plt.show()


fig = plt.figure(figsize=(10,6))
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)


trivial_hallucinations=['shows','was','and','were','with','from','that',',','this','for','of',
                        '\'s','amounted','about','(',')','by','had','around','approximately','has',
                        'between','over','most','according','there','highest','increase',
                        'their','reported','largest','during','up', 'which','than','first','its',
                        'depicts','are','additional','as','to','all','more','since','have','increased',
                        'been','previous','ranked','ranking','until','who',
                        'they','while','leading','some','among','based','used','also','be',
                        'expected','when','only','presents','reached','stated','-','almost','followed',
                        'generated','illustatrates','compared','recent','came','produced','down','found',
                        'last','same','such','- ','popular','across','reach','per','results','sorted','after',
                        'aged','not','roughly','the','will','can','comparison','estimated','experienced']

new_list = [elem for elem in hallucinated_list if elem in trivial_hallucinations]
count_counter2 = Counter(new_list)

most_common=count_counter2.most_common(20)
# most_common=most_common[::-1]
most_common_freqs=[item[1] for item in most_common]
most_common_words=[item[0] for item in most_common]
plt.rcParams.update({'font.size': 7})
ax1 = fig.add_subplot(231)
# fig.set_size_inches(3,3)
ax1.bar(most_common_words, most_common_freqs,color='blue' ,align='center', alpha=1)
ax1.autoscale(tight=True)
ax1.tick_params(axis='x',labelrotation=75)
#plt.yticks(most_common_words, keys)
# plt.xlabel('Trivial Hallucination Frequencies')
ax1.title.set_text('Frequency of Trivial Hallucinations')
# plt.show()
# fig.savefig('trivial_hallucinations.png', bbox_inches='tight',dpi=400)





nontrivial_hallucinations = ['%','statistic','million','total','period','years','country','year',
                             'worldwide','information','one','global','dollars','average',
                             'second','company','people','survey','time','countries','industry',
                             'number','world','figure','u.s','population','respondents','market',
                             'billion','british','fiscal','forecast','percentage',
                             'data','online','products','units','growth','pounds','users','european','sales',
                             'services','united_states','consumers','individuals','international','projections'
                             'third','annual','broken','companies','month']




new_list = [elem for elem in hallucinated_list if elem in nontrivial_hallucinations]
count_counter2 = Counter(new_list)

most_common=count_counter2.most_common(20)
# most_common=most_common[::-1]
most_common_freqs=[item[1] for item in most_common]
most_common_words=[item[0] for item in most_common]
ax2 = fig.add_subplot(232,sharey=ax1)
# fig.set_size_inches(3,3)
# plt.rcParams.update({'font.size': 7})
ax2.bar(most_common_words, most_common_freqs,color='blue', align='center', alpha=1)
ax2.autoscale(tight=True)
ax2.tick_params(axis='x',labelrotation=75)
#plt.yticks(most_common_words, keys)
# plt.xlabel('Nontrivial Hallucination Frequencies')
ax2.title.set_text('Frequency of Nontrivial Hallucinations')
# plt.show()
# fig.savefig('nontrivial_hallucinations.png', bbox_inches='tight',dpi=400)









factual_hallucination_fillers=['2018','2019','2017','2015','100,000','2020','50',
                               '2014','?','2016','25','2012','co2','40','2008',
                               'august_16','q2_2019','1.3','18','27.99','34.8','65+_years',
                               '264.2','1978','2010_s2','2013','2018_s1','uber_technologies_(may_9)',
                               'yuan','1000','1.4','1.072','7am','10,000','21.7','24.9','29',
                               '31','42.7','118','183','200','374','423','606','1953','2000/01',
                               '2004','2010','2018/19']





new_list = [elem for elem in hallucinated_list if elem  in factual_hallucination_fillers]
count_counter2 = Counter(new_list)

most_common=count_counter2.most_common(20)
# most_common=most_common[::-1]
most_common_freqs=[item[1] for item in most_common]
most_common_words=[item[0] for item in most_common]
ax3 = fig.add_subplot(233)
# fig.set_size_inches(3,3)
# plt.rcParams.update({'font.size': 7})
ax3.bar(most_common_words, most_common_freqs,color='blue', align='center', alpha=1)
ax3.autoscale(tight=True)
ax3.tick_params(axis='x',labelrotation=75)
#plt.yticks(most_common_words, keys)
# plt.xlabel('Factual Hallucination Frequencies')
ax3.title.set_text('Frequency of Factual Hallucinations')
# plt.show()
# fig.savefig('factual_hallucinations.png', bbox_inches='tight',dpi=400)







other_fillers = ['%', 'shows','statistic','was', 'and','were','with','from',
                         'that',',','this','for','of','\'s','about','(', ')','by',
                         'had','around','has','between','over','or', 'an', 'as',
                         'can', 'be', 'a', ':', '-', 'to', 'but', 'is', 'of', 
                         'it', 'on', '.', 'at', '(', ')', ',', ';','in','the',
                         'until','are']



new_list = [elem for elem in recall_list if elem not in other_fillers]
count_counter2 = Counter(new_list)

most_common=count_counter2.most_common(20)
# most_common=most_common[::-1]
most_common_freqs=[item[1] for item in most_common]
most_common_words=[item[0] for item in most_common]
ax4 = fig.add_subplot(234,sharey=ax1)
# plt.rcParams.update({'font.size': 7})
ax4.bar(most_common_words, most_common_freqs,color='blue', align='center', alpha=1)
ax4.autoscale(tight=True)
ax4.tick_params(axis='x',labelrotation=75)
#plt.yticks(most_common_words, keys)
# plt.xlabel('Recall Frequencies')
ax4.title.set_text('Frequency of Recalls')
# plt.show()
# fig.savefig('Recalls.png', bbox_inches='tight',dpi=400)








new_list = [elem for elem in other_recalled_list if elem not in other_fillers]
count_counter2 = Counter(new_list)

most_common=count_counter2.most_common(20)
# most_common=most_common[::-1]
most_common_freqs=[item[1] for item in most_common]
most_common_words=[item[0] for item in most_common]
ax5 = fig.add_subplot(235)
# plt.rcParams.update({'font.size': 7})
ax5.bar(most_common_words, most_common_freqs,color='blue', align='center', alpha=1)
ax5.autoscale(tight=True)
ax5.tick_params(axis='x',labelrotation=75)
#plt.yticks(most_common_words, keys)
# plt.xlabel('Other generated word Frequencies')
ax5.title.set_text('Frequency of Other Generated Words')




fig.tight_layout()
plt.show()
fig.savefig('All_Charts.png', bbox_inches='tight',dpi=400)

    






