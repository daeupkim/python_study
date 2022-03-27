import pandas as pd

def load_stock_data(file_name):
    df = pd.read_excel(file_name)
    # print(df.describe())

    return df
