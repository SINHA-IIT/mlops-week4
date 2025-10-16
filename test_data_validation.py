import pandas as pd

def test_column_names():
    df = pd.read_csv("data/data_iris.csv")
    expected = set(['sepal_length','sepal_width','petal_length','petal_width','species'])
    assert set(df.columns) == expected

def test_no_missing_values():
    df = pd.read_csv("data/iris.csv")
    assert df.isnull().sum().sum() == 0
