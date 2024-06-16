# filename: ytd_stock_gains.py

import subprocess
import sys

# Ensure required packages are installed
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

try:
    import yfinance as yf
except ImportError:
    install('yfinance')
    import yfinance as yf

try:
    import matplotlib
    import matplotlib.pyplot as plt
except ImportError:
    install('matplotlib')
    import matplotlib
    import matplotlib.pyplot as plt

# Switch to a non-GUI backend
matplotlib.use('Agg')

# Define the ticker symbols
tickers = ['NVDA', 'TSLA']

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
plt.title('Cumulative YTD Stock Gains for NVDA and TSLA')
plt.ylabel('Gain %')
plt.xlabel('Date')
plt.grid(True)

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')

# Show the plot (optional, for user to see the plot)
plt.show()