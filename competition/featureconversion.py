import pickle
import pandas as pd
 
test_features = pickle.load(open('./test_features/features','rb'))
#print(test_features.shape)
tfdf=pd.DataFrame(test_features)
print("\n test_features")
print(tfdf.shape)

tfdf.to_csv("test_features/test_features.csv")


test_labels = pickle.load(open('./test_features/labels','rb'))
#print(test_labels.shape)
tldf=pd.DataFrame(test_labels)
print("\n test_labels")
print(tldf.shape)
tldf.to_csv("test_features/test_labels.csv")

print("\n TEST")
train_features = pickle.load(open('./train_features/features','rb'))
#print(train_features.shape)
trfdf=pd.DataFrame(train_features)
print("\n train_features")
print(trfdf.shape)

trfdf.to_csv("train_features/train_features.csv")

print("\n TEST")
train_labels = pickle.load(open('./train_features/labels','rb'))
#print(train_labels.shape)
trldf=pd.DataFrame(train_labels)
print("\n test_labels")
print(trldf.shape)

trldf.to_csv("train_features/train_labels.csv")
