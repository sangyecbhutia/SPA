
from stock_data import fetch_stock_data
from predictive_model import prophet_predict
from valuation_model import calculate_dcf
from user_input import load_inputs_from_excel

#step 1 --- fetch stock data
tickers = ['BFLY','NVDA', 'MSFT', 'MSTR', 'VRT', 'UBER', 'TSM', 'MSTR', 'AMZN', 'BTI', 'LX', 'AMD', 'VRT','SLB','TALO','VOO']  #list of stock tickers
stock_data = fetch_stock_data(tickers)

#step 2 --- predict stock prices 
prophet_predict(stock_data, 'BTI', years=5)
#for ticker in tickers:
    #prophet_predict(stock_data, ticker, years=5)
    

#step 3 --- load user input for DCF calculation (optional)
#free_cash_flow, growth_rate, discount_rate, terminal_value_multiple = load_inputs_from_excel()

#step 4 --- calculate DCF valuation
#company_valuation = calculate_dcf(free_cash_flow, growth_rate, discount_rate, terminal_value_multiple)
#print(f"Estimated Company Valuation: ${company_valuation:,.2f}")

# Next steps:
#factor in Macro-economic inputs; 
    # non-historical and non-quantitative data will allow this model to be even better.
# factor in things like tracking performance against other companies in the industry, and even n-day moving averages
#have a function that will allow the user to input a stock ticker and get a r
    #recommendation on whether to buy, sell, or hold the stock

#have a function to return the P/E, P/B, and P/S ratios for a given stock ticker

#*** ADVANCED ***
    #have a function to output relevant info about the stock,
    #such as recent news, company's sector, industry, and market cap

    #have a function to return the stock's volatility