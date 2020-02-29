from keras.datasets import cifar10

# Topics list
    # Exploring CIFAR10 dataset
    # understanding specific data points
    # formatting input images and labels

# Day 5 - 01. Exploring CIFAR10 Dataset

# note cifar 10 is too big to put on github, if you are running this program
# please download the image set locally

# x is input or images
# y is output or labels
(x_train, y_train), (x_test,y_test) = cifar10.load_data()
