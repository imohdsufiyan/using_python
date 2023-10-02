import pandas as pd

# Sample DataFrame with student names and IDs
df1 = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Student_ID': [101, 102, 103]
})

df2 = pd.DataFrame({
    'Student_ID': [101, 102, 103],
    'Score': [85, 90, 78]
})

df2.set_index('Student_ID', inplace=True)

df1['Score'] = df1['Student_ID'].apply(lambda x: df2.loc[x, 'Score'])

print(df1.T)
