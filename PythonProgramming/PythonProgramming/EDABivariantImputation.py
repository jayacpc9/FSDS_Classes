import pandas as pd
import numpy as np

# 1. Create the dataset
data = {
    'Category': ['Summer', np.nan, 'Winter', 'Rainy', 'Winter', 'Summer', 'Rainy', 'summer'],
    'temp': [45, 5, 13, 20, 10, 50, np.nan, 42]
}
df = pd.DataFrame(data)

# 2. Clean the text consistency issue
df['Category'] = df['Category'].str.lower()

# 3. Calculate the mean temperature for each known category
# winter: ~11.5, rainy: 18.0, summer: ~45.6
mean_temps = df.groupby('Category')['temp'].mean()
print(mean_temps)

mode_category = df.groupby('temp')['Category'].mode()
print(mode_category)

# 4. Fill NaN based on the closest matching group mean
def impute_season(row):
    if pd.isna(row['Category']):
        # Find the category with the minimum absolute temperature difference
        return (abs(mean_temps - row['temp'])).idxmin()
    return row['Category']

# 4. Fill NaN based on the closest matching group mean
def impute_temperature(row):
    if pd.isna(row['temp']):
        # Find the category with the minimum absolute temperature difference
        return (abs(mode_category - row['Category'])).idxmin()
    return row['temp']


df['Category'] = df.apply(impute_season, axis=1)
print(df)