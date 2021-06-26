import pandas as pd

import re

df = pd.read_csv('python_assesment.csv')


names = df['name'].tolist()
#print(names)

matches = []

 
pattern = re.compile(r'[a-zA-Z]*\s*[a-zA-Z]*',flags = re.IGNORECASE)

s = input("Enter the string to be serached in capital letters: ")


search = pattern.search(s).group()


for match in names:
    if search in match:
        matches.append(match)
#print(matches)

df = pd.DataFrame(matches)
print(df.head(20))

