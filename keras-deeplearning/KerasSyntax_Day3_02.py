import keras

from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

# Day 3 Explore the Keras API
# 02. Understanding Keras Syntax

model = Sequential()

# Conv2D(
#   filters
#   kernel_size : size of kernel, what determines the output features
#   strides     : how we traverse the image matrix (like right one down one)
#   activation_function : neuron fires strongly or nah?
#   ...
#   )

conv_layer = Conv2D(filter=32, kernel_size=(3,3), activation='relu'))

max_pool_layer = MaxPooling2D(pool_size=(2,2))

dense_layer = Dense(1024, activation='softmax')

# drop half of the neurons during training with rate 0.5)
#   prevents from focusing on details that don't matter
#   dropping random also

dropout_layer = Dropout(rate=0.5)

model.add(conv_layer)
model.add(max_pool_layer)
model.add(dense_layer)
model.add(dropout_layer)

# in tensorflow this step is stupid complex
model.compile(optimizer=SGD, loss=0.01, metrics=['accuracy']) 

# need data to use this function
model.fit()
model.evaluate()
model.predict()
