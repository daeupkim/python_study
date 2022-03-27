from load_stock_data import *
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

df = load_stock_data('./test_files/AAPL.xlsx')

scatter_matrix(df[['Open','High','Low','Close']], figsize=(6,6))
plt.show()
