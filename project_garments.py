# -*- coding: utf-8 -*-
"""project_garments.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qf1yRcX4vsMVd5rW1QE-DeyXEN6vknaA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/content/garments_worker_productivity.csv')
df

df.head()

df.tail()

df.columns

df.dtypes

# datatype changing : date , quarter , department , day

from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
df['date']=lab.fit_transform(df['date'])
df['quarter']=lab.fit_transform(df['quarter'])
df['department']=lab.fit_transform(df['department'])
df['day']=lab.fit_transform(df['day'])

df.isna().sum()

df.drop(['wip'],axis=1,inplace=True)
df

#heat map for finding corelation :
sns.heatmap(df.corr())

#dropping the columns which has less corelation
df.drop(['no_of_style_change','idle_men','team','smv'],axis=1,inplace=True)
df

df.isna().sum()

plt.scatter(df['incentive'],df['actual_productivity'],color='r')
plt.xlabel("incentive")
plt.ylabel("actual_productivity")

sns.barplot(x="quarter",y="actual_productivity", data=df, palette="icefire")

sns.boxplot(x="department",y="actual_productivity" ,hue="day", data=df , palette="icefire")

sns.barplot(x="day",y="actual_productivity",data=df,palette="coolwarm")

sns.barplot(x="targeted_productivity",y="actual_productivity",data=df,palette="coolwarm")

x=df.iloc[:,:-1]
x

y=df.iloc[:,-1]
y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42)
x_train

import seaborn as sns
sns.regplot(x=df['targeted_productivity'],y=y,color='r')

sns.regplot(x=df['incentive'],y=y,color='b')

sns.regplot(x=df['no_of_workers'],y=y,color='k')

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)
x_train

# model creationn
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
y_pred

y_test

# performance matrics
from sklearn.metrics import mean_absolute_error,mean_squared_error
mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
rmse=np.sqrt(mse)
print('mse :',mse)
print('mae :',mae)
print('rmse :',rmse)

from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)
score

print('slope is')
print(model.coef_)

print('constant is')
print(model.intercept_)

residuals=y_test-y_pred
print(residuals)

sns.displot(residuals,kind='kde')

plt.scatter(y_pred,residuals)