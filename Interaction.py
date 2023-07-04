import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the preprocessed data from Phase One
data = pd.read_csv('Data/full-diabetes.csv')

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(data.drop('Outcome', axis=1), data['Outcome'], test_size=0.2, random_state=42)

# Define the logistic regression model
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def loss(h, y):
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()


def add_intercept(X):
    intercept = np.ones((X.shape[0], 1))
    return np.concatenate((intercept, X), axis=1)


class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.theta = None
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose

    def fit(self, X, y):
        if self.fit_intercept:
            X = add_intercept(X)

        self.theta = np.zeros(X.shape[1])

        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= self.lr * gradient

            if self.verbose and i % 10000 == 0:
                z = np.dot(X, self.theta)
                h = sigmoid(z)
                print(f'Loss: {loss(h, y)}')

    def predict_proba(self, X):
        if self.fit_intercept:
            X = add_intercept(X)

        return sigmoid(np.dot(X, self.theta))

# Train the logistic regression model on the training set
lr = LogisticRegression(lr=0.1, num_iter=300000)
lr.fit(X_train, y_train)