from os import path

import pandas as pd

dir = path.dirname(__file__)

# data for sections
titanic = pd.read_csv(path.join(dir, "titanic.csv"))
air_quality = pd.read_csv(path.join(dir, "air_quality_no2.csv"),
                          index_col=0, parse_dates=True)
air_quality_long = pd.read_csv(path.join(dir, "air_quality_long.csv"),
                               index_col="date.utc", parse_dates=True)
