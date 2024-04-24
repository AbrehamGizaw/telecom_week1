import pandas as pd
import pytest

# Load cleaned data for testing
df = pd.read_csv('cleaned_data.csv')

# Example test: Check if DataFrame has any missing values
def test_missing_values():
    assert df.isnull().sum().sum() == 0, "DataFrame contains missing values"
