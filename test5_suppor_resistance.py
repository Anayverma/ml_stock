import yfinance as yf
from datetime import datetime, timedelta
import time
import test1 as t

# Define the stock symbol and the time interval
stock_symbol = 'IDEA.NS'  # Change this to the appropriate symbol for IDEA stock on Yahoo Finance
interval = '1m'  # You can adjust the interval as needed, e.g., '1m' for 1-minute data

# Run the program until the Indian stock market is closed
market_close_time = datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)  # Assuming Indian market closes at 3:30 PM

# Initialize variables to track the best buying and selling opportunities
best_buy_start_time = None
best_sell_start_time = None
consistent_increase_count = 0
consistent_decrease_count = 0
last_close_value = None

# Initialize variables for dynamic support and resistance levels
support_levels = []
resistance_levels = []

def calculate_support_resistance(data):
    # Calculate support and resistance levels based on historical data
    support_level = data['Low'].min()
    resistance_level = data['High'].max()
    return support_level, resistance_level

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
            consistent_decrease_count = 0
        elif last_close_value is not None and current_values['Close'] < last_close_value:
            consistent_decrease_count += 1
            consistent_increase_count = 0
            best_sell_start_time = current_time
        else:
            consistent_increase_count = 0
            consistent_decrease_count = 0
            best_buy_start_time = current_time
            best_sell_start_time = current_time

        # Update the last close value
        last_close_value = current_values['Close']

        # Check if it's the best time to buy
        if consistent_increase_count >= 15:
            print(f"Best time to buy! Consistent increase for 15 minutes starting from {best_buy_start_time}")
            consistent_increase_count = 0
            t.placeorder("IDEA-EQ", "14366", 1, 'NSE', 'BUY', 'MARKET', 0)

        # Check if it's the best time to sell
        if consistent_decrease_count >= 15:
            print(f"Best time to sell! Consistent decrease for 15 minutes starting from {best_sell_start_time}")
            consistent_decrease_count = 0
            t.placeorder("IDEA-EQ", "14366", 1, 'NSE', 'SELL', 'MARKET', 0)

        # Check for dynamic support and resistance levels
        support, resistance = calculate_support_resistance(live_data)
        support_levels.append(support)
        resistance_levels.append(resistance)

        # Print the current five support and resistance levels
        if len(support_levels) >= 5 and len(resistance_levels) >= 5:
            s1, s2, s3 = support_levels[-3:]
            r1, r2, r3 = resistance_levels[-3:]
            print(f"Current Support Levels: s1={s1}, s2={s2}, s3={s3}")
            print(f"Current Resistance Levels: r1={r1}, r2={r2}, r3={r3}")

        # Pause for a few seconds before fetching the next data point
        time.sleep(60)

        # Check if the stock crosses support or resistance levels
        if current_values['Close'] > resistance:
            print(f"Stock crossed above the resistance level at {current_time}!")
        elif current_values['Close'] < support:
            print(f"Stock crossed below the support level at {current_time}!")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Pause for a longer time in case of an error to avoid excessive API calls
        time.sleep(60)

# The loop ends when the market is closed
print("Indian stock market is closed. Program terminated.")
