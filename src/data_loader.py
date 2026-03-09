import pandas as pd


def load_cycle(demo_path, cbc_path, cycle_label):

    demo = pd.read_sas(demo_path)
    cbc = pd.read_sas(cbc_path)

    df = pd.merge(demo, cbc, on="SEQN")

    df["cycle"] = cycle_label

    return df


def load_all_cycles():

    df_2011 = load_cycle(
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Demographics_data/2011-12/DEMO_G.xpt.txt",
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Laboratory_data/2011-12/CBC_G.xpt.txt",
        "2011-2012"
    )

    df_2013 = load_cycle(
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Demographics_data/2013-14/DEMO_H.xpt.txt",
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Laboratory_data/2013-14/CBC_H.xpt.txt",
        "2013-2014"
    )

    df_2015 = load_cycle(
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Demographics_data/2015-16/DEMO_I.xpt.txt",
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Laboratory_data/2015-16/CBC_I.xpt.txt",
        "2015-2016"
    )

    df_2017 = load_cycle(
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Demographics_data/2017-20/P_DEMO.xpt.txt",
        "/Users/anuj/Documents/DataSet's/Cell_Prediction_data/Laboratory_data/2017-20/P_CBC.xpt.txt",
        "2017-2020"
    )

    df_all = pd.concat(
        [df_2011, df_2013, df_2015, df_2017],
        ignore_index=True
    )

    return df_all
