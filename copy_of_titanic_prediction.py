# -*- coding: utf-8 -*-
"""Copy of Titanic Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzDzcALehrAwWl18pobjf8TxHCzWGnl3
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import os
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
# %matplotlib inline
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv('/content/drive/MyDrive/titanic.csv')

data.head()

data.isnull().sum()

train = pd.read_csv("/content/drive/MyDrive/titanic.csv")
test = pd.read_csv("/content/drive/MyDrive/titanic.csv")

train.isnull().sum()
print("Train Shape:",train.shape)
test.isnull().sum()
print("Test Shape:",test.shape)

train.info()

test.info()

data.info()

data.set_axis(['PassengerId','Survived','Pclass','PassengerName','Sex','Age','Sibsp','Parch','Ticket','Fare','Cabin','Embarked'], axis='columns',inplace=True)

data.head()

plt.figure(figsize=(12,7))
sns.heatmap(data.corr(),annot=True,cmap='pink')
plt.plot()

sns.pairplot(data,corner=True)
plt.show()

mean = data['Survived'].mean
mean()

sns.jointplot(data=data,x='Age',y='Survived',kind='reg')
plt.show()

fig=px.bar(data.head(100),x='PassengerId',y='Age',template='ggplot2')
fig.show()

fig=px.bar(data.head(100),x='Age',y='Survived',template='ggplot2')
fig.show()

fig = px.pie(data, values='Survived', names='Age')
fig.show()

fig = px.line(data, x="PassengerId", y="Age", color='Survived',markers=True,color_discrete_sequence=['white','orange'],template='plotly_dark')
fig.show()

df= data.copy()
df.head()

data.info()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
df['Embarked']=le.fit_transform(df['Embarked'])
df

from sklearn.model_selection import train_test_split
# Splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
for i in df.columns:
    if df[i].dtype == 'object':
        df[i]=l.fit_transform(df[i])

X = df.drop('Survived',axis=1)
y = df['Survived']

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=2)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier,ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier,BaggingClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
k_fold = KFold(n_splits=10, shuffle=True, random_state=0)

train.Cabin.value_counts()