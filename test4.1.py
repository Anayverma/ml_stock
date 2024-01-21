import yfinance as yf
from datetime import datetime, timedelta
import time
import test1 as t

def check_support_resistance(current_values, support_levels, resistance_levels):
    current_close = current_values['Close']
    for support_level in support_levels:
        if current_close <= support_level:
            print(f"Stock has crossed below support level: {support_level}")

    for resistance_level in resistance_levels:
        if current_close >= resistance_level:
            print(f"Stock has crossed above resistance level: {resistance_level}")

# Define the stock symbol and the time interval
stock_symbol = 'IDEA.NS'  # Change this to the appropriate symbol for IDEA stock on Yahoo Finance
interval = '1m'  # You can adjust the interval as needed, e.g., '1m' for 1-minute data

# Define user-defined support and resistance levels
support_levels = [13.35,13.30,13.25]  # Add your support levels
resistance_levels = [13.50,13.55,13.60]  # Add your resistance levels

# Run the program until the Indian stock market is closed
market_close_time = datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)  # Assuming the Indian market closes at 3:30 PM

# Initialize variables to track the best buying opportunity
consistent_increase_count = 0
last_close_value = None

while datetime.now() < market_close_time:
    try:
        # Fetch live data
        live_data = yf.download(stock_symbol, period='1d', interval=interval)

        # Get the last row of the live data
        current_values = live_data.iloc[-1]

        # Print live updated current values
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current Values ({current_time}):")
        print(current_values)

        # Check if the close value has increased
        if last_close_value is not None and current_values['Close'] > last_close_value:
            consistent_increase_count += 1
        else:
            consistent_increase_count = 0

        # Update the last close value
        last_close_value = current_values['Close']

        # Check support and resistance levels
        check_support_resistance(current_values, support_levels, resistance_levels)

        # Check if it's the best time to buy
        if consistent_increase_count >= 15:
            print(f"Best time to buy! Consistent increase for 15 minutes starting from {current_time}")
            consistent_increase_count = 15
            t.placeorder("IDEA-EQ", "14366", 1, 'NSE', 'BUY', 'MARKET', 0)

        # Pause for a few seconds before fetching the next data point
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {e}")
        # Pause for a longer time in case of an error to avoid excessive API calls
        time.sleep(60)

# The loop ends when the market is closed
print("Indian stock market is closed. Program terminated.")
