import pandas as pd
# import numpy as np


def data_processing():
    df = pd.read_csv('./server/dp/datasets/epi_r.csv')
    de10 = df.head(10)
    return de10
