import pandas as pd

def test_amount_no_na():
    df = pd.read_parquet('data/clean_orders.parquet')
    assert not df['amount'].isna().any(), "❌ 'amount' column contains NaNs"

def test_non_empty():
    df = pd.read_parquet('data/clean_orders.parquet')
    assert len(df) > 0, "❌ Parquet file is empty"
