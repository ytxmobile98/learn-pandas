from os import path

import pandas as pd

titanic_csv = path.abspath(path.dirname(__file__) + "/titanic.csv")
titanic = pd.read_csv(titanic_csv)
