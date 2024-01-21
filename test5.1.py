import yfinance as yf
from datetime import datetime, timedelta

# Define the stock symbol and the time interval
stock_symbol = 'IDEA.NS'  # Change this to the appropriate symbol for IDEA stock on Yahoo Finance
interval = '1m'  # Use daily data for historical analysis

# Fetch historical data for the specified date
specified_date = '2023-11-19'  # Adjust the date as needed
try:
    historical_data = yf.download(stock_symbol, start=specified_date, end=specified_date, interval=interval)
    
    # Check if historical data is available
    if historical_data.empty:
        raise Exception(f"No historical data found for {stock_symbol} on {specified_date}")
    
    # Calculate initial support and resistance levels based on historical data
    initial_support, initial_resistance = historical_data['Low'].min(), historical_data['High'].max()

    # Display the information in a table
    print(f"Stock Symbol: {stock_symbol}")
    print(f"Date: {specified_date}")
    print("\nHistorical Data:")
    print(historical_data)
    
    print("\nCalculated Support and Resistance Levels:")
    print(f"Initial Support: {initial_support}")
    print(f"Initial Resistance: {initial_resistance}")

except Exception as e:
    print(f"An error occurred: {e}")
