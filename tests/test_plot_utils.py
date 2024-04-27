# test_plot_utils.py
import pytest
import matplotlib.pyplot as plt
from visualization.plot_utils import plot_data

@pytest.fixture
def sample_data():
    """Sample data for testing."""
    return [1, 2, 3, 4, 5]

def test_plot_data(sample_data):
    """Test plot data function."""
    # Call plot data function
    plt_obj = plot_data(sample_data)
    # Assert plot object is created
    assert isinstance(plt_obj, plt.Axes)  # Placeholder for actual assertion

