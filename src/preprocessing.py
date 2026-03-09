
from config import FEATURES, TARGET


def prepare_data(df):

    df_model = df[FEATURES + [TARGET]].dropna()

    X = df_model[FEATURES]
    y = df_model[TARGET]

    return X, y
