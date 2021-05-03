# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:02:16 2021

@author: Prashant
"""

# import files
import json
import pandas as pd

# Reading CSV  in dataframe
df0 = pd.read_csv('C:/Users/Prashant/Downloads/Regan - Full Time AI Engineer - Technical test/interview/task1/oidv6-class-descriptions.csv'
               )

# Reading JSON files 
with open('C:/Users/Prashant/Downloads/Regan - Full Time AI Engineer - Technical test/interview/task1/bbox_labels_600_hierarchy.json') as f:
  data1 = json.load(f)


"""
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
"""
def flatten_json(nested_json):
    
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out    

#%%
#Reading JSON file into dataframe
df = pd.Series(flatten_json(data1)).to_frame()

#Reset index of dataframe
df2 = df.reset_index()
#Rename Column Name in dataframe
df2 = df2.rename(columns={0: "LabelName", "index": "Category"})

# Map values from one data frame to another dataframe
df2['LabelName'] = df2.LabelName.map(df0.set_index('LabelName')['DisplayName'])

df.to_csv('Final_output_task1.csv')