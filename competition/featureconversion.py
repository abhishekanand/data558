# Make sure generated Feautures and Labels in right directory  

import pickle
import pandas as pd


# TRAIN Labels and Feautures
print("\n TRAIN")
 
test_features = pickle.load(open('./test_features/features','rb'))
#print(test_features)
test_featuresdf=pd.DataFrame(test_features)
print("\n test_features")
#print(test_featuresdf.shape)
test_featuresdf.to_csv("test_features/test_features.csv")

print("\n TRAIN")
test_labels = pickle.load(open('./test_features/labels','rb'))
#print(test_labels.shape)
test_labelsdf=pd.DataFrame(test_labels)
print("\n test_labels")
#print(test_labelsdf.shape)
test_labelsdf.to_csv("test_features/test_labels.csv")

# TEST Labels and Feautures

print("\n TEST")

train_features = pickle.load(open('./train_features/features','rb'))
#print(train_features.shape)
train_featuresdf=pd.DataFrame(train_features)
#print("\n train_features")
print(train_featuresdf.shape)
train_featuresdf.to_csv("train_features/train_features.csv")


print("\n TEST")
train_labels = pickle.load(open('./train_features/labels','rb'))
#print(train_labels.shape)
train_labelsdf=pd.DataFrame(train_labels)
print("\n test_labels")
#print(train_labelsdf.shape)
train_labelsdf.to_csv("train_features/train_labels.csv")
