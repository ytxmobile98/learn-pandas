from os import path

import pandas as pd

dir = path.dirname(__file__)

__csv_files = {
    "titanic": "titanic.csv",
}


def __read_file(name: str) -> pd.DataFrame:
    return pd.read_csv(path.join(dir, __csv_files[name]))


titanic = __read_file("titanic")
