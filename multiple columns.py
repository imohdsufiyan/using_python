import pandas as pd

df = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})


ids_to_lookup = [101, 103]
columns_to_return = ['Name', 'Salary']

result1 = pd.DataFrame(ids_to_lookup, columns=['ID'])
for col in columns_to_return:
    result1[col] = result1['ID'].apply(lambda x: df[df['ID'] == x][col].values[0] if x in df['ID'].values else None)



print(result1)

lookup_ids = pd.DataFrame({'ID': [101, 103]})
result2 = lookup_ids.merge(df[['ID', 'Name', 'Salary']], on='ID', how='left')

print(result2)
