import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# Create a dummy dataframe with a linear trend and some random noise
dates = pd.date_range(start='2020-01-01', end='2021-12-31', freq='D')
data = np.arange(len(dates)) + np.random.randn(len(dates)) * 10
df = pd.DataFrame(data=data, index=dates, columns=['value'])

# Method 1: Rolling statistics using Pandas
rolling_mean = df.rolling(window=30).mean()
rolling_std = df.rolling(window=30).std()

plt.plot(df, label='Original')
plt.plot(rolling_mean, label='Rolling Mean')
plt.plot(rolling_std, label='Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show()

# Method 2: Regression using statsmodels
model = sm.OLS(df, sm.add_constant(df.index)).fit()
print(model.summary())

# Method 3: Regression using scikit-learn
X = df.index.values.reshape(-1, 1)
y = df.values.reshape(-1, 1)
model = LinearRegression().fit(X, y)
print('Trend:', model.coef_[0][0])
