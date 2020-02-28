The following are notes I've taken from a machine learning masterclass on
stackskills.com. Days 1 and 2 are basics of Python.

# Day 3: Understand Machine Learning Neural Networks
## 01. Intro to Machine learning
- basic definition: machines ability to learn from previous experience
- programs should get better with increased exposure to relevant data
- examples
    -- opt, prediction, classifications
    -- stock market prediction or image recognition
        --- stock market hard
        --- image recog easy and can use simple machines
- many different algorithms
    -- we will use convolutional NN trained with supervised learning

### 4 steps
    1. processing 
        - more relevant == more accurate
        - gather a lot of data is time consuming
            -- a lot of preformatted databases online
            -- data collection can be the most frustrating
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

## 02. Understanding Keras Syntax
### Before you run, set up your env:
Install keras package and its dependecies.
I use pip so this works for me: `python -m pip install keras`
keras depends on only one other package: tensorflow

### What is TensorFlow?
- TensorFlow is more complex than Keras

## 03. Intro to Activation Functions

# Day 4: Explore the Keras API

# Day 5: Format Datasets and Examine CIFAR-10

# Day 6: Build the Image Classifier Model

# Day 7: Save and Load Trained Models

