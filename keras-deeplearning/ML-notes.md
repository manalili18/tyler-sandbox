# Deep Learning / Machine Learning Notes
The following are notes I've taken from a machine learning masterclass on
stackskills.com. Days 1 and 2 are basics of Python.

## Day 3: Understand Machine Learning Neural Networks
### 01. Intro to Machine learning
- basic definition: machines ability to learn from previous experience
- programs should get better with increased exposure to relevant data
- examples
    - opt, prediction, classifications
    - stock market prediction or image recognition
        - stock market hard
        - image recog easy and can use simple machines
- many different algorithms
    - we will use convolutional NN trained with supervised learning

#### 4 steps
1. processing 
    - more relevant == more accurate
    - gather a lot of data is time consuming
        - a lot of preformatted databases online
        - data collection can be the most frustrating
    - data formatting must be the same and easily interpreted
    - divide data into training and testing sets and label the data

2. building
    - write algortithms
    - clever way to interpret 
    - decide which model works best for our problem (conv nn)
    - construct computational graph
    - interconnected nodes that hold values or ops and maps pathways from 
        inputs to outputs
    - graph is where all the calc happens
    - time consuming

3. training
    - model is only as good as the data
    - during training, becoming more accurate
    - run training set for learning
    - minimize loss (the difference between NN answers vs 'correct' answers)

4. testing
    - run it on data it has never seen before
    - convert output into something meaningful to us

#### Extra learning
- checkout other ML algos

### 02. Intro to Neural Networks

#### What is a nerual net?
- connected notes with weights and biases and data flows through it from input
    to output
- set of algorithms designed to recognize patterns
- hand drawn digit recognition
    - model recognizes patterns of dark against light paper
- derived from the structure model of the human brain
- several layers containing operations to process inputs or map pathways through 
    the net to produce outputs
- focus mostly on network layers (dense or connected)
    - network, dense, and connected refer to the same thing

- layers of mini networks of many interconnected nodes each with assigned weights
    and biases
- biases are some constant value
- models learn the pathways and adjust neuron weights during training

### 03. Intro to Convolutions

#### what are convolutional neural net
- neural net interconnected nodes in dense layer 
- before we feed into this dense layer series of convolutions and max pool
    ing and format
- we will have dropout layers
- how our image data will be represented?

#### image data
- starts with a matrix of pixel values 0 to 255 of three color channels 
    with a fixed size
- each pixel is a feature and should be analyzed to accurately classify 
    the image
    - for humans classification is very simple at glancing
    - model must analyze the whole thing
    - each pixel is considered a feature, 32x32 image has 1024 features
        - not every pixel is important
- 1024 neurons in first layer
    - even more in layer b
    - 1024 neurons times 1024 connections, no computer can handle this
    - convolve and maxpooling to reduce image size
- dont care about most of the image
    - only the pixels that involve the dog
    - dont care about finer details like hair
    - dont care of non dog pixels
    - hilight features that are important

#### convolutions
- like a double integral, really cool
- takes a matrix of pixel values, and applies a kernel to each block 
    - kernel also can be called a filter
- apply kernel block to each part of the image until the entire image is
    is covered
- matches in image data and kernel get applied to produce a smaller image size
    - hilighted a smaller set of features
    - convolutions occur in filters too like convolutions
    - max pooling also occur outside of ML
- reduces noise
    - dont care about the fine details
    - dont care about the background image

#### max pooling
- creates borders and finds the max value 
- greatly reduces the size of matrix to accentuate important features
- can convolve and max pool many times
- good idea to change parameters and max pooling

#### review
- convolve => max pool => formatting => dense => dropout

## Day 4: Explore the Keras API

### 00. Intro to Day 4
- goals: coding, coding, and lessons
- writing code
- lecture in activation 
    - commonly used functions
    - advantages of function over the other    

### 01. Intro to TensorFlow and Keras

#### What is TensorFlow?

