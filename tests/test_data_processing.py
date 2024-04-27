import pytest
import pandas as pd
from data.data_processing import *
@pytest.fixture
def test_data():
    return pd.DataFrame({
        'Handset Type': ['iPhone', 'Samsung', 'Samsung', 'iPhone', 'Huawei'],
        'Handset Manufacturer': ['Apple', 'Samsung', 'Samsung', 'Apple', 'Huawei'],
        
    })

# Test top_handsets function
def test_top_handsets(test_data):
    result = top_handsets(test_data)
  

# Test top_manufacturers function
def test_top_manufacturers(test_data):
    result = top_manufacturers(test_data)
    

# Test top_handsets_per_manufacturer function
def test_top_handsets_per_manufacturer(test_data):
    result = top_handsets_per_manufacturer(test_data)
   

# Test display_user_aggregate function
def test_display_user_aggregate(test_data):
    result = display_user_aggregate(test_data)
  

# Test describe_variables function
def test_describe_variables(test_data):
    result = describe_variables(test_data)
    

# Test basic_metrics function
def test_basic_metrics(test_data):
    result = basic_metrics(test_data)
  

# Test dispersion_parameters function
def test_dispersion_parameters(test_data):
    result = dispersion_parameters(test_data)
   

# Test plot_univariate function
def test_plot_univariate(test_data):
    result = plot_univariate(test_data)


# Test calculate_data_volume function
def test_calculate_data_volume(test_data):
    result = calculate_data_volume(test_data)
    

# Test bivariate_analysis function
def test_bivariate_analysis(test_data):
    result = bivariate_analysis(test_data)
    

# Test variable_transformations function
def test_variable_transformations(test_data):
    result = variable_transformations(test_data)
   

# Test correlation_analysis function
def test_correlation_analysis(test_data):
    result = correlation_analysis(test_data)
   

# Test dimensionality_reduction function
def test_dimensionality_reduction(test_data):
    result = dimensionality_reduction(test_data)
    
