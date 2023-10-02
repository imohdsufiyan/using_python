# import pandas as pd


# df = pd.DataFrame({
#     'ID': [101, 102, 103, 104],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'Salary': [50000, 60000, 70000, 80000]
# })

# # 1. Concatenate

# columns = ['Age','ID']

# for col in columns:
#     df[col] = df.apply(lambda x: str(x[col]), axis = 1)
# df['concat'] = df[columns].apply(''.join, axis = 1)

# print(df)


# # 2. Exact 

# df['exact'] = df['Name'].isin(['Bob','alice'])
# print(df)

# # 3. Left/Right/Medium
# to_search = ['Bob','Alice']
# to_replace_dict = {'Alice': 'XX','David': 'Y'}
# pattern = "|".join(to_search)
# print(pattern)
# df['find'] = df['Name'].apply(lambda x: all(word in x for word in to_search))
# print(df)

# #def replace_func(string, dic):
#     # for key, value in dic.items():
#     #     string = string.replace(key, value)
#     # return string
# #df['replace'] = df['Name'].apply(lambda x: replace_func(x,to_replace))


# # for key, value in to_replace_dict.items():
# #     df['find2'] = df['Name'].apply(lambda x: x.replace(key,value))
                       
# # print(df)
                                  
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})

# Create a new column to store the replaced values
df['find2'] = df['Name']

# Dictionary of words to be replaced
to_replace_dict = {'Alice': 'XX', 'David': 'Y'}

# Apply replacements
for key, value in to_replace_dict.items():
    df['find2'] = df['find2'].apply(lambda x: x.replace(key, value))

print(df)
                               