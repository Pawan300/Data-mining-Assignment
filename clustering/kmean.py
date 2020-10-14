import numpy as np
import pandas as pd
import os

class Kmeans:

    def __init__(self, k):
        self.data = None
        self.distance_mat = None
        self.cp = None
        self.k = k
        self.cluster_point=[""]*(k)
        self.cluster=[""]*k
    
    def loading_data(self, path):
        self.data = pd.read_csv(path)
        self.data = self.data.drop([self.data.columns[0],self.data.columns[1]],axis=1)
        self.data = self.data.values

    def clustered_data(self, cluster):
        temp=[]
        for i in range(len(cluster)):
            temp.append(pd.DataFrame(cluster[i])) 
        return(temp)

    def distance(self, m):
        self.distance_mat = np.array([[0] *self.data.shape[0] for i in range(len(m))])
        for i in range(len(m)):
            for j in range(self.data.shape[0]):  
                self.distance_mat[i][j]= np.sum(np.abs((self.data[m[i]]-self.data[j])))
         
    def minloc(self, x):
        m=min(x)
        l=[]
        for i in range(len(x)):
            if(m==x[i]):
                l.append(i)
        return(l)

    def cluster_equal(self, data1,data2):
        for i in range(len(data1)):
            if(np.array_equal(data1[i],data2[i])):
                continue
            else:
                return(False)
        return(True)
        
    def kmean(self):
        
        self.cp = np.random.randint(1, self.data.shape[0], self.k)
        self.cluster_point=list(map(lambda x:self.data[x], self.cp))

        def f(d):
            d = []
            return d

        for i in range(self.k):
            self.cluster = list(map(f,self.cluster))
            
            self.distance(self.cp)
            for j in range(self.distance_mat.shape[1]):
                temp = self.minloc(self.distance_mat[:,j])
                for L in range(len(temp)):
                    self.cluster[temp[L]].append(self.data[j])
            for i in range(len(self.cluster)):
                self.cluster[i] = np.array(self.cluster[i])
                self.cluster_point[i] = self.cluster[i].mean(axis=0)
        
def main():
    k = Kmeans(10)
    k .loading_data("College.csv")
    k.kmean()

    for i in range(len(k.cluster)):
        print("\n"+str(i)+"th cluster point is: \n")
        print("**************************************************")
        print(" Cluster : {} \n Cluster point : {}".format(k.cluster[i], k.cluster_point[i]))
    
if __name__=="__main__": 
    main() 