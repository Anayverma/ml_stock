# with graph
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Fetch historical data
stock_symbol = 'EURUSD=X'  # Change to your desired stock symbol
df = yf.download(stock_symbol, start='2021-01-01', end='2021-12-31', progress=False)

# Check if NA values are in data
df = df[df['Volume'] != 0]
df.reset_index(drop=True, inplace=True)
df.isna().sum()

def support(df1, l, n1, n2):
    if l - n1 + 1 < 0 or l + n2 >= len(df1):
        return 0  # Index out of bounds, cannot calculate support
    for i in range(l - n1 + 1, l + 1):
        if df1['Low'][i] > df1['Low'][i - 1]:
            return 0
    for i in range(l + 1, l + n2 + 1):
        if df1['Low'][i] < df1['Low'][i - 1]:
            return 0
    return 1

def resistance(df1, l, n1, n2):
    if l - n1 + 1 < 0 or l + n2 >= len(df1):
        return 0  # Index out of bounds, cannot calculate resistance
    for i in range(l - n1 + 1, l + 1):
        if df1['High'][i] < df1['High'][i - 1]:
            return 0
    for i in range(l + 1, l + n2 + 1):
        if df1['High'][i] > df1['High'][i - 1]:
            return 0
    return 1

# Example: Calculate support and resistance for a specific candle
support_level = support(df, 30, 3, 5)
resistance_level = resistance(df, 30, 3, 5)
print("Support Level:", support_level)
print("Resistance Level:", resistance_level)

# Plot candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()
