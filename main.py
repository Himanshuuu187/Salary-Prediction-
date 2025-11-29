import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

df = pd.read_csv("Salary_dataset.csv")


x = df.iloc[:,1:2]
y = df.iloc[:,2:3]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)

lr = LinearRegression()
lr.fit(x_train,y_train)

lr.predict(x_test.iloc[0].values.reshape(1,1))


m = lr.coef_
b = lr.intercept_


Experience = float(input("Enter your Years of Experience: "))

result = m*Experience + b

print("Your predicted Salary is: ",int(result[0][0]))
