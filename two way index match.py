import pandas as pd



# Sample DataFrame
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'History': [88, 82, 91],
    'Biology': [92, 87, 85]
}
df = pd.DataFrame(data)


lookup_data = {
    'Student': ['Alice', 'Charlie'],
    'Subject': ['History', 'Math']
}
lookup_df = pd.DataFrame(lookup_data)

df.set_index('Student', inplace=True)

print(df)
print(lookup_df)


df['sum'] = df.apply(lambda x: x['Math'] + x['History'], axis = 1)
print(df)

lookup_df['score'] = lookup_df.apply(lambda x: df.loc[x['Student'],x['Subject']], axis = 1)

print(lookup_df)