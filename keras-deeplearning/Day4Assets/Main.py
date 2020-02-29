import keras

from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

model = Sequential()

conv_layer = Conv2D(filter=32, kernel_size=(3, 3), activation='relu')
max_pool_layer = MaxPooling2D(pool_size=(2, 2))
dense_layer = Dense(10, activation='softmax')
dropout_layer = Dropout(rate=0.5)

model.add(conv_layer)
model.add(max_pool_layer)
model.add(dense_layer)
model.add(dropout_layer)
model.add(dense_layer)

model.compile(optimizer=SGD, loss=0.01, metrics=['accuracy'])
model.fit()
model.evaluate()
model.predict()
