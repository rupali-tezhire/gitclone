# test_pandas_version.py

import pandas as pd

# Define the expected version
EXPECTED_PANDAS_VERSION = "2.2.3"  # Replace with your desired version

# Test function
def test_pandas_version():
    installed_version = pd.__version__
    assert installed_version == EXPECTED_PANDAS_VERSION, f"Expected pandas version {EXPECTED_PANDAS_VERSION}, but got {installed_version}"
