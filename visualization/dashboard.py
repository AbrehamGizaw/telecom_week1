import sys
import os
import pandas as pd

# Add the project's root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import modules relative to the project's root directory
import streamlit as st
from plot_utils import plot_data
from data.data_loading import load_data
from data.data_processing import *

def main():
    """Main function to create Streamlit dashboard."""
    st.title("Telecom User Behavior Analysis")

    # Load data
    file_path = "telecom_data.csv"  # Example file path
    data = load_data(file_path)

    # Task 1: Identify the top 10 handsets used by customers
    st.header("Top 10 Handsets Used by Customers")
    top_handsets_data = top_handsets(data)
    st.write(top_handsets_data)

    # Task 2: Identify the top 3 handset manufacturers
    st.header("Top 3 Handset Manufacturers")
    top_manufacturers_data = top_manufacturers(data)
    st.write(top_manufacturers_data)

    # Task 3: Identify the top 5 handsets per top 3 handset manufacturers
    st.header("Top 5 Handsets per Top 3 Handset Manufacturers")
    top_handsets_per_manufacturer_data = top_handsets_per_manufacturer(data)
    for manufacturer, handsets in top_handsets_per_manufacturer_data.items():
        st.subheader(manufacturer)
        st.write(handsets)
    
    st.subheader("Aggregate Information per User")
    user_aggregate = display_user_aggregate(data)
    st.write(user_aggregate.head())

    st.header("Task 1: Describe Variables and Data Types")
    variables_description = describe_variables(data)
    st.write(variables_description)

    # Task 2: Analyze basic metrics
    st.header("Task 2: Basic Metrics Analysis")
    basic_metrics_analysis = basic_metrics(data)
    st.write(basic_metrics_analysis)

    # Task 3: Non-Graphical Univariate Analysis
    st.header("Task 3: Non-Graphical Univariate Analysis")
    dispersion_params = dispersion_parameters(data)
    st.write(dispersion_params)

    # Task 4: Graphical Univariate Analysis
    st.header("Task 4: Graphical Univariate Analysis")

    # Call plot_univariate function and display histograms
    plots = plot_univariate(data)
    for plot in plots:
        st.pyplot(plot)
    
    # Calculate data volume
    app_data = calculate_data_volume(data)
    # Display the pie chart
    st.header("Distribution of Data Volume by Application")
    plt.figure(figsize=(10, 8))
    plt.pie(app_data, labels=app_data.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Data Volume by Application')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot()

    # Task 5: Bivariate Analysis
    st.header("Task 5: Bivariate Analysis")

    # Call bivariate_analysis function and display correlation matrices
    bivariate_results = bivariate_analysis(data)
    applications = ['Social Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']
    for app in applications:
        st.subheader(f"Correlation between {app} and Total DL+UL Data:")
        st.write(bivariate_results[app])
    # Task 6: Variable Transformations
    st.header("Task 6: Variable Transformations")
    variable_transformation = variable_transformations(data)
    st.write(variable_transformation)

    # Task 7: Correlation Analysis
    st.header("Task 7: Correlation Analysis")
    correlation_matrix = correlation_analysis(data)
    st.write(correlation_matrix)

    # # Task 8: Dimensionality Reduction
    # st.header("Task 8: Dimensionality Reduction")
    # explained_variance_ratio = dimensionality_reduction(data)
    # st.write(explained_variance_ratio)
    
    #  Perform dimensionality reduction using PCA
    explained_variance_ratio, transformed_data = dimensionality_reduction(data)

    # Get column names from the original data
    column_names = data.columns.tolist()

    # Display the results in the dashboard
    st.title('Dimensionality Reduction using PCA')

    # Interpretation of PCA results
    st.write("Interpretation of Principal Component Analysis:")
    st.write("- Variance Explained: PCA captures X% of the variance in the data.")
    st.write("- Principal Components: Features with higher loadings contribute more to the principal components.")
    st.write("- Feature Correlation: High correlations between original features and principal components indicate strong contributions.")
    st.write("- Dimension Reduction: PCA reduces the dimensionality of the data while preserving the most important information.")

    # Display explained variance ratio in a table
    variance_table = {"Column Name": column_names, "Explained Variance Ratio": explained_variance_ratio}
    st.write('Explained Variance Ratio:')
    st.table(variance_table)

    # Display transformed data
    st.write('Transformed Data:')
    st.write(transformed_data)
if __name__ == "__main__":
    main()

