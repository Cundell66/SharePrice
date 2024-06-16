import yfinance as yf
import matplotlib.pyplot as plt

ticker1 = input("Enter first ticker: ")
ticker2 = input("Enter second ticker: ")

# Define the ticker symbols
tickers = [ticker1, ticker2]

# Define the start and end dates
start_date = '2024-01-01'
end_date = '2024-06-16'

# Fetch the stock data
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Calculate cumulative daily gains
daily_gains = data.pct_change().add(1).cumprod().subtract(1).multiply(100)

# Create a line plot for cumulative gains
plt.figure(figsize=(10, 6))
daily_gains.plot()
plt.title(f'Cumulative YTD Stock Gains for {ticker1} and {ticker2}')
plt.ylabel('Gain %')
plt.xlabel('Date')
plt.grid(True)

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')

# Show the plot (optional, for user to see the plot)
plt.show()