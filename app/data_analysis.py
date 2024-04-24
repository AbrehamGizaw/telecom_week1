import pandas as pd
import numpy as np

def count_empty_values(df):
    return df.isnull().sum()

def calculate_descriptive_statistics(df):
    return df.describe()
