import numpy as np
import random
import pickle
import matplotlib.pyplot as plt
"""
    Back propagation program with for loop was so long to compile
    so we use Vectorization the reduce the complexity of code
    (use matrix instead of for loop)
    so we can tran with more data 
"""
number_of_train = 200
number_of_epochs = 10
batch_size = 10
batch_num = 20
learning_rate = 0.3
total_costs = []


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

# with some epochs and batches find the cost and accuracy we can say we do
    # back propagation epoch's time so the result can be more accurate with matrix
for epoch in range(number_of_epochs):   #5
    random.shuffle(train_set)
    train_set1 = train_set[:number_of_train]
    for batch in range (batch_size):   #10
        # random the weight and bias of layers
        W1_grad = np.zeros((150, 102))
        W2_grad = np.zeros((60, 150))
        W3_grad = np.zeros((4, 60))
        b1_grad = np.zeros((150, 1))
        b2_grad = np.zeros((60, 1))
        b3_grad = np.zeros((4, 1))

        for k in range (batch_num):      #20
            image = train_set1[batch * 20 + k][0]
            label_grad = train_set1[batch * 20 + k][1]
            sig_y_grad = 1 / (1 + pow(np.e, -(W1 @ image + b1)))
            sig_z_grad = 1 / (1 + pow(np.e, -(W2 @ sig_y_grad + b2)))
            sig_c_grad = 1 / (1 + pow(np.e, -(W3 @ sig_z_grad + b3)))

            W3_grad += (2 * (sig_c_grad - label_grad) * sig_c_grad * (1 - sig_c_grad)) @ np.transpose(sig_z_grad)

            # bias
            b3_grad += 2 * (sig_c_grad - label_grad) * sig_c_grad * (1 - sig_c_grad)

            #3rd layer
            delta_3 = np.zeros((60, 1))
            delta_3 += np.transpose(W3) @ (2 * (sig_c_grad - label_grad) * (sig_c_grad * (1 - sig_c_grad)))

            # weight
            W2_grad += (sig_z_grad * (1 - sig_z_grad) * delta_3) @ np.transpose(sig_y_grad)

            # bias
            b2_grad += delta_3 * sig_z_grad * (1 - sig_z_grad)

            #2nd layer
            delta_2 = np.zeros((150, 1))
            delta_2 += np.transpose(W2) @ (delta_3 * sig_z_grad * (1 - sig_z_grad))

            # weight
            W1_grad += (delta_2 * sig_y_grad * (1 - sig_y_grad)) @ np.transpose(image)

            # bias
            b1_grad += delta_2 * sig_y_grad * (1 - sig_y_grad)

        # upgrade the weights and layers
        W3 = W3 - (learning_rate * (W3_grad / batch_size))
        W2 = W2 - (learning_rate * (W2_grad / batch_size))
        W1 = W1 - (learning_rate * (W1_grad / batch_size))
        b3 = b3 - (learning_rate * (b3_grad / batch_size))
        b2 = b2 - (learning_rate * (b2_grad / batch_size))
        b1 = b1 - (learning_rate * (b1_grad / batch_size))

    cost = 0
    for train_data in train_set[:number_of_train]:    #200
        x_grad = train_data[0]
        sig_y_grad = 1 / (1 + pow(np.e, -(W1 @ x_grad + b1)))
        sig_z_grad = 1 / (1 + pow(np.e, -(W2 @ sig_y_grad + b2)))
        sig_c_grad = 1 / (1 + pow(np.e, -(W3 @ sig_z_grad + b3)))
        for j in range(4):
            cost += np.power((sig_c_grad[j, 0] - train_data[1][j, 0]), 2)
        label_grad = train_data[1]

    cost /= number_of_train
    total_costs.append(cost)

# show the plot of epoch size and total cost of each
epoch_size = [x+1 for x in range(number_of_epochs)]
plt.plot(epoch_size, total_costs)
plt.show()

# find the accuracy of train
counter = 0
for train_data in train_set[:number_of_train]:
    x_grad = train_data[0]
    sig_y_grad = 1 / (1 + pow(np.e, -(W1 @ x_grad + b1)))
    sig_z_grad = 1 / (1 + pow(np.e, -(W2 @ sig_y_grad + b2)))
    sig_c_grad = 1 / (1 + pow(np.e, -(W3 @ sig_z_grad + b3)))
    predicted_number = np.where(sig_c_grad == np.amax(sig_c_grad))
    real_number = np.where(train_data[1] == np.amax(train_data[1]))
    if predicted_number == real_number:
        counter += 1
print('Accuracy:', counter / number_of_train)

