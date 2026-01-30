# Dog and Cat images classified using Convolutional Neural Networks 
## 1. Introduction

In recent years, Computer Vision (CV) has become one of the most rapidly developing fields of Artificial Intelligence. CV enables computers to see and understand the content of images and videos, thereby unlocking many important real-world applications such as face recognition, autonomous vehicles, security surveillance, healthcare, and e-commerce.

One of the fundamental and important problems in Computer Vision is **Image Classification** — the task of assigning a label to each input image. In this problem, the system must learn how to extract meaningful features from images in order to make accurate predictions about the class to which an image belongs.

In this project, we focus on the **Dog vs. Cat Classification** problem — a classic task often used as an introductory example for deep learning models in image processing. Although the problem structure is relatively simple, real-world image data still contains many complex variations, requiring the model to learn spatial features at multiple levels.

To address this problem, we employ **Convolutional Neural Networks (CNNs)** — a neural network architecture specifically designed for image data. CNNs are capable of automatically learning spatial features such as edges, corners, textures, and object structures, enabling high performance in computer vision tasks.

The goal of this project is to build a CNN model that can accurately classify input images into two classes: `dog` or `cat`, while also helping learners better understand the end-to-end process of building a complete image classification system.

## 2. Motivation

Although humans can easily distinguish between dogs and cats within seconds, this task is far from trivial for computers. Real-world images can vary significantly in terms of:

- Camera angles  
- Lighting conditions  
- Image size and resolution  
- Object poses  
- Background context  

These factors make rule-based image classification approaches impractical. As a result, machine learning models — especially deep learning — have become the optimal choice for image processing tasks.

The dog vs. cat classification problem is commonly used as a **benchmark** in the field of CV for several reasons:

- The problem structure is simple and intuitive  
- The dataset is rich and easily accessible  
- It is challenging enough to demonstrate the power of CNNs  
- It is well-suited for beginners in Deep Learning  

**Convolutional Neural Networks (CNNs)** have demonstrated superior performance in image classification tasks due to their ability to:

- Automatically learn features from raw data  
- Reduce the number of parameters compared to fully connected networks  
- Preserve spatial information within images  

Through this project, we aim to:

- Gain a deeper understanding of how CNNs work in image classification tasks  
- Practice the complete deep learning workflow, from data preparation to training and evaluation  
- Build a foundation for tackling more complex Computer Vision problems in the future  

## 3. Problem Formulation

### 3.1 Input

The input to the model is an RGB color image represented as a tensor:

$$
x \in \mathbb{R}^{H \times W \times 3}
$$

where:

- $H$ denotes the image height  
- $W$ denotes the image width  
- 3 corresponds to the three RGB color channels  

Before being fed into the model, images are preprocessed (e.g., resizing, normalization, etc.) to ensure consistent size and appropriate formatting.

### 3.2 Output

The output of the model is a label:

$$
y \in \{0, 1\}
$$

where:

- 0 = cat  
- 1 = dog

### 3.3 Learning Model

The objective of the task is to learn a mapping function:

$$
f: x \rightarrow y
$$

such that for an input image not seen during training, the model can still correctly predict the corresponding label.

To achieve this, we use a **Convolutional Neural Network (CNN)** consisting of convolutional layers, pooling layers, and fully connected layers to extract and aggregate important features from images.

### 3.4 Loss Function

The model employs the **Categorical Crossentropy** loss function in combination with an output layer containing two nodes with a Softmax activation. This approach allows the model to estimate separate probabilities for each class and provides a foundation for extending the task to multi-class classification problems in the future.
