# load modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# risk-free Treasury rate
R_f = 0.0175 / 252

# read in the market data
data = pd.read_csv('capm_market_data.csv')

#data.head()

data = data.drop('date', axis=1)

data.isna().sum()

pc = data.pct_change(axis=0)
pc.dropna(inplace=True)

print(pc.head(5))

aapl_returns = pc.aapl_adj_close.values
spy_returns = pc.spy_adj_close.values

type(aapl_returns)
type(spy_returns)

spy_returns[0:5]
aapl_returns[0:5]

ER_aapl = aapl_returns - R_f
y = ER_aapl
#ER_aapl

ER_spy = spy_returns - R_f
x = ER_spy
#ER_spy

print(ER_aapl[-5:])

print(ER_spy[-5:])

plt.scatter(ER_spy, ER_aapl)

ER_spy = ER_spy.reshape(-1,1)
ER_aapl = ER_aapl.reshape(-1,1)

x_T = ER_spy.transpose()
XTX = np.matmul(x_t, ER_spy)
inv_xtx = XTX ** -1
XTY = np.matmul(x_T,ER_aapl)
beta = np.matmul(inv_xtx,XTY)[0]
print(beta)


def beta_sensitivity(x, y):
    '''
    PURPOSE:

    INPUTS:
        x numpy arrays
        y numpy arrays
    OUTPUTS:
        a list of tuples. each tuple contains (observation row dropped, beta estimate)
    '''

    betas = []
    for i in range(0, len(x)):
        x_deleted = np.delete(x, i).reshape(-1, 1)
        y_deleted = np.delete(y, i).reshape(-1, 1)
        x_T = x_deleted.transpose()
        XTX = np.matmul(x_T, x_deleted)
        inv_xtx = XTX ** -1
        next_mat = np.matmul(inv_xtx, x_T)
        beta = np.matmul(next_mat, y_deleted)[0][0]
        betas.append((i, beta))

    return betas

betas = beta_sensitivity(x, y)
print(betas[:5])