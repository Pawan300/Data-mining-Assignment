import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from matplotlib import pyplot as ppt
data=pd.read_csv(r"G:\practicals\fundamental of d.s\pca.csv")
train,test=train_test_split(data,test_size=0.4)
x=np.matrix(train)
train_scalar=preprocessing.StandardScaler()
train_scalar.fit(train)
s_data=train_scalar.transform(train)
data_cov=np.cov(s_data,rowvar=False)
eigen=np.linalg.eigh(data_cov)
pc1=[]
error=[]
l=[i for i in range(1,14)]
for i in range(1,14):
   pc1.append(eigen[1][-i])
   pc=np.matrix(pc1)
   x_bar=(pc.T.dot(pc.dot(x.T))).T
   er=x-x_bar
   error.append(np.sqrt((1/er.shape[0])*np.sum(np.square(er))))
ppt.plot(l,error)