- high level library for mathematical computational, focused on ML
- build and predict pretrained model
- very time consuming to build ML engine from scratch
- TensorFlow is built in C++
- very flexible, not as easy as keras, especially with conv models
    - complex model lets more custom
    - manually build

#### What is Keras?

- keras is built ontop of tensorflow
- easier to use
    - more user friendly
    - simpler syntax
    - create a layer object and add it to keras model
    - tensor flow needs to specify
        - one line of code vs 5 lines
    - built in functions to train, test, and predict
    - easily integrate GPU

### 02. Understanding Keras Syntax
#### Before you run, set up your env:
Install keras package and its dependecies.
I use pip so this works for me: `python -m pip install keras`
keras depends on only one other package: tensorflow

The following code snippet shows some of the syntax of Keras and is
not completely functional:

```python
import keras

from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

## Day 3 Explore the Keras API
## 02. Understanding Keras Syntax

model = Sequential()

## Conv2D(
##   filters
##   kernel_size : size of kernel, what determines the output features
##   strides     : how we traverse the image matrix (like right one down one)
##   activation_function : neuron fires strongly or nah?
##   ...
##   )

conv_layer = Conv2D(filter=32, kernel_size=(3,3), activation='relu'))

max_pool_layer = MaxPooling2D(pool_size=(2,2))

dense_layer = Dense(1024, activation='softmax')

## drop half of the neurons during training with rate 0.5)
##   prevents from focusing on details that don't matter
##   dropping random also

dropout_layer = Dropout(rate=0.5)

model.add(conv_layer)
model.add(max_pool_layer)
model.add(dense_layer)
model.add(dropout_layer)

## in tensorflow this step is stupid complex
model.compile(optimizer=SGD, loss=0.01, metrics=['accuracy']) 

## need data to use this function
model.fit()
model.evaluate()
model.predict()
```

### 03. Intro to Activation Functions

#### Common Activation Functions
- sum all inputs, apply a function, then produce output

##### Identity: output = input
- just outputs what it inputs
- fine for simple models, fails in dense networks

##### binary step: output = 1 if input >=0 else output = 0
- not very flexible
- no in between numbers
- causes dead neurons which are neurons don't fire

##### logistic/sigmoid: `output -> 0 as input < 0 or output -> 1 as input > 0
- similar to binary, but smoothed out

##### TanH: `output -> -1 as input < 0 or output -> 1 as input > 0`
- similar shape to sigmoid
- not a bad function
- lots of models use this

##### Relu: `output = 0 if input < 0 or output = input if input >= 0`
- combo binary and identity
- eliminate all negative values, keeping magnitude of positive
- problem don't get to keep negative values
- only interested in positive or null outputs
- can produce dead neurons

##### Leaky Relu: `output -> input if input < 0 or output = input if input >= 0`
- best models use combination of Relu and leaky

##### SoftMax:: `output = set of probabilites based on number of output connections`
- usually used as last layer to guarantee possible output to all possible outputs
- 5 possible outputs: a, b, c, d, or e
| output        | a     | b     | c     | d     | e     |
| possibilty    | 0.1   | 0.2   | 0.001 | 0.5   | 0.01  |
- this table is what a soft max output kind of looks like

##### Which is best?
- it depends on the implementation
- inner layres typically Relu / Leaky Relu
- last layer SoftMax

## Day 5: Format Datasets and Examine CIFAR-10
### 00. Intro to Day 5
Focus: learning to format data
Coding day

### 01. Exploring CIFAR10 Dataset
### 02. Understanding Specific Data
### 03. Formatting Input Images

## Day 6: Build the Image Classifier Model
### 00. Intro to Day 6
### 01. Building the Model
### 02. Compiling and Training the Model
### 03. Gradient Descent and Optimizers

## Day 7: Save and Load Trained Models
### 00. Intro to Day 7
### 01. Saving and Loading Model to H5
### 02. Saving Model to Protobuf File
### 03. BootCamp Summary
