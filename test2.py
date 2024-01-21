#  to print the historic data from a date to present
import yfinance as yf
import plotly.graph_objects as go

# Define the stock symbol and the time interval
stock_symbol = 'IDEA.NS'  # Change this to the appropriate symbol for IDEA stock on Yahoo Finance
interval = '5m'

# Fetch historical data
stock_data = yf.download(stock_symbol, period='3d', interval=interval)

# Print the data values
print("Stock Data:")
print(stock_data)

# Plot candlestick chart
fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                     open=stock_data['Open'],
                                     high=stock_data['High'],
                                     low=stock_data['Low'],
                                     close=stock_data['Close'])])

# Customize the layout
fig.update_layout(title=f'{stock_symbol} Stock - 3-Minute Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  xaxis_rangeslider_visible=False)

# Show the plot
fig.show()