import pandas as pd
from sqlalchemy import create_engine

# Connect to the PostgreSQL database using SQLAlchemy
engine = create_engine('postgresql://postgres:1127@localhost/tenacademy')

# Query to select all data from the xdr_data table
query = "SELECT * FROM public.xdr_data;"

# Load data into a DataFrame
df = pd.read_sql(query, engine)

# Close the database connection
engine.dispose()

# Print number of empty rows by column
empty_rows_by_column = df.isnull().sum()
print("Number of empty rows by column:")
print(empty_rows_by_column)

# Check if empty rows are greater than 25% of total rows for each column
total_rows = len(df)
threshold = 0.25 * total_rows
for column, num_empty in empty_rows_by_column.items():
    if num_empty > threshold:
        df.drop(column, axis=1, inplace=True)
    elif num_empty > 0:
        if df[column].dtype == 'object':
            # If the column is non-numeric, replace missing values with the mode of the column
            mode_value = df[column].mode()[0]
            df[column] = df[column].fillna(mode_value)
        else:
            # Replace missing values with the mean of the column
            df[column] = df[column].fillna(df[column].mean())

# Save DataFrame to CSV
df.to_csv('telecom_data.csv', index=False)
