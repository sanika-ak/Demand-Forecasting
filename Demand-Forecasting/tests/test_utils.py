from demand_forecast.utils import load_data
import pandas as pd

def test_load_data(tmp_path):
    # create a temporary CSV
    d = tmp_path / "data.csv"
    d.write_text("col1,col2\n1,2\n3,4")

    df = load_data(d)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
