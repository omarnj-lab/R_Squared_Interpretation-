import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
sns.set()

df = pd.read_csv('data.csv')
plt.scatter(df['YearsExperience'], df['Salary'])

X = np.array(df['YearsExperience']).reshape(-1, 1)
y = df['Salary']
rf = LinearRegression()
rf.fit(X, y)
y_pred = rf.predict(X)

plt.scatter(df['YearsExperience'], df['Salary'])
plt.plot(X, y_pred, color='red')


def r2_score_from_scratch(ys_orig, ys_line):
    y_mean_line = [ys_orig.mean() for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)
def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))
r_squared = r2_score_from_scratch(y, y_pred)
print(r_squared)


r2_score(y, y_pred)











