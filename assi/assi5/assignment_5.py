'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import csv
from pickletools import int4
import pandas as pd
import datetime
import numpy as np
#1
missing_values = ["_", "error"]
df = pd.read_csv("attendance_to_clean.csv", na_values = missing_values)

#2 for dates, for name, for count
for index, lines in df.iterrows():
    try:
        datetime.datetime.strptime(lines['DATE'], '%Y-%m-%d')
    except:
        df.loc[index, 'DATE'] = np.nan

    try:
        int(lines['NAME_STUDENT'])
        df.loc[index, 'NAME_STUDENT'] = np.nan
    except:
        pass

    try:
        int(lines['COUNT'])
    except:
        df.loc[index, 'COUNT'] = np.nan

df.dropna(inplace = True)

# 3
for index in df.index:
    if df.loc[index, 'BEGIN_HOUR'] > 17:
        df.loc[index, 'BEGIN_HOUR'] = np.nan
    if float(df.loc[index, 'COUNT']) > 2:
        df.loc[index, 'COUNT'] = np.nan

for index,lines in df.iterrows():
    df.loc[index, 'COUNT'] = float(lines['COUNT'])
    df.loc[index, 'WEEK'] = int(lines['WEEK'])

    if(datetime.datetime.strptime(lines['DATE'], '%Y-%m-%d') < datetime.datetime(2022, 8, 1)):
        df.loc[index, 'DATE'] = np.nan


#4
# print(df.isnull().sum().sum())
df.dropna(inplace = True) 

#5
df.drop_duplicates(inplace = True)

#6
df = df.sort_values(by = ['NAME_STUDENT', 'DATE', 'BEGIN_HOUR', 'WEEK'], ignore_index= True)
df.reset_index(drop=True, inplace = True)
print(df)

