import pytest
from sci_analyzer import SciDataAnalyzer

@pytest.fixture
def sample_data():
    return {
        "time_seconds": [1, 2, 3, 4, 5],
        "velocity_m_s": [10, 20, 30, 40, 50]
    }

def test_calculate_statistics(sample_data):
    analyzer = SciDataAnalyzer(sample_data)
    stats = analyzer.calculate_statistics("velocity_m_s")
    
    assert stats["mean"] == 30.0
    assert stats["median"] == 30.0
    assert round(stats["std_dev"], 2) == 15.81

def test_invalid_column(sample_data):
    analyzer = SciDataAnalyzer(sample_data)
    with pytest.raises(ValueError):
        analyzer.calculate_statistics("non_existent_column")