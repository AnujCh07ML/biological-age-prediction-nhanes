from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def linear_model():

    return LinearRegression()


def random_forest():

    return RandomForestRegressor(
        n_estimators=200,
        max_depth=None,
        random_state=42
    )
