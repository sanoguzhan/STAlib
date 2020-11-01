import pytest
from stalib.errors import STALibValidationError

def test_value_error():
    """
    Test for Error Message displayed correctly with given input"""
    assert "For Algorithms Data should be homogenous" == str(STALibValidationError("Test"))