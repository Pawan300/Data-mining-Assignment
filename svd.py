import numpy as np
import pandas as pd
from sklearn import preprocessing
from matplotlib import pyplot
d=pd.read_csv(r"C:\Users\pawan_300\Desktop\Project work\fundamental of d.s\College.csv")
data=d.drop([d.columns[0],d.columns[1]],axis=1)
scalar=preprocessing.StandardScaler()
scalar.fit(data)
data=scalar.transform(data)
A=data
def plot(u,v,s):
    err=[]
    err.append(error(u,v,s))
    for i in range(s.shape[1]-1,0,-1):
       s[i][i]=0
       err.append(error(u,v,s))
    l=[i for i in range(s.shape[1])]
    pyplot.plot(l,err) 
    return(err)
def error(u,v,s):
   Anew=u.dot(s.dot(v.T))
   er=A-Anew
   n=er.shape[0]
   return(np.sqrt((1/n)*np.sum(np.square(er))))   
def svd():
    e_aat=np.linalg.eig(A.dot(A.T))
    e_ata=np.linalg.eig(A.T.dot(A))
    u=e_aat[1].T
    v=e_ata[1].T
    e=e_aat[0]
    s=np.zeros(A.shape)
    e=sorted(e,reverse=True)
    e=np.sqrt(e)
    np.fill_diagonal(s,e)
    return(u,v,s)
    
