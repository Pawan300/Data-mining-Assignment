import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class KNN:

    def __init__(self):

        self.train = None
        self.test = None
        self.y_test = None
        self.y_train = None
        self.distance = []
        self.sol = []

    def loading_data(self, path):

        data = pd.read_csv(path)
        self.train, self.test = train_test_split(data, train_size=0.7)
        self.y_train = self.train[" Class_label"]
        self.train = self.train.drop([self.train.columns[4]],axis=1)
        self.y_test = self.test[" Class_label"]
        self.test = self.test.drop([self.test.columns[4]],axis=1)
        self.test = self.test.values

    def eucledian_dist(self, l):

        for i in range(self.train.shape[0]):
            self.distance.append(np.sqrt(np.sum(np.square(self.train.iloc[i]-l))))
        
    def knn(self, l,k):
        
        i_vi=0
        i_s=0
        i_ve=0
        
        self.eucledian_dist(l)
        
        for i in range(k):

            t = min(self.distance)
            for i in range(len(self.distance)):
                if(self.distance[i]==t):
                    t=i
                    break        
            if(self.y_train.iloc[t]=="Iris-setosa"):
                i_s+=1
            elif(self.y_train.iloc[t]=="Iris-virginica"):
                i_vi+=1
            else:
                i_ve+=1
            self.distance.remove(min(self.distance))
        if(max(i_vi,i_s,i_ve)==i_vi):
            return("Iris-virginica")
        elif(max(i_vi,i_s,i_ve)==i_ve):
            return("Iris-versicolor")
        else:
            return("Iris-setosa")

    def predict(self, k):
        for i in range(self.test.shape[0]):
            self.sol.append(self.knn(self.test[i],k))
        self.sol = np.array(self.sol)        
        self.sol = self.sol.T
    
    def error(self):
        er=0
        for i in range(len(self.sol)):
            if(self.sol[i] != self.y_test.iloc[i]):
                er+=1
        return(er/len(self.sol))

def main():

    k = KNN()
    k.loading_data("iris.csv")
    k.predict(5)
    
if __name__ == "__main__":
    main()