
'''
The objective of this assignment is to print the dataframe showed in the instruction.
Only one test will be done.
You can write you code after this comment :
'''
#Your code here:

import pandas as pd


name = ["Brad", "Angelina", "Tom" ]
surname = ["Pitt", "Jolie", "Cruise" ]
age = [58, 47, 60]

dictio = {'Name' : name,
          'Surname' : surname, 
          'Age' : age }

df = pd.DataFrame(dictio)
print(df)