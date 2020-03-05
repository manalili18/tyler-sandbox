from keras.datasets import cifar10
import matplotlib.pyplot as plt
import keras.utils as utils
import numpy as np

# Topics list
    # Exploring CIFAR10 dataset
    # understanding specific data points
    # formatting input images and labels

# Day 5 - 01. Exploring CIFAR10 Dataset

# note cifar 10 is too big to put on github, if you are running this program
# please download the image set locally

# x is input or images
# y is output or labels
#(x_train, y_train), (x_test,y_test) = cifar10.load_data()

# more descriptive setup
# each variable is an array / list
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# matrix form each image is 32x32 pixels (x3 subpixels RGB)
#   each subpixel has 

# whole image
# print(train_images[0])

# First row of pixels
# print(train_images[0][0])

# First pixel
# print(train_images[0][0][0])

# R value of first pixel (out of R G B )
# print(train_images[0][0][0][0])

#plt.imshow(train_images[0])
#plt.show()

labels_array = ['airplane', 'car', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck']

# testing label correct labeled first picture
#print(labels_array[train_labels[0][0]])

# looking at how keras stores labels
# the following lines will interpret the output, then
# display the category of the image
train_labels = utils.to_categorical(train_labels)
max_index = np.argmax(train_labels[0])
# print(train_labels[0])
print(labels_array[max_index])


