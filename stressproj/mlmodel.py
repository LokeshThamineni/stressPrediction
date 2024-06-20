
#importing required modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as rfc
import pickle
#importing dataset
stress_data = pd.read_csv('SaYoPillow.csv')
cpy=stress_data.copy(deep=True)
x=cpy.drop("sl",axis=1)
y=cpy["sl"]
#splitting data for training and testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=2)
#training RandomForestClassifier 
rfc = rfc(criterion = 'gini',max_depth=4)
ml = rfc.fit(x_train,y_train)
#storing the model into pkl file
pickle.dump(ml, open('stress.pkl', 'wb'))
