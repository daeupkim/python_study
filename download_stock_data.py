import yfinance as yf
import datetime

def download_stock_data(file_name, ticker, year1, month1, date1, year2, month2, date2):
    start = datetime.datetime(year1, month1, date1)
    end = datetime.datetime(year2, month2, date2)

    stock = yf.Ticker(ticker)

    hist = stock.history(start = start, end = end)
    hist.to_excel(file_name)

    return

download_stock_data('./test_files/AAPL.xlsx','AAPL',2021,1,1,2021,12,31)