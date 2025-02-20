# Portfolio Optimization using CVXPY

This project demonstrates a basic portfolio optimization workflow using Python. The main file ([main.py](main.py)) downloads historical stock data, computes returns, and optimizes a portfolio by minimizing the variance. A pie chart is then generated to visualize the optimal portfolio weights.

## Features

- **Data Download**: Uses [yfinance](https://pypi.org/project/yfinance/) to download historical stock prices for selected tickers (AAPL, AMZN, GOOGL, MSFT, MSTR).
- **Data Processing**: 
  - Extracts the "Close" prices from the downloaded data.
  - Calculates daily percentage returns.
  - Computes the covariance matrix of the returns.
- **Portfolio Optimization**: 
  - Uses [cvxpy](https://www.cvxpy.org/) to define and solve a quadratic programming problem that minimizes the portfolio variance subject to the constraint that the sum of the weights equals 1.
  - Prints out the raw computed weights.
- **Visualization**: 
  - Clips negative weights for visualization purposes and normalizes them.
  - Displays a pie chart of the portfolio weights with [matplotlib](https://matplotlib.org/).

## Requirements

Make sure you have the following packages installed:

- Python 3.x
- `cvxpy`
- `numpy`
- `pandas`
- `yfinance`
- `matplotlib`
- `IPython`

You can install these dependencies via pip:

```sh
pip install cvxpy numpy pandas yfinance matplotlib ipython
```
How to Run
- From the terminal, navigate to your project directory and run:
```sh
python main.py
```
- Or run it through a Jupiter notebook
  
## python code walkthrough

## Data Download:

- The script starts by downloading historical data for the specified tickers from January 1, 2002, to January 1, 2025.
- It checks if the data or the "Close" prices are empty, raising errors if either is the case.

## Data Processing:

- The "Close" prices are extracted and printed for reference.
- Daily percentage returns are calculated, and from these returns, the covariance matrix is computed.

## Portfolio Optimization:

- A cvxpy variable is defined for the portfolio weights.
- The portfolio variance is formulated as a quadratic form using the covariance matrix.
- A constraint is applied to ensure that the sum of weights equals 1.
- The optimization problem is solved to minimize the variance.

## Output and Visualization:

- The computed optimal weights are printed to the console.
- To make the results more intuitive, negative weights are clipped and the remaining ones normalized.
- A pie chart representing the portfolio allocation is displayed using matplotlib.
- This project is provided for educational purposes.

