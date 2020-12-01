import pytest
import time 
import random

test_data = {
    "integer": {"input":[1,0,90,5,4,2],
                "expected": [0,1,2,4,5,90]
    },
    "float":{"input":[1.0,0.9,90.2,5.4,4.2,2.1,2.3,],
                "expected": [0.9, 1.0, 2.1, 2.3, 4.2, 5.4, 90.2]
    },
    "string": {"input":[ "ac", "foo","g", "a", "ab"],
                "expected": ["a", "ab", "ac", "foo","g"]

    }
}
@pytest.fixture
def Integer() -> dict:
    """Test integer list for sort Algortihms"""
    return test_data.get("integer")

@pytest.fixture
def Float() -> dict:
    """Test float list values for sort Algorithms"""
    return test_data.get("float")

@pytest.fixture
def String() -> dict:
    """Test string list values for sort Algorithms"""
    return test_data.get("string")

@pytest.fixture
def random_list()->list:
    """Random list for sorting and searching algorithms"""
    return [i * random.randint(0,100) for i in range(100*100)]
