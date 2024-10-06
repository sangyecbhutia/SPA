import yfinance as yf

class Portfolio:
    '''
    A class to represent a stock portfolio.
    '''
    def __init__(self):
        self.holdings = {}

    def __str__(self):
        return f"Portfolio: {self.holdings}"

    def add_stock(self, ticker, shares, purchase_price):
        '''
        Add stock purchases to the portfolio.
        '''
        if ticker not in self.holdings:
            self.holdings[ticker] = {'shares': shares, 'purchase_history': [(shares, purchase_price)]}
        else:
            #update total shares and append to purchase history
            self.holdings[ticker]['shares'] += shares
            self.holdings[ticker]['purchase_history'].append((shares, purchase_price))

        #update the average purchase price of the stock
        total_shares = sum([key[0] for key in self.holdings[ticker]['purchase_history']])
        avg_price = sum([key[0] * key[1] for key in self.holdings[ticker]['purchase_history']]) / total_shares
        self.holdings[ticker]['purchase_price'] = avg_price


    def update_prices(self):
        '''
        Update the current price of all stocks in the portfolio.
        '''
        for ticker in self.holdings:
            current_price = yf.Ticker(ticker).history(period='1d')['Close'].iloc[0]
            self.holdings[ticker]['current_price'] = current_price

    def portfolio_value(self):
        '''
        Calculate the total value of the portfolio.
        '''
        total_value = 0
        for _, data in self.holdings.items():
            total_value += data['shares'] * data['current_price']
        return total_value
    
    def total_profit(self):
        '''
        Calculate the total profit of the portfolio.
        '''
        total_profit = 0
        for _, data in self.holdings.items():
            total_profit += data['shares'] * (data['current_price'] - data['purchase_price'])
        return total_profit

    def show_holdings(self):
        '''
        Print the holdings of the portfolio.
        '''
        for ticker, data in self.holdings.items():
            print(f"{ticker}: {data['shares']} shares at ${data['purchase_price']:,.2f}, current price: ${data['current_price']:,.2f}")
        print(f"Total portfolio value: ${self.portfolio_value():,.2f}")

    def remove_stock(self, ticker):
        '''
        Remove a stock from the portfolio.
        '''
        if ticker in self.holdings:
            del self.holdings[ticker]
        else:
            print(f"{ticker} not found in the portfolio")
    
    def percentage_return(self):
        '''
        Calculate the weighted percentage return of the portfolio.
        '''
        total_cost = sum([key['shares'] * key['purchase_price'] for key in self.holdings.values()])
        if total_cost == 0:
            return 0 #avoid division by zero
        total_profit = self.total_profit()
        return (total_profit / total_cost) * 100 #percentage return


    def stock_percentage_return(self, ticker):
        '''
        Calculate the percentage return of a specific stock in the portfolio.
        '''
        return (self.holdings[ticker]['current_price'] - self.holdings[ticker]['purchase_price']) / self.holdings[ticker]['purchase_price'] * 100
    
    def stock_volatility(self, ticker):
        '''
        Calculate the volatility of a stock.
        '''
        #fetch historical stock data
        stock_data = yf.Ticker(ticker).history(period='1y')['Close']
        #calculate the daily returns
        daily_returns = stock_data.pct_change().dropna() #dropna() drops first day to which there is no previous
        #calculate the standard deviation of daily returns
        volatility = daily_returns.std() * (252**0.5) #annualized volatility
        #approx 252 trading days in a year, annualize the volatility
        #annualized volatility = daily volatility * sqrt(252)
        #volatility is sqrt of variance

        return volatility
    
#my portfolio:
portfolio = Portfolio()
portfolio.add_stock(ticker='NVDA', shares=1.5, purchase_price=118)
portfolio.add_stock(ticker='MSTR', shares=2, purchase_price=139)
portfolio.add_stock(ticker='MSTR', shares=1, purchase_price=156)
portfolio.update_prices() #update to the current prices of the stocks
portfolio.show_holdings() #print the holdings and value of the portfolio
print(f"Percentage return overall: {portfolio.percentage_return():,.2f}%") #print the percentage return of the portfolio
for ticker in portfolio.holdings:
    print(f"Percentage return for {ticker}: {portfolio.stock_percentage_return(ticker):,.2f}%") #print the percentage return for each stock in the portfolio
    print(f"Annual volatility for {ticker}: {portfolio.stock_volatility(ticker):,.2f}%") #print the volatility of MSTR
print(f"Total profit: ${portfolio.total_profit():,.2f}") #print the total profit of the portfolio

