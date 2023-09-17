import pandas as pd


# Sample DataFrame 1
df_x = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Employee_ID': [101, 102, 103]
})

# Sample DataFrame 2 with non-unique IDs and non-numeric data
df_y = pd.DataFrame({
    'Emp_ID': [101, 102, 102, 103, 103],
    'Department': ['HR', 'IT', 'Finance', 'Sales', 'Marketing']
})



## Taking the first occurrence
df_y_first = df_y.drop_duplicates(subset='Emp_ID', keep='first')
df_x['Department_1'] = df_x['Employee_ID'].map(df_y_first.set_index('Emp_ID')['Department'])

## Combining all occurrences into a list
df_y_list = df_y.groupby('Emp_ID')['Department'].apply(list)
df_x['Department_2'] = df_x['Employee_ID'].map(df_y_list)

##  Combining all occurrences into a delimited string
df_y_string = df_y.groupby('Emp_ID')['Department'].apply(', '.join)

df_x['Department_3'] = df_x['Employee_ID'].apply(lambda x: df_y_string.loc[x])

print(df_x)
## joining data horizontally
#pd.concat([df_x,df_y], axis = 'index')