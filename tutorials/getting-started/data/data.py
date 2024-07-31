from os import path

import pandas as pd

dir = path.dirname(__file__)


def __read_file(name: str) -> pd.DataFrame:
    return pd.read_csv(path.join(dir, name))


air_quality = __read_file("air_quality_no2.csv")
titanic = __read_file("titanic.csv")
