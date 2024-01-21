import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import test1 as t

# Define the stock symbol and the time interval
stock_symbol = 'IDEA.NS'  # Change this to the appropriate symbol for IDEA stock on Yahoo Finance
interval = '1d'  # Use daily data for historical analysis

# Fetch historical data for the last working day
last_working_day = datetime.now() - timedelta(days=1)
last_working_day_str = last_working_day.strftime('%Y-%m-%d')

try:
    historical_data = yf.download(stock_symbol, start=last_working_day_str, end=last_working_day_str, interval=interval)
    
    # Check if historical data is available
    if historical_data.empty:
        raise Exception(f"No historical data found for {stock_symbol} on {last_working_day_str}")
    
    # Calculate initial support and resistance levels based on historical data
    initial_support, initial_resistance = historical_data['Low'].min(), historical_data['High'].max()

    # Create an initial empty figure
    fig = go.Figure()

    # Customize the layout
    fig.update_layout(title=f'{stock_symbol} Stock - Live Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Stock Price',
                      xaxis_rangeslider_visible=False)

    # Display the initial figure with historical data
    fig.add_trace(go.Candlestick(x=historical_data.index,
                                 open=historical_data['Open'],
                                 high=historical_data['High'],
                                 low=historical_data['Low'],
                                 close=historical_data['Close']))

    # Add initial support and resistance lines
    fig.add_shape(
        type='line',
        x0=historical_data.index[0],
        x1=historical_data.index[-1],
        y0=initial_support,
        y1=initial_support,
        line=dict(color='red', width=2),
        name='Initial Support'
    )

    fig.add_shape(
        type='line',
        x0=historical_data.index[0],
        x1=historical_data.index[-1],
        y0=initial_resistance,
        y1=initial_resistance,
        line=dict(color='green', width=2),
        name='Initial Resistance'
    )

    # Display the initial figure
    fig.show()

except Exception as e:
    print(f"An error occurred: {e}")
