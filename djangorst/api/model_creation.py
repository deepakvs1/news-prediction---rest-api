import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
import pickle

def model_creation():
    df = pd.read_json("E:\\News_Category_Dataset_v3.json",lines=True)
    df.head(5)

    X=df['short_description']
    Y=df['category']
    # print(Y)

    xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=.2,random_state=45)
    # # Create an instance of TfidfVectorizer
    vectorizer = TfidfVectorizer()
    # Fit the vectorizer on the training data and transform the training data into numerical features
    Xtrain_tfidf = vectorizer.fit_transform(xtrain)
    # Transform the test data into numerical features
    X_test_tfidf = vectorizer.transform(xtest)
    # # Assuming you have a trained vectorizer named 'vectorizer'
    with open('logisticvectorizer.pkl', 'wb') as file:
        pickle.dump(vectorizer, file)
   
    model = LogisticRegression()

    model.fit(Xtrain_tfidf, ytrain)

    with open('logisticmodel.pkl', 'wb') as file:
        pickle.dump(model, file)

    y_pred = model.predict(X_test_tfidf)

    accuracy = accuracy_score(ytest, y_pred)
    print("Accuracy:", accuracy)
# model_creation()    
def model_load(modelpath,vectorizerpath,input_text):   
    with open(modelpath, 'rb') as f:
        model = pickle.load(f)
        
    with open(vectorizerpath, 'rb') as f:
        vectorizer = pickle.load(f)    
        
    # Transform the input text into numerical features
    input_text_tfidf = vectorizer.transform([input_text])

    # Make prediction
    prediction = model.predict(input_text_tfidf)
    return prediction

    

# input_text = input("Enter the text to predict: ")
# modelpath = "C:\\Users\\user\\Desktop\\restapi\\REstapinew\\logisticmodel.pkl"
# vectorizerpath = "C:\\Users\\user\\Desktop\\restapi\\REstapinew\\logisticvectorizer.pkl"
# prediction = model_load(modelpath,vectorizerpath,input_text)
# print("Prediction:", prediction)


