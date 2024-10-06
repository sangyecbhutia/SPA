import matplotlib.pyplot as plt
from prophet import Prophet

def prophet_predict(stock_data, ticker, years=5):
    """
    Function to predict stock price for the next years using Prophet
    - stock_data: historical stock data.
    - ticker: stock symbol to predict.
    - years: number of years into the future to predict (default is 5 years)
    """
    #prepare the dataframe for Prophet
    df = stock_data[[ticker]].reset_index() #reset the index to get the 'Date' column
    df.columns = ['ds', 'y'] #rename the columns to 'ds' and 'y'
    
    #remove timezone from the 'ds' column since its no longer supported in pandas 
    df['ds'] = df['ds'].dt.tz_localize(None) 
    
    #initialize and fit the model
    model = Prophet()
    model.fit(df)
    
    #create a future dataframe for the next years
    future = model.make_future_dataframe(years * 365) #in days
    
    #make prediction
    forecast = model.predict(future)
    
    #plot the forecast along with historical data to visualize the prediction
    model.plot(forecast)
    plt.title(f"{ticker} Stock Price Prediction for Next {years} Years")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()
    
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
