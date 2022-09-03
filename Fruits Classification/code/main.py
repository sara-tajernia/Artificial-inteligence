import numpy as np
import random
import pickle
"""
    This project is FeedForward it the first we got some random number
    and pass them through 2 hidden layer and in the end find the cost and 
    accuracy of random numbers to find out how many of the guesses were true
"""

number_of_train = 200

# loading training set features
f = open("Datasets/train_set_features.pkl", "rb")
train_set_features2 = pickle.load(f)
f.close()

# reducing feature vector length
features_STDs = np.std(a=train_set_features2, axis=0)
train_set_features = train_set_features2[:, features_STDs > 52.3]

# changing the range of data between 0 and 1
train_set_features = np.divide(train_set_features, train_set_features.max())

# loading training set labels
f = open("Datasets/train_set_labels.pkl", "rb")
train_set_labels = pickle.load(f)
f.close()

# ------------
# loading test set features
f = open("Datasets/test_set_features.pkl", "rb")
test_set_features2 = pickle.load(f)
f.close()

# reducing feature vector length
features_STDs = np.std(a=test_set_features2, axis=0)
test_set_features = test_set_features2[:, features_STDs > 48]

# changing the range of data between 0 and 1
test_set_features = np.divide(test_set_features, test_set_features.max())

# loading test set labels
f = open("Datasets/test_set_labels.pkl", "rb")
test_set_labels = pickle.load(f)
f.close()

# ------------
# preparing our training and test sets - joining datasets and lables
train_set = []
test_set = []

for i in range(len(train_set_features)):
    label = np.array([0, 0, 0, 0])
    label[int(train_set_labels[i])] = 1
    label = label.reshape(4, 1)
    train_set.append((train_set_features[i].reshape(102, 1), label))

for i in range(len(test_set_features)):
    label = np.array([0, 0, 0, 0])
    label[int(test_set_labels[i])] = 1
    label = label.reshape(4, 1)
    test_set.append((test_set_features[i].reshape(102, 1), label))

random.shuffle(train_set)
random.shuffle(test_set)

# random the weight and bias of layers
W1 = np.random.normal(size=(150,102))
W2 = np.random.normal(size=(60, 150))
W3 = np.random.normal(size=(4, 60))
b1 = np.ones((150, 1))
b2 = np.ones((60, 1))
b3 = np.ones((4, 1))

# find the sigmoid of each node with formula 1/(1+e^(-W+sig last node + bias)
for i in range (number_of_train):
    sig_y = 1/(1 + pow(np.e, -(W1 @ train_set[i][0] + b1)))
    sig_z = 1 / (1 + pow(np.e, -(W2 @ sig_y + b2)))
    sig_c = 1 / (1 + pow(np.e, -(W3 @ sig_z + b3)))

# find the accuracy of nodes by counting how many are fruits were guesses true
counter = 0
for i in range (number_of_train):
    label = train_set[i][1]
    if sig_c.tolist().index(max(sig_c)) == label.tolist().index(max(label)):
        counter+=1
print('Accuracy: ', counter/number_of_train)
