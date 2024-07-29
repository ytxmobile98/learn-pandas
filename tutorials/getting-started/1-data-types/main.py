import pandas as pd

# initialize data
df = pd.DataFrame({
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
})
print(df)

# print "Age" series
print(df["Age"])

# create "Age" series
ages = pd.Series([22, 35, 58], name="Age")
print(ages)

# get max age
print(df["Age"].max())
print(ages.max())

# describe data
print(df.describe())
