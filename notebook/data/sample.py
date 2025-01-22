from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score


# Define the custom `__sklearn_tags__` method
def custom_sklearn_tags(self):
    return {
        "estimator_type": "regressor",
        "requires_positive_y": False,
    }


# Monkey-patch the XGBRegressor class
XGBRegressor.__sklearn_tags__ = custom_sklearn_tags

# Generate dummy data
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Split the data
X_train, X_test, y_train, y_test = X[:80], X[80:], y[:80], y[80:]

# Define the model and parameter grid
model = XGBRegressor()
param_grid = {"n_estimators": [50, 100], "learning_rate": [0.01, 0.1]}

# Perform GridSearchCV
try:
    grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring="r2")
    grid.fit(X_train, y_train)

    # Evaluate the best model
    best_model = grid.best_estimator_
    y_pred = best_model.predict(X_test)
    print(f"R2 Score: {r2_score(y_test, y_pred)}")
except Exception as e:
    print(f"Error: {e}")
