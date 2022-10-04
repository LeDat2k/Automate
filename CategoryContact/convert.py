# %%
#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('contacts.csv')
# Name : all combine

# Those people who have 2 numbers but I didn't categorize them : 8080853532 ::: 25808874232


# %%
# use 1 name only: "Given Name"
for i, name in enumerate(df['Given Name']):
    if str(df.at[i, 'Additional Name']) != 'nan':
        df.at[i, 'Given Name'] += ' ' + str(df.at[i, 'Additional Name']) 
        df.at[i, 'Additional Name'] = ''
    
    if str(df.at[i, 'Family Name']) != 'nan':
        df.at[i, 'Given Name'] += ' ' + str(df.at[i, 'Family Name'])
        df.at[i, 'Family Name'] = ''

# %%
#  ::: 
# split merged numbers
for i, value in enumerate(df['Phone 1 - Value']):
    if value.find(':::') != -1:
        numbers = value.split(' ::: ')
        df.at[i, 'Phone 1 - Value'] = numbers[0]
        df.at[i, 'Phone 2 - Value'] = numbers[1]

# %%

# take 3 first letter of df['Phone 1 - Value']
# check backthem in ./MobileNetwork.csv
# Take code print it back to df['Phone 1 - Type']
mobile = pd.read_csv('./mobileNetwork.csv')
head_number = ''
for i, num in enumerate(df['Phone 1 - Value']):
    # take 3 first number
    if (str(num[:3]).find(' ') != -1):
        # case : "08 7"=> 087
        head_number = str(num[:4]).replace(' ', '')
    else:    
        head_number = str(num[:3])

    # check network code lookup with ./mobileNetwork.csv 
    network_code = mobile.network.loc[mobile['head_number']==int(head_number)].values
    if network_code.size<=0:
        continue
    else:
        network_code = network_code[0]
    
    df.at[i, 'Phone 1 - Type'] = network_code

############################ 
for i, num in enumerate(df['Phone 2 - Value']):
    if str(num) == 'nan':
        continue
    if (str(num[:3]).find(' ') != -1):
        head_number = str(num[:4]).replace(' ', '')
    else:    
        head_number = str(num[:3])
    
    network_code = mobile.network.loc[mobile['head_number']==int(head_number)].values
    if network_code.size<=0:
        continue
    else:
        network_code = network_code[0]
    
    df.at[i, 'Phone 2 - Type'] = network_code

# %%
df.to_csv('out.csv', index=False)   


# %% 
