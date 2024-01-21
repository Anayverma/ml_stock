import plotly.graph_objects as go

def plot_candlestick(data):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
    fig.update_layout(title='Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=False)
    fig.show()

def main():
    # Sample data
    initial_data = {
        'Open': [100, 110, 95, 105],
        'High': [120, 115, 100, 110],
        'Low': [90, 105, 90, 95],
        'Close': [115, 100, 105, 100]
    }

    # Create DataFrame
    import pandas as pd
    df = pd.DataFrame(initial_data)

    # Plot initial candlestick chart
    plot_candlestick(df)

    while True:
        try:
            # Get user input
            open_price = float(input('Enter Open price: '))
            high_price = float(input('Enter High price: '))
            low_price = float(input('Enter Low price: '))
            close_price = float(input('Enter Close price: '))

            # Update DataFrame
            df = pd.DataFrame({
                'Open': [open_price],
                'High': [high_price],
                'Low': [low_price],
                'Close': [close_price]
            })

            # Plot updated candlestick chart
            plot_candlestick(df)

        except ValueError:
            print('Invalid input. Please enter numeric values.')

if __name__ == "__main__":
    main()
