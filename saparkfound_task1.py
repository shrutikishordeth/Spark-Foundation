# -*- coding: utf-8 -*-
"""SaparkFound_task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UmSgBGoCWT0fbhiscdB9czCfgP_qcQ7L

**Prediction using Supervised ML**

Task:- Predict the percentage of an student based on the no. of study hours.

**Deth Shruti Kishor**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline

url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
s_data.head(5)

"""Let's visiualize data"""

s_data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()

"""Dividing the data into inputs and outputs"""

x = s_data.iloc[:, :-1].values  
y = s_data.iloc[:, 1].values  
print("Inputs = ",x)
print("Outputs = ",y)

"""Spilting tha dataset into training dataset and testing dataset"""

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0) 
print("x_train = ",X_train)
print("X_test = ",X_test)
print("y_train = ",y_train)
print("y_test = ",y_test)

"""Training the model"""

from sklearn.linear_model import LinearRegression  
reg = LinearRegression()  
reg.fit(X_train, y_train) 

print("Training complete.")

"""Plotting regression line"""

line = reg.coef_*X+reg.intercept_

# Plotting for the test data
plt.scatter(X, y)
plt.plot(X, line);
plt.show()

"""Testing the model"""

y_pred = reg.predict(X_test)
print("Actual output = ",y_test)
print("Predicted output = ",y_pred)

"""Predicting score if a student studies for 9.25 hrs/ day"""

h=[[9.25]]
y_pred=reg.predict(h)
print("Predicted score for 9.25 hrs/day = ",y_pred)