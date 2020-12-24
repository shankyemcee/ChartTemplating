



import numpy as np
from os.path import isfile, join
import re
import pandas as pd
import json
import copy

data_file_no=0
multicolumn_file_no=0

data_output_dir="../nondata_tmplao"
multicol_data_output_dir="../nondata_multicolumn_tmplao"
output_data_txt_dir="./tmplao_nondata_files"

#ref_no=file_no
#train_data_load
mypath="..\..\C2T_data"
summary = np.loadtxt(join(mypath,"train\\trainOriginalSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
title = np.loadtxt(join(mypath,"train\\trainTitle.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data = np.loadtxt(join(mypath,"train\\trainData.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)


templated_summary = np.loadtxt(join(mypath,"train\\trainSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data_label = np.loadtxt(join(mypath,"train\\trainDataLabel.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)

templated_data_list=[]

#convert each line in data to a table and store as csv file in  data/all_csv.



# months = ['january', 'february', 'march', 'april', 'june', 'july', 'august', 'september', 'november', 'december']

# years = [str(i) for i in range(1850, 2050)]

fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']

# numbers = ['percent', 'percentage', '%', 'hundred', 'thousand', 'million', 'billion', 'trillion',
#            'hundreds', 'thousands', 'millions', 'billions', 'trillions']

# positiveTrends = ['increased', 'increase', 'increasing', 'grew', 'growing', 'rose', 'rising', 'gained', 'gaining']
# negativeTrends = ['decreased', 'decrease', 'decreasing', 'shrank', 'shrinking', 'fell', 'falling', 'dropped',
#                   'dropping']





def convert_list_to_dict(axis_value_list):
    table_dict={}
    for item in axis_value_list:
        colname = re.findall(r'.*?\|',item)[0][:-1]
        colval = re.findall(r'.*?\|',item)[1][:-1]
        if colname not in table_dict:
            table_dict[colname]=[colname];table_dict[colname].append(colval)
        else:
            table_dict[colname].append(colval)
    return  table_dict



def table_templater(table_frame,templated_summary_list,summary_list,old_data_list):
    table_frame=table_frame.drop(index=0)
    comp_frame=copy.deepcopy(table_frame)
    new_data_string = " ".join(old_data_list)
    for token in templated_summary_list:
        if "templateXLabel" in token:
           token_index=int(re.findall(r'\d+',token)[0])
           new_col_name=comp_frame.columns[0]
           new_col_name=new_col_name.replace("_"," ")
           new_col_name=[word for word in new_col_name.split() if word not in fillers]
           new_col_name[token_index] = token
           new_data_string = new_data_string.replace(comp_frame.columns[0],"_".join(new_col_name))
           comp_frame = comp_frame.rename(columns={comp_frame.columns[0]: "_".join(new_col_name)}) 
           
       
        elif "templateYLabel" in token:
           token_index=int(re.findall(r'\d+',token)[0])
           new_col_name=comp_frame.columns[1]
           new_col_name=new_col_name.replace("_"," ")
           new_col_name=[word for word in new_col_name.split() if word not in fillers]
           new_col_name[token_index] = token
           new_data_string = new_data_string.replace(comp_frame.columns[1],"_".join(new_col_name))
           comp_frame = comp_frame.rename(columns={comp_frame.columns[1]: "_".join(new_col_name)}) 
           
        
        elif "templateXValue" in token:
            col = table_frame.columns[0]
            comp_col=comp_frame.columns[0]
            if 'max' in token:
                row_index = table_frame[col].index[table_frame[col] == table_frame[col].max()].tolist()[0]
                new_data_string = new_data_string.replace(table_frame[col].max(),token)
                comp_frame[comp_col][row_index] = token
            elif 'min' in token:
                row_index = table_frame[col].index[table_frame[col] == table_frame[col].min()].tolist()[0]
                new_data_string = new_data_string.replace(table_frame[col].min(),token)
                comp_frame[comp_col][row_index] = token
            elif 'first' in token:
                new_data_string = new_data_string.replace(comp_frame[comp_col][1],token)
                comp_frame[comp_col][1] = token
            elif 'last' in token:
                row_index = len(table_frame)
                new_data_string = new_data_string.replace(comp_frame[comp_col][row_index],token)
                comp_frame[comp_col][row_index] = token
            else:
                token_index=int(re.findall(r'\d+',token)[0])
                new_data_string = new_data_string.replace(comp_frame[comp_col][token_index+1],token)
                comp_frame[comp_col][token_index+1] = token
            
          
        elif "templateYValue" in token:
            col = table_frame.columns[1]
            comp_col=comp_frame.columns[1]
            if 'max' in token:
                row_index = table_frame[col].index[table_frame[col] == table_frame[col].max()].tolist()[0]
                new_data_string = new_data_string.replace(table_frame[col].max(),token)
                comp_frame[comp_col][row_index] = token
            elif 'min' in token:
                row_index = table_frame[col].index[table_frame[col] == table_frame[col].min()].tolist()[0]
                new_data_string = new_data_string.replace(table_frame[col].min(),token)
                comp_frame[comp_col][row_index] = token
            elif 'first' in token:
                new_data_string = new_data_string.replace(comp_frame[comp_col][1],token)
                comp_frame[comp_col][1] = token
            elif 'last' in token:
                row_index = len(table_frame)
                new_data_string = new_data_string.replace(comp_frame[comp_col][row_index],token)
                comp_frame[comp_col][row_index] = token
            else:
                token_index=int(re.findall(r'\d+',token)[0])
                new_data_string = new_data_string.replace(comp_frame[comp_col][token_index+1],token)
                comp_frame[comp_col][token_index+1] = token
        
    new_data_string_list=new_data_string.split()
    for row in range(len(new_data_string_list)):
        row_list = new_data_string_list[row].split("|")
        if "template" not in row_list[0]:
            row_list[0] = "NONTEMPLATE"
        if "template" not in row_list[1]:
            row_list[1] = "NONTEMPLATE"
        new_data_string_list[row] = "|".join(row_list)
                
    new_data_string= " ".join(new_data_string_list)  
    return comp_frame,new_data_string 
                





def multicol_table_templater(table_frame,templated_summary_list,summary_list,old_data_list):
    table_frame=table_frame.drop(index=0)
    comp_frame=copy.deepcopy(table_frame)
    new_data_string = " ".join(old_data_list)
    for token in templated_summary_list:
        if "templateXLabel" in token:
           raise Exception("templateXLabel")
           # token_index=int(re.findall(r'\d+',token)[0])
           # new_col_name=comp_frame.columns[0]
           # new_col_name=new_col_name.replace("_"," ")
           # new_col_name=[word for word in new_col_name.split() if word not in fillers]
           # new_col_name[token_index] = token
           # comp_frame = comp_frame.rename(columns={comp_frame.columns[0]: " ".join(new_col_name)}) 
       
        elif "templateYLabel" in token:
           raise Exception("templateYLabel")
           # token_index=int(re.findall(r'\d+',token)[0])
           # new_col_name=comp_frame.columns[1]
           # new_col_name=new_col_name.replace("_"," ")
           # new_col_name=[word for word in new_col_name.split() if word not in fillers]
           # new_col_name[token_index] = token
           # comp_frame = comp_frame.rename(columns={comp_frame.columns[1]: " ".join(new_col_name)}) 
        
        elif "templateValue" in token:
            token_col=int(re.findall(r'\d+',token)[0])
            col = table_frame.columns[token_col]
            comp_col=comp_frame.columns[token_col]
            if 'max' in token:
                row_index = table_frame[col].index[table_frame[col] == table_frame[col].max()].tolist()[0]
                new_data_string = new_data_string.replace(table_frame[col].max(),token)
                comp_frame[comp_col][row_index] = token
            elif 'min' in token:
                row_index = table_frame[col].index[table_frame[col] == table_frame[col].min()].tolist()[0]
                new_data_string = new_data_string.replace(table_frame[col].min(),token)
                comp_frame[comp_col][row_index] = token
            elif 'first' in token:
                new_data_string = new_data_string.replace(comp_frame[comp_col][1],token)
                comp_frame[comp_col][1] = token
            elif 'last' in token:
                row_index = len(table_frame)
                new_data_string = new_data_string.replace(comp_frame[comp_col][row_index],token)
                comp_frame[comp_col][row_index] = token
            else:
                token_row=int(re.findall(r'\d+',token)[1])
                new_data_string = new_data_string.replace(comp_frame[comp_col][token_row+1],token)
                comp_frame[comp_col][token_row+1] = token
            
    new_data_string_list=new_data_string.split()
    for row in range(len(new_data_string_list)):
        row_list = new_data_string_list[row].split("|")
        if "template" not in row_list[0]:
            row_list[0] = "NONTEMPLATE"
        if "template" not in row_list[1]:
            row_list[1] = "NONTEMPLATE"
        new_data_string_list[row] = "|".join(row_list)
                
    new_data_string= " ".join(new_data_string_list)            
    return comp_frame,new_data_string



for tableIndex in range(len(data)):
    axis_value_list=[re.findall(r".*?\|.*?[\|]",item)[0] for item in  data[tableIndex].split()]
    table_dict = convert_list_to_dict(axis_value_list)
    table_frame = pd.DataFrame(table_dict)
    if table_frame.shape[1] == 2:
        templated_table,new_data_string=table_templater(table_frame,
                                        templated_summary[tableIndex].split(),
                                        summary[tableIndex].split(),
                                        data[tableIndex].split())
        templated_table.to_csv(join(data_output_dir,str(data_file_no)+".csv"),index=False)
        templated_data_list.append(new_data_string)
        data_file_no+=1
    
    else: 
        # break;
        templated_table,new_data_string=multicol_table_templater(table_frame,
                                                  templated_summary[tableIndex].split(),
                                                  summary[tableIndex].split(),
                                                  data[tableIndex].split())
        templated_table.to_csv(join(multicol_data_output_dir,str(multicolumn_file_no)+".csv"),index=False)
        templated_data_list.append(new_data_string)
        
        multicolumn_file_no+=1
        
# with open(join(output_data_txt_dir,"file.txt"), "w") as output:
#     output.write(new_data_string)     


# with open(join(output_data_txt_dir,"file.txt"), "w") as output:
#     #for listitem in places:
#         output.write('%s\n' % new_data_string)

        
    # if templated_table.shape[1] > 2:
    #     templated_table.to_csv(join(multicol_data_output_dir,str(multicolumn_file_no)+".csv"),index=False)
    #     multicolumn_file_no+=1
    # else:
    #     templated_table.to_csv(join(data_output_dir,str(data_file_no)+".csv"),index=False)
    #     data_file_no+=1



new_data_array = np.array(templated_data_list)
np.savetxt(join(output_data_txt_dir,"trainData.txt"), new_data_array,comments=None, delimiter="\n",fmt='%s',encoding='utf8')
    

    
 


#--------------------------------test data/summary/title load -----------------------



#ref_no=file_no
#train_data_load
mypath="..\..\C2T_data"
summary = np.loadtxt(join(mypath,"test\\testOriginalSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
title = np.loadtxt(join(mypath,"test\\testTitle.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data = np.loadtxt(join(mypath,"test\\testData.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)


templated_summary = np.loadtxt(join(mypath,"test\\testSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data_label = np.loadtxt(join(mypath,"test\\testDataLabel.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)

templated_data_list=[]



for tableIndex in range(len(data)):
    axis_value_list=[re.findall(r".*?\|.*?[\|]",item)[0] for item in  data[tableIndex].split()]
    table_dict = convert_list_to_dict(axis_value_list)
    table_frame = pd.DataFrame(table_dict)
    if table_frame.shape[1] == 2:
        templated_table,new_data_string=table_templater(table_frame,
                                        templated_summary[tableIndex].split(),
                                        summary[tableIndex].split(),
                                        data[tableIndex].split())
        templated_table.to_csv(join(data_output_dir,str(data_file_no)+".csv"),index=False)
        templated_data_list.append(new_data_string)
        data_file_no+=1
    
    else: 
        # break;
        templated_table,new_data_string=multicol_table_templater(table_frame,
                                                  templated_summary[tableIndex].split(),
                                                  summary[tableIndex].split(),
                                                  data[tableIndex].split())
        templated_table.to_csv(join(multicol_data_output_dir,str(multicolumn_file_no)+".csv"),index=False)
        templated_data_list.append(new_data_string)
        multicolumn_file_no+=1
        
   

    
new_data_array = np.array(templated_data_list)
np.savetxt(join(output_data_txt_dir,"testData.txt"), new_data_array,comments=None, delimiter="\n",fmt='%s',encoding='utf8')
    

    



#--------------------------------validation data/summary/title load -----------------------


#ref_no=file_no
#train_data_load
mypath="..\..\C2T_data"
summary = np.loadtxt(join(mypath,"valid\\validOriginalSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
title = np.loadtxt(join(mypath,"valid\\validTitle.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data = np.loadtxt(join(mypath,"valid\\validData.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)


templated_summary = np.loadtxt(join(mypath,"valid\\validSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data_label = np.loadtxt(join(mypath,"valid\\validDataLabel.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)

templated_data_list=[]



for tableIndex in range(len(data)):
    axis_value_list=[re.findall(r".*?\|.*?[\|]",item)[0] for item in  data[tableIndex].split()]
    table_dict = convert_list_to_dict(axis_value_list)
    table_frame = pd.DataFrame(table_dict)
    if table_frame.shape[1] == 2:
        templated_table,new_data_string=table_templater(table_frame,
                                        templated_summary[tableIndex].split(),
                                        summary[tableIndex].split(),
                                        data[tableIndex].split())
        templated_table.to_csv(join(data_output_dir,str(data_file_no)+".csv"),index=False)
        templated_data_list.append(new_data_string)
        data_file_no+=1
    
    else: 
        # break;
        templated_table,new_data_string=multicol_table_templater(table_frame,
                                                  templated_summary[tableIndex].split(),
                                                  summary[tableIndex].split(),
                                                  data[tableIndex].split())
        templated_table.to_csv(join(multicol_data_output_dir,str(multicolumn_file_no)+".csv"),index=False)
        templated_data_list.append(new_data_string)
        multicolumn_file_no+=1
        
        

    
new_data_array = np.array(templated_data_list)
np.savetxt(join(output_data_txt_dir,"validData.txt"), new_data_array,comments=None, delimiter="\n",fmt='%s',encoding='utf8')
    
 




