from sklearn.linear_model import LinearRegression

def train_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model