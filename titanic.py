import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn as sklearn

titanic_data = pd.read_csv('train.csv')
""" print (titanic_data.head())
print (titanic_data.info())
print (titanic_data.describe())
print (titanic_data.isnull().sum())
print (titanic_data['Survived'].value_counts()) 
print (titanic_data['Pclass'].value_counts())
print (titanic_data.tail()) """



test = pd.read_csv("test.csv")

#remove age from the dataset
titanic_data = titanic_data.drop(['Age','Cabin','Ticket','Name', 'Embarked','SibSp','Parch', 'Fare'], axis=1)
test = test.drop(['Age','Cabin','Ticket','Name'], axis=1)
#the colum sex is categorical we need to convert it into numerical
titanic_data['Sex'] = titanic_data['Sex'].map({'male': 0, 'female': 1})
titanic_data['Pclass'] = titanic_data['Pclass'].map({1: 0, 2: 1, 3: 2})
test['Pclass'] = test['Pclass'].map({1: 0, 2: 1, 3: 2})
#one hot encoding
#drop the pclass 1 mapping  
#titanic_data = titanic_data.drop(columns=1, axis=1)
#test = test.drop('First', axis=1)
test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})

print (titanic_data.head())
print (titanic_data.info())
print (titanic_data.describe())
print (titanic_data.isnull().sum())   
#drop the female column
#titanic_data = titanic_data.drop('Female', axis=1)
#test = test.drop('female', axis=1)    
# split the train.csv into 75 25 ratio
from sklearn.model_selection import train_test_split
train, val = train_test_split(titanic_data, test_size=0.25, random_state=42)    
# get logistic regression from sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


