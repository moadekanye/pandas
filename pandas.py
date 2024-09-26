import pandas as pd

# Load datasets
petal_data = pd.read_csv('petal_data.csv')
sepal_data = pd.read_csv('sepal_data.csv')

# Strip any whitespace from column names
petal_data.columns = petal_data.columns.str.strip()
sepal_data.columns = sepal_data.columns.str.strip()

# Print columns to confirm
print("Petal Data Columns:", petal_data.columns)
print("Sepal Data Columns:", sepal_data.columns)

# Merge datasets
combined_df = pd.merge(petal_data, sepal_data, on='sample_id', how='inner')

# Check the merged DataFrame
print("Combined DataFrame Columns:", combined_df.columns)
print(combined_df.head())

# Proceed only if 'species' exists in combined_df
if 'species' in combined_df.columns:
    combined_df = combined_df[['sample_id', 'species', 'petal_length', 'petal_width', 'sepal_length', 'sepal_width']]
    
    # Calculate correlation matrix
    correlation_matrix = combined_df[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].corr()
    print("Correlation Matrix:\n", correlation_matrix)

    # Calculate average, median, and standard deviation
    average_values = combined_df.groupby('species').mean()
    median_values = combined_df.groupby('species').median()
    std_dev_values = combined_df.groupby('species').std()

    print("Averages:\n", average_values)
    print("Medians:\n", median_values)
    print("Standard Deviations:\n", std_dev_values)
else:
    print("Column 'species' is missing from combined_df.")
