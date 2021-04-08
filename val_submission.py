# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:12:05 2019

@author: Rubén
"""

'''
Script to make the submission csv
'''

import pandas as pd


y_pred = pd.read_csv('D:/Data_Master/Recommenders/Task1Data/7_15features/y_pred_val_15features.csv')
val_data = pd.read_csv('D:/Data_Master/Recommenders/Task1Data/val.csv')

pd_clickout_test = val_data[val_data['action_type']=='clickout item']
y_pred = y_pred.values

item_cont = 0
cont = 0
output = []

for item in pd_clickout_test.values:
    item_feat = []
    item_feat.append(item[0])
    item_feat.append(item[1])
    item_feat.append(item[2])
    item_feat.append(item[3])
    
    recommend = item[10].split('|')
    n_items = len(recommend)
    y = list(y_pred[cont:cont+n_items,1])
    y_ord, recommend_ord = (list(t) for t in zip(*sorted(zip(y,recommend),reverse=True)))
    line = ''
    for r in recommend_ord:
        line = line+r+' '
    item_feat.append(line[:-1])
    
    cont += n_items
    item_cont += 1
    print(item_cont)
    
    output.append(item_feat)
    
columns = ['user_id','session_id','timestamp','step','item_recommendations']
submission = pd.DataFrame(output, columns = columns)
submission.to_csv('D:/Data_Master/Recommenders/Task1Data/7_15features/val_submission_15features.csv', index=False)