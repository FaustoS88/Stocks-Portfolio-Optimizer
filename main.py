import cvxpy as cp
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from IPython.display import display

# Define assets and download data
tickers = ['AAPL', 'AMZN', 'GOOGL', 'MSFT','MSTR']
data = yf.download(tickers, start='2002-01-01', end='2025-01-01')

if data.empty:
    raise ValueError("No data downloaded!")

# Extract Close Prices from MultiIndex DataFrame
try:
    close_prices = data['Close']
except KeyError:
    raise ValueError("Expected 'Close' column in the downloaded data.")

if close_prices.empty:
    raise ValueError("Close prices DataFrame is empty!")

# Display the extracted Close Prices for reference
print("Extracted Close Prices:")
display(close_prices)

# Compute daily returns and covariance matrix
returns = close_prices.pct_change().dropna()
cov_matrix = returns.cov().values

# Portfolio Optimization using cvxpy: Minimize portfolio variance
n = len(tickers)
w = cp.Variable(n)
portfolio_variance = cp.quad_form(w, cov_matrix)
constraints = [cp.sum(w) == 1]  # Allowing short selling; hence no non-negativity constraint

prob = cp.Problem(cp.Minimize(portfolio_variance), constraints)
prob.solve()

# Display the raw optimal weights
optimal_weights = w.value
print("Optimal Portfolio Weights (raw):")
for idx, weight in enumerate(optimal_weights):
    print(f"{tickers[idx]}: {weight:.4f}")

# For visualization, clip negative weights then normalize so they sum to 1.
vis_weights = np.clip(optimal_weights, 0, None)
if vis_weights.sum() > 0:
    vis_weights = vis_weights / vis_weights.sum()

plt.figure(figsize=(6, 6))
plt.pie(vis_weights, labels=tickers, autopct='%1.1f%%', startangle=140)
plt.title("Optimal Portfolio Weights (for visualization)")
plt.show()