import pandas as pd
import numpy as np



# DataFrame with student names and IDs
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Student_ID': [101, 102, 103, 104]
})

# DataFrame with student IDs and scores
df2 = pd.DataFrame({
    'ID': [102, 102, 103, 104],
    'Score': [85, 90, 78, 88]
})

# using merge
df3 = df1.merge(df2,
         how ='left', 
         left_on ='Student_ID', 
         right_on = 'ID')

print(df3)



# using map



