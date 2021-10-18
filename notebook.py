import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from datetime import datetime as dt

# Supress Warnings
import warnings
warnings.filterwarnings('ignore')

df_heart = pd.read_csv('./data/cardio_train.csv', delimiter=';')
df_food = pd.read_csv('./data/nutrition.csv')

# display of the first row of each datasets
df_heart.head()
df_food.head()

# Show the number of missing value
df_heart.isnull().sum()
df_food.isnull().sum()

# Show the internal structure of the datasets
df_heart.info()
df_food.info()

# Data cleaning

# We will only use the colomns that concern heart desease, such as cholesterols
# and sugars.
# Thus, we will have to drop all the units behind those data to make them a
# Float type.
# As for the heart desease one, we will use the colomns of cholesterols and
# sugar as well and the target one.

# Droping all columns besides the three that are interesting
df_food = df_food.filter(['name', 'cholesterol', 'sugars'])

# Transforming the data to be numerical
df_food['cholesterol'] = df_food['cholesterol'].str.replace('mg','')
df_food['cholesterol'] = df_food['cholesterol'].astype(int)

df_food['sugars'] = df_food['sugars'].str.replace(' g','')
df_food['sugars'] = df_food['sugars'].astype(float)

# Droping id since it doesn't give any information
df_heart = df_heart.drop('id', axis=1)

# Data analysis

# First of all, we need to determine if a high cholesterol and sugars in blood
# make the persons more likely to have heart desease.
fig, ax = plt.subplots(figsize=(14, 14))
sns.heatmap(df_heart.corr(), annot=True, linewidths=0.4, fmt='.1f', ax=ax)
plt.show()
st.pyplot()

# From that we can see that the age, the weight and the ammout of cholesterol
# are variable that correlate with having heart deasease
# Systolic and diastolic blood presure and sugar have also a small impact on
# the chance to have heart desease

# We divise the cholesterol level accordind to the sugar level
chol_0 = df_heart.loc[df_heart['gluc'] == 1]
chol_1 = df_heart.loc[df_heart['gluc'] == 2]
chol_2 = df_heart.loc[df_heart['gluc'] == 3]
sns.distplot(chol_0['cholesterol'], color='blue', hist=False, label='normal sugar level')
sns.distplot(chol_1['cholesterol'], color='red', hist=False, label='high sugar level')
sns.distplot(chol_2['cholesterol'], color='green', hist=False, label='very high sugar level')
plt.legend()
plt.show()
st.pyplot()
# As we can see, people with very high sugar level, tend to have very high
# cholesterol level too.

# Since we saw that people with high cholesterol tend to also have high sugar
# level, we have to see if that it is also true for food.
fig, ax = plt.subplots(figsize=(2, 2))
sns.heatmap(df_food.corr(), annot=True, linewidths=0.4, fmt='.1f', ax=ax)
plt.show()
st.pyplot()
# No corelation between sugar and cholesterol.
# Despite the fact that people with high cholesterol have high
# sugar level, it is not due to one type of food.


# Sorting foods by cholesterol rate
sort_chol = df_food.sort_values(['cholesterol'], ascending=False)
print(sort_chol.head(25))
st.write(sort_chol.head(25))
# As we can see, foods with the most cholesterol are veal, beef, pork,
# lamb and eggs.

# Conclusion

# People with heart desease are most likely people with high cholesterol
# that could mean that cholesterol is a factor for heart desease.
# Theremore, veal, beef, pork, lamb and eggs have the most cholesterol levels
# among food, so we can conclude that consuming large ammount of those kind of
# food can lead to a greater chance to have heart deseases.