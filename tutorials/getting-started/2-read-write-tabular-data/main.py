import os.path as path

import pandas as pd

# read Titanic data
titanic_csv = path.abspath(path.dirname(__file__) + "/../data/titanic.csv")
titanic = pd.read_csv(titanic_csv)

# print first 5 rows of the data frame
print(titanic.head())

# get age of the Titanic passengers
ages = titanic["Age"]
print(ages.head())
print(type(titanic["Age"]))
print(titanic["Age"].shape)

# get age and sex of Titanic passengers
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())

# get passengers older than 35 years
above_35_col = titanic["Age"] > 35
above_35 = titanic[above_35_col]
print(above_35.head())
print(above_35_col)
print(above_35.shape)

# get Titanic passengers from cabin class 2 and 3
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23.head())
class_23_filter = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23_filter.head())

# get passengers whose age are known
age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na.head())
print(age_no_na.shape)

# get names of the passengers older than 35 years
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names.head())

# get rows 10 till 25, and columns 3 to 5
print(titanic.iloc[9:25, 2:5])

# assign the name "anonymous" to first 3 elements of the fourth column
titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())
