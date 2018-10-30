"""

USC Hackathon Project - Class Design
"""
import random

class Data:
    def __init__(self):
        self.positive_datasets  =[]
        self.negative_datasets = []
        self.total = []
        self.cleaned = []
    def scrape_positive(self):
        # Scrape data using WireShark
        # Access packet information
        # Get the following fields:
        # sourcemac, destmac,sourceip,destip,protocol,port numbers,etc
        print("scraping positive datasets")
        self.positive_datasets = [1,1,2,4,5]*5 #for simplicity# .

    def scrape_negative(self):
        # Analyze LAN Traffic from Portland Oregon
        # + other data sources.
        print("scraping negative datasets")

        self.negative_datasets  = [1,3,4,5,1]*5 ## for simplicity.

    def combine(self):
        print("combining positive and negative datasets")
        self.total = self.positive_datasets +  self.negative_datasets
        random.shuffle(self.total)

    def clean(self):
        ### return the cleaned version of the self.total data.
        # Cleaning :
        # 1. Map protocols to integers.
        # 2. normalize port numbers to small range.
        # 3. create hashmaps of sourceip,destip,sourcemac,destmac
        # 4. resolve hosts with protocol.
        print("cleaning datasets")
        self.cleaned = self.total

class Model:
    def __init__(self):
        self.model = None
        self.parameters = []
        self.train = []
        self.test = []
        self.accuracy = 0

    def split_train_test(self,total):
        print("splitting the data into train and test")
        self.train = total[:int(len(total)*0.7)]
        self.test = total[int(len(total)*0.7):]

    def KNN(self,train,test):
        # def train():
            self.model = "KNN"  ## build the model here.
            print("KNN")
        # def test():
            correct = 40 ### for simplicity
            total = len(train)+len(test)
            self.accuracy  = (correct/total) * 100

    def LogisticRegression(self,train,test):
        # def train():
            self.model = "Logistic Regression"  ## build the model here.
            print("Logistic Regression")
        # def test():
            correct = 46 ### for simplicity
            total = len(train)+len(test)
            self.accuracy  = (correct/total) * 100



if __name__ == '__main__':
    d = Data()
    d.scrape_negative()
    d.scrape_positive()
    d.combine()
    model = Model()
    model.split_train_test(d.total)
    model.KNN(model.train,model.test)
    print("accuracy",model.accuracy)
    model.LogisticRegression(model.train,model.test)
    print("accuracy",model.accuracy)

