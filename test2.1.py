# to print five suppport and rsistance level from past data 
import yfinance as yf

# Define the stock symbol and the time interval
stock_symbol = 'IDEA.NS'  # Change this to the appropriate symbol for IDEA stock on Yahoo Finance
interval = '5m'

# Fetch historical data
stock_data = yf.download(stock_symbol, period='3d', interval=interval)

# Print the data values
print("Stock Data:")
print(stock_data)

# Calculate support and resistance levels based on historical data
support_level = stock_data['Low'].min()
resistance_level = stock_data['High'].max()

# Print the 5 support and resistance levels
print(f"\nSupport Level: {support_level}")
print(f"Resistance Level: {resistance_level}")

# If you want to print the 5 most recent levels, you can use tail
last_five_support_levels = stock_data['Low'].tail(5).tolist()
last_five_resistance_levels = stock_data['High'].tail(5).tolist()

print("\nLast 5 Support Levels:")
print(last_five_support_levels)

print("\nLast 5 Resistance Levels:")
print(last_five_resistance_levels)
