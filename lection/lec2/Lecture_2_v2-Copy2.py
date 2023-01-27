#!/usr/bin/env python
# coding: utf-8

# # Correction of the practice

# ## Check Python

# In[1]:


#Check that your python environnment is working:
print('It\'s working')


# ## Open csv file with Python

# In[2]:


#installation => anaconda prompt => pip install csv
#Import the csv package
import csv


# In[6]:


#import the csv package and print every row in the console
# print("D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv")
# print(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv")
#'r' : reading
#'w' writing
#'a' append (writing)

file = open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r')

csvfile = csv.reader(file)
for row in csvfile:
    print(row)
    
file.close()

#remeber to close files


# In[16]:


#I recommend : with open
#you can only iterate one time on csv.reader object

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        print(row)


# In[19]:


#opened with a dictionnary
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    for row in csvfile:
        print(row)


# ## Get CSV data into python console

# In[20]:


#import csv package
import csv


# In[30]:


#Create lists to store data (here a list of list to go faster)
list1, list2, list3 = [], [], []


#Information:
# #don't do that :
# list1 = list2 = list3 = []
# list1.append(1)
# print(list1, list2)
# info = [1,2,3]
# info2 = info # wrong
# info2 = [i for i in info] #right
# info2.append(7)
# print(info, info2)

# #Be carefull of names
# #open = [] #do not do that
# open_list = []


# In[22]:


#Open csv file and store data in lists
#be careful with name of lists (ex : data, open)
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        list1.append(row[0])
        list2.append(row[1])
        list3.append(row[2])


# In[25]:


#Check your lists
print(list1[:10])
print(list2[:10])


# In[40]:


#faster
lists = [[] for i in range(7)]
print(lists)

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile: 
        for index, l in enumerate(lists):
            l.append(row[index])
#         for index in range(0, len(lists)):
#             lists[index].append(row[index])  
#info about enumerate
a = [564, 166, 12]
for index, item in enumerate(a): 
    print(index)
    print(item)


# In[42]:


#Check your lists
print(lists[0][:10])
print(lists[1][:10])


# # Modify your data

# In[43]:


#First: Text into number (float)
for i in range(1,len(lists)):
    lists[i] = [float(j) for j in lists[i]]
    
print(lists[1][0])


# In[46]:


#Second: date
#first check the format
#1962-01-02
import datetime
print(type(datetime.datetime.strptime("1962-01-02" , "%Y-%m-%d")))


# In[52]:


#let's do it for all the list
lists[0] = [datetime.datetime.strptime(i , "%Y-%m-%d") for i in lists[0]]
print(lists[0])
# print(lists[0][3])
# print(lists[0][3].weekday())


# In[ ]:


#For this week :
#Prepare your code : clean
#result : 7 lists with datetime and float


# # DataFrame

# ## What are the advantages

# ### Using lists to manage data

# In[83]:


#You have a list of informations on students:
#Create the list
name = ['Bob', 'advgd', 'buo']
surname = ['jhg', 'hu', 'jio']
age = [18, 26, 17]


# In[55]:


#Diplay your data
print(name)
print(surname)
print(age)
#print last one

print(name[-1])
print(surname[-1])
print(age[-1])


# In[69]:


# Operate on this lists : delete one value,   
#advgd, hu
for i in range(0, len(name)):
    if name[i] == 'advgd' and surname[i] == 'hu':
        index_delete = i

del name[index_delete]
del surname[index_delete]
del age[index_delete]
print(name)


# In[73]:


# Operate on this lists : extract information on one student
for i in range(0, len(name)):
    if name[i] == 'advgd' and surname[i] == 'hu':
        print(name[i])


# In[77]:


# Operate on this lists : extract information on several students
for i in range(0, len(name)):
    if name[i] == 'advgd' or name[i] == 'Bob':
        print(name[i])


# In[86]:


# Sort datas
#function .sort
print(age)
age.sort()
print(name)
print(surname)
print(age)


# # Pandas

# ## The pandas package

# In[ ]:


#Install pandas
# pip install pandas


# In[87]:


#Import pandas package
#recommended as pd
import pandas as pd


# ## Let's create our first DataFrame

# In[89]:


#Create your first DataFrame
#Do not forget Uppercas for "D" and "F"
df = pd.DataFrame()
print(df)


# ## Populate it

# In[90]:


#Create a dictionnary with data from student
name = ['Bob', 'advgd', 'buo']
surname = ['jhg', 'hu', 'jio']
age = [18, 26, 17]


# In[93]:


#Create a dataframe from this dictionnary
# dictio = { 'key' : value}
dictio = {'names' : name, 'surnames' : surname, 'ages' : age}
print(dictio)
df = pd.DataFrame(dictio)


# In[94]:


# Display all your dataframe
print(df)


# In[97]:


# Display some lines of your dataframe
print(df['names'][1])


# In[ ]:


#Your turn:
#Create a empty dataframe
#Populate it with 3 lines of 6 columns (invent your own data)
#12:05


# ## Populate with csv file

# In[ ]:


# Select some data of the dataframe


# In[ ]:


#display it


# In[ ]:


# Remove 2 last columns to be more clear


# In[ ]:


#Modify data for later use (date and float)


# In[ ]:


#YOUR TURN
#Use you data from last pratice to make a dataframe from it
#Choose your own names for the columns (check the documentation of read_csv method)
#Column names should be : 
#['Date', 'Open price', 'High price', 'Low price', 'Close price', 'Adjusted close price', 'Volume exchanged']
#Try to automaticaly change Date into datetime object with the read_csv emthod 
#(check the documentation of read_csv method)


# ## Select data

# In[ ]:


# Display of the first data of the dataframe


# loc function => [index, column]


# In[ ]:


#select only a line with index (iloc)


# In[ ]:


#Select several lines with indexes


# In[ ]:


#Creation of a selection DataFrame


# In[ ]:


#select a part.


# In[ ]:


#Select a part of a Dataframe  ( () &() or .between)


# In[ ]:





# In[ ]:


#Sort the dataframe (.sort_values)


# In[ ]:


#YOUR TURN
#From your dataframe: extract data with the following conditions:
# - Only in 2021
# - Only date, Volume and High
# - Only when high price is superior than 2019 average high price


# In[ ]:




