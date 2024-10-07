import yfinance as yf

def fetch_stock_data(tickers, start_date='2015-01-01', end_date=None):
    """
    Fetch historical stock data for given tickers.
    """
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data
