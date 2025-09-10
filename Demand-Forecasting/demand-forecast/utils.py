import pandas as pd
import numpy as np

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)
