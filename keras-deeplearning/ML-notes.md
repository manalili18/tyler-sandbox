The following are notes I've taken from a machine learning masterclass on
stackskills.com. Days 1 and 2 are basics of Python.

# Day 3: Understand Machine Learning Neural Networks
## 01. Intro to Machine learning
- basic definition: machines ability to learn from previous experience
- programs should get better with increased exposure to relevant data
- examples
    - opt, prediction, classifications
    - stock market prediction or image recognition
        - stock market hard
        - image recog easy and can use simple machines
- many different algorithms
    - we will use convolutional NN trained with supervised learning

### 4 steps
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

### Extra learning
- checkout other ML algos

## 02. Intro to Neural Networks

### What is a nerual net?
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

## 03. Intro to Convolutions

### what are convolutional neural net
- neural net interconnected nodes in dense layer 
- before we feed into this dense layer series of convolutions and max pool
    ing and format
- we will have dropout layers
- how our image data will be represented?

### image data
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

### convolutions
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

### max pooling
- creates borders and finds the max value 
- greatly reduces the size of matrix to accentuate important features
- can convolve and max pool many times
- good idea to change parameters and max pooling

### review
- convolve => max pool => formatting => dense => dropout

# Day 4: Explore the Keras API

## 00. Intro to Day 4
- goals: coding, coding, and lessons
- writing code
- lecture in activation 
    - commonly used functions
    - advantages of function over the other    

## 01. Intro to TensorFlow and Keras

### What is TensorFlow?

- high level library for mathematical computational, focused on ML
- build and predict pretrained model
- very time consuming to build ML engine from scratch
- TensorFlow is built in C++
- very flexible, not as easy as keras, especially with conv models
    - complex model lets more custom
    - manually build

### What is Keras?

- keras is built ontop of tensorflow



## 02. Understanding Keras Syntax
### Before you run, set up your env:
Install keras package and its dependecies.
I use pip so this works for me: `python -m pip install keras`
keras depends on only one other package: tensorflow

## 03. Intro to Activation Functions

### What is TensorFlow?
- TensorFlow is more complex than Keras

# Day 5: Format Datasets and Examine CIFAR-10

# Day 6: Build the Image Classifier Model

# Day 7: Save and Load Trained Models

