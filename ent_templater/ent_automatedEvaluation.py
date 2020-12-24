import csv
import json
from statistics import mean, stdev
#from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance
import sys





labelPath = '../C2T_data/test/testSummaryLabel.txt'
goldPath = '../C2T_data/test/testOriginalSummary.txt'
summaryPath = '../C2T_data/test/testSummary.txt'

generatedPath = "./generated-p80.txt"


fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']

count = 0

generatedScores = []


"""generatedDLDs = []
baselineDLDs = []
untemplatedDLDs = []"""


with open(generatedPath, 'r', encoding='utf-8') as summaryFile:
    sumFile = summaryFile.readlines()



with open(labelPath, 'r', encoding='utf-8') as labelFile, open(summaryPath, 'r', encoding='utf-8') as summaryFile, \
        open(goldPath, 'r', encoding='utf-8') as goldFile:
    for lbls, summary, gold in zip(labelFile.readlines(), summaryFile.readlines(), goldFile.readlines()):
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
        
        
        summary1 = sumFile[count]
        for token in summary1.split():
            if token.lower() in list1:
                list1.remove(token.lower())
                generatedList.append(token.lower())

        

        count += 1

        generatedRatio = len(generatedList) / recordLength


        generatedScores.append(generatedRatio)


 

print(f'generated CS stdev: {round(stdev(generatedScores)*100,2)}%')

print()
print(f'generated CS mean: {round(mean(generatedScores)*100,2)}%')

print()
print(f'generated CS RSD: {round((stdev(generatedScores)*100) / abs(mean(generatedScores)),2)}%')


labels = ['generated CS stdev', 'generated CS mean', 'generated CS RSD']
values = [f'{round(stdev(generatedScores)*100,2)}%',
          f'{round(mean(generatedScores)*100,2)}%',
          f'{round((stdev(generatedScores)*100) / abs(mean(generatedScores)),2)}%']

# with open('../results/automatedEvaluation.csv', 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     csvwriter.writerow(labels)
#     csvwriter.writerow(values)