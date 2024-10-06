Stock Price Prediction, Portfolio Manager, and Company Valuation Tool

A personal project to highlight the intersection of my expertise in computing
and market analysis, I want to create a python program that exploits financial 
data to make stock price projections. Additional features: portfolio class to allow
management of your portfolio, and an application that allows you to plug in data 
and outputs a calculated valuation for a company (perhaps in excel). 

I used to be reluctant to enter the world of stock trading and felt excluded
from learning more about the stock market. I felt it was out of reach for me and
beyond the scope of my abilities and financial stability. My money sat around,
collecting dust, losing value. Diving into the complex and dynamic world of 
the stock market has been tremendously fun, rewarding, and interesting. My biggest
hope for this project is to streamline the process of getting interested in 
stocks and help people make data-driven decisions about growing their money, and
adding features, kind of like DuoLingo, to make it fun for the users. I believe
everyone should be involved, as us investors dictate the free market Hayek 
identified many years ago.  

----

This Python project leverages financial data to predict future stock prices and calculate company valuations.

It includes:
- Stock Price Predictions: Using Prophet for time-series forecasting to predict future stock trends.
- Discounted Cash Flow (DCF) Valuation: Allows users to input financial metrics (like Free Cash Flow, Growth Rate, Discount Rate) 
    and outputs a company valuation based on a DCF model.
- Excel Integration: Users can input financial data via an Excel sheet for automated valuation calculations.

Features:
1. Stock Data Fetching: Automatically fetches historical stock data using `yfinance`.
2. Stock Price Prediction: Uses the Prophet model to predict stock prices into future years.
3. DCF Valuation: Calculates the DCF valuation based on user-provided financial metrics.
4. Excel Data Input: Optionally load user-provided input for DCF calculations from an Excel sheet.

Libraries Used:
- `yfinance`: To download historical stock price data.
- `pandas`: For data manipulation and analysis.
- `matplotlib`: To plot stock price trends.
- `prophet`: To perform time-series forecasting on stock data.
- `statsmodels`: For additional time-series modeling options.
- `openpyxl`: To load and read data from Excel files.
  
In the future, I want to be able to factor in Macro-economic inputs; 
non-historical and non-quantitative data will allow this model to be even better.
I also want to factor in things like tracking performance against
other companies in the industry, and even n-day moving averages.

