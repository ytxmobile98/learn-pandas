from data.data import titanic

# get ages of Titanic passengers
ages = titanic["Age"]
print(ages.head())
print(type(ages))
print(ages.shape)

# get age and sex of Titanic passengers
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())
print(type(age_sex))
print(age_sex.shape)

# filter specific rows from a DataFrame

# Titanic passengers above 35
above_35 = titanic[ages > 35]
print(above_35.head())
print(ages > 35)
print(above_35.shape)

# Titanic passengers from cabin class 2 and 3
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23.head())
# alternative form
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23.head())

# Titanic passengers whose ages are known
age_no_na = titanic[ages.notna()]
print(age_no_na.head())
print(age_no_na.shape)

# Select specific rows and columns from a DataFrame
adult_names = titanic.loc[ages > 35, "Name"]
print(adult_names.head())

# Select rows 10 till 25 and columns 3 to 5
print(titanic.iloc[9:25, 2:5])

# Assign the name "anonymous" to the first 3 elements of the fourth column
titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())
