import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date='2015-01-01', end_date=None):
    """
    Fetch historical stock data for given tickers.
    """
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Function for correlation matrix (optional)
def compute_correlation(stock_data):
    return stock_data.corr()
