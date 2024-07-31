from os import path

import pandas as pd

dir = path.dirname(__file__)

titanic_csv = path.join(dir, "titanic.csv")
titanic = pd.read_csv(titanic_csv)
