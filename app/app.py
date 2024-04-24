import streamlit as st
import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Streamlit App
st.title('Telecom Data Analysis')

# Display the DataFrame
st.write(df)

# Example visualization
st.subheader('Distribution of Dur. (ms)')
st.hist(df['Dur. (ms)'], bins=30)
