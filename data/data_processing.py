import pandas as pd
def top_handsets(data):
    """Identify the top 10 handsets used by customers."""
    top_handsets = data['Handset Type'].value_counts().head(10)
    return top_handsets

def top_manufacturers(data):
    """Identify the top 3 handset manufacturers."""
    top_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
    return top_manufacturers

def top_handsets_per_manufacturer(data):
    """Identify the top 5 handsets per top 3 handset manufacturers."""
    top_manufacturers = data['Handset Manufacturer'].value_counts().head(3).index
    top_handsets_per_manufacturer = {}
    for manufacturer in top_manufacturers:
        top_handsets_per_manufacturer[manufacturer] = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
    return top_handsets_per_manufacturer

def display_user_aggregate(data):
    user_aggregate = data.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',
        'Dur. (ms)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum',
        'Social Media DL (Bytes)': 'sum',
        'Social Media UL (Bytes)': 'sum',
        'Google DL (Bytes)': 'sum',
        'Google UL (Bytes)': 'sum',
        'Email DL (Bytes)': 'sum',
        'Email UL (Bytes)': 'sum',
        'Youtube DL (Bytes)': 'sum',
        'Youtube UL (Bytes)': 'sum',
        'Netflix DL (Bytes)': 'sum',
        'Netflix UL (Bytes)': 'sum',
        'Gaming DL (Bytes)': 'sum',
        'Gaming UL (Bytes)': 'sum',
        'Other DL (Bytes)': 'sum',
        'Other UL (Bytes)': 'sum'
    })
    return user_aggregate

def describe_variables(data):
    """Describe all relevant variables and associated data types."""
    return data.dtypes


def basic_metrics(data):
    """Analyze basic metrics in the dataset."""
    return data.describe()


def dispersion_parameters(data):
    """Conduct Non-Graphical Univariate Analysis."""
    numeric_data = data.select_dtypes(include=['number'])  # Filter numeric columns
    return numeric_data.quantile([0.25, 0.5, 0.75])

import matplotlib.pyplot as plt



def plot_univariate(data):
    """Conduct Graphical Univariate Analysis."""
    plots = []
    applications = ['Social Media', 'Google', 'Email', 'Youtube','Netflix', 'Gaming', 'Other']
    for app in applications:
        ul_column = f"{app} UL (Bytes)"
        dl_column = f"{app} DL (Bytes)"
        # Calculate the sum of UL and DL for each application
        data[f"{app} Total (Bytes)"] = data[ul_column] + data[dl_column]
        plt.figure(figsize=(8, 6))
        plt.hist(data[f"{app} Total (Bytes)"])
        plt.title(f"{app} Total Data Distribution")
        plt.xlabel("Total Data (Bytes)")
        plt.ylabel("Frequency")
        plot = plt.gcf()  # Get the current figure
        plots.append(plot)
    return plots

def calculate_data_volume(data):
    """Calculate the total data volume for each application."""
    columns_of_interest = ['Social Media DL (Bytes)', 'Social Media UL (Bytes)',
                           'Youtube DL (Bytes)', 'Youtube UL (Bytes)',
                           'Netflix DL (Bytes)', 'Netflix UL (Bytes)',
                           'Google DL (Bytes)', 'Google UL (Bytes)',
                           'Email DL (Bytes)', 'Email UL (Bytes)']
    
    # Sum the data for each application
    app_data = data[columns_of_interest].sum()
    return app_data

def bivariate_analysis(data):
    """Conduct Bivariate Analysis."""
    bivariate_results = {}
    applications = ['Social Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']
    for app in applications:
        dl_column = f"{app} DL (Bytes)"
        ul_column = f"{app} UL (Bytes)"
        correlation = data[['Total DL (Bytes)', 'Total UL (Bytes)', dl_column, ul_column]].corr()
        bivariate_results[app] = correlation
    return bivariate_results

def variable_transformations(data):
    """Variable Transformations."""
    data['Total Duration Decile'] = pd.qcut(data['Dur. (ms)'], 5, labels=['D1', 'D2', 'D3', 'D4', 'D5'])
    decile_data = data.groupby('Total Duration Decile')[['Total DL (Bytes)', 'Total UL (Bytes)']].sum()  # Use list instead of tuple
    return decile_data



def correlation_analysis(data):
    """Correlation Analysis."""
    selected_columns = ['Social Media DL (Bytes)', 'Social Media UL (Bytes)', 'Google DL (Bytes)', 
                        'Google UL (Bytes)', 'Email DL (Bytes)', 'Email UL (Bytes)', 
                        'Youtube DL (Bytes)', 'Youtube UL (Bytes)', 'Netflix DL (Bytes)', 
                        'Netflix UL (Bytes)', 'Gaming DL (Bytes)', 'Gaming UL (Bytes)', 
                        'Other DL (Bytes)', 'Other UL (Bytes)']
    correlation_matrix = data[selected_columns].corr()
    return correlation_matrix


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def dimensionality_reduction(data):
    # Drop non-numeric columns and columns containing datetime values
    numeric_data = data.select_dtypes(include=['number'])

    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)

    # Perform PCA
    pca = PCA()
    pca.fit(scaled_data)

    # Calculate explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_

    # Return explained variance ratio and transformed data
    return explained_variance_ratio, pca.transform(scaled_data)
