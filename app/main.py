# main.py

import streamlit as st
import pandas as pd
import psycopg2

# Function to connect to PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="tenacademy",
            user="postgres",
            password="1127",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        st.error(f"Database connection error: {e}")

# Function to fetch data from the database
def fetch_data(conn):
    try:
        query = "SELECT * FROM xdr_data LIMIT 1000;"  # Assuming 'xdr_data' is the table name
        df = pd.read_sql(query, conn)
        return df
    except psycopg2.Error as e:
        st.error(f"Error fetching data: {e}")

def main():
    # Title and description
    st.title("Telecom Data Analysis and Visualization")
    st.write("This Streamlit app displays basic analysis and visualizations of telecom data.")

    # Connect to the database
    conn = connect_to_database()

    if conn:
        # Fetch data from the database
        data = fetch_data(conn)

        # Display the fetched data
        if not data.empty:
            st.subheader("Sample Data:")
            st.write(data)

            # Perform data analysis
            st.subheader("Data Analysis:")
            # You can perform various analyses here using Pandas functions

            # Data visualization
            st.subheader("Data Visualization:")
            # You can create plots, charts, and graphs using libraries like Matplotlib or Seaborn

            # Close the database connection
            conn.close()
        else:
            st.error("No data found.")
    else:
        st.error("Failed to connect to the database.")

if __name__ == "__main__":
    main()
