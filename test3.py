import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Define the stock symbol and the time interval
stock_symbol = 'IDEA.NS'  # Change this to the appropriate symbol for IDEA stock on Yahoo Finance
interval = '2m'  # You can adjust the interval as needed, e.g., '1m' for 1-minute data

# Create an initial empty figure
fig = go.Figure()

# Customize the layout
fig.update_layout(title=f'{stock_symbol} Stock - Live Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  xaxis_rangeslider_visible=False)

# Display the initial figure
fig.show()

# Run the program until the Indian stock market is closed
market_close_time = datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)  # Assuming Indian market closes at 3:30 PM

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

        # Create a new trace for each update
        new_trace = go.Candlestick(x=live_data.index,
                                   open=live_data['Open'],
                                   high=live_data['High'],
                                   low=live_data['Low'],
                                   close=live_data['Close'])

        # Add the new trace to the figure
        fig.add_trace(new_trace)

        # Update the layout
        fig.update_layout(title=f'{stock_symbol} Stock - Live Candlestick Chart ({current_time})')

        # Pause for a few seconds before fetching the next data point
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {e}")
        # Pause for a longer time in case of an error to avoid excessive API calls
        time.sleep(60)

# The loop ends when the market is closed
print("Indian stock market is closed. Program terminated.")