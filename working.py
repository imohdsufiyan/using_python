import pandas as pd
import numpy as np


# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Visit': [5, 10, 15, 20],
    'Profit': [-100, 200, 300, 400]
}

df = pd.DataFrame(data)




# nested if 

## np.where
df['remarks_1'] = np.where(df['Profit']<= 110,"V Low",
                         np.where(df['Profit']<= 200,"Low",
                                  np.where(df['Profit']<= 300,"Medium",
                                           "High")))

df['remarks_X'] = np.where((df['Profit']<= 200) | (df['City']== "New York"), "A","B")

## pd.cut
bins = [df['Profit'].min(), 110,200,300,400]
labels = ['V Low', 'Low','Medium','High']
df['remarks_2'] = pd.cut(df['Profit'],bins = bins, labels = labels, include_lowest= True)


## custom function
def remarks_func(x):
    if x <= 110 :
        y = "V Low"
    elif x <= 200 :
        y = "Low"
    elif x<= 300 :
        y = "Medium"
    else :
        y = "High"
    return y
df['remarks_3'] = df['Profit'].apply(remarks_func)

print(df)

