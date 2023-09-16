import pandas as pd


# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Visit': [5, 10, 15, 20],
    'Profit': [100, 200, 300, 400]
}

df = pd.DataFrame(data)





# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Visit': [5, 10, 15, 20],
    'Profit': [100, 200, 300, 400]
}

df = pd.DataFrame(data)

# Selecting columns that contain only non-numeric data
non_numeric_columns = df.select_dtypes(include=['number'],)

# Displaying the selected columns
print(non_numeric_columns)

# Selecting columns that contain "it" in their names
selected_columns = df.filter(like='it', axis=1)

# Displaying the selected columns
print(selected_columns)
