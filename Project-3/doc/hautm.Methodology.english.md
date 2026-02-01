# Methodology: CNN Architecture and Solution for Image Classification

In this section, we delve into the methodology employed to solve the **Cats vs. Dogs Classification** problem. Instead of relying on traditional Machine Learning algorithms (such as SVM or KNN), which struggle with unstructured data like images, this project utilizes **Convolutional Neural Networks (CNN)** – the backbone of modern computer vision.

## 1. Problem Formulation

The problem is defined as a **Binary Classification** task.
Given a dataset $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}$, where:

* $x_i \in \mathbb{R}^{H \times W \times C}$: The input image (in this project, images are resized to $128 \times 128 \times 3$).
* $y_i \in \{0, 1\}$: The corresponding label (0: Cat, 1: Dog).

The objective is to train a mapping function $f(x; \theta)$ (a CNN model with parameters $\theta$) such that the prediction $\hat{y} = f(x)$ minimizes the **Loss Function** over the dataset.

## 2. Why Choose CNN?

Traditional Fully Connected Networks (MLP) face two major limitations when processing images:

1.  **Parameter Explosion:** A color image of size $128 \times 128$ contains $128 \times 128 \times 3 = 49,152$ pixels. If a standard MLP is used, the number of weights becomes unmanageably large, leading to severe *Overfitting*.
2.  **Loss of Spatial Information:** Flattening the image into a 1D vector destroys the spatial relationships between neighboring pixels (e.g., the right eye is always near the nose).



**CNNs solve these issues through three key mechanisms:**

* **Local Connectivity:** Neurons are connected only to a small region of the input image (Receptive Field).
* **Parameter Sharing:** The same filter (kernel) is swept across the entire image, significantly reducing the number of parameters.
* **Translation Invariance:** The ability to recognize an object regardless of its position within the image [1].

## 3. Detailed Model Architecture

The model follows a **Sequential** architecture, consisting of two main components: the **Feature Extractor** and the **Classifier**.

### 3.1. Feature Extractor (Convolutional Blocks)

This component is responsible for transforming the raw input (pixels) into abstract features (edges, textures, shapes).

#### a. Convolutional Layer
This is the core building block. A filter (kernel) $K$ of size $k \times k$ slides over the input image $I$. The value at position $(i, j)$ of the output Feature Map is calculated via the convolution operation:

$$
(I * K)_{ij} = \sum_{m=0}^{k-1} \sum_{n=0}^{k-1} I(i+m, j+n) \cdot K(m, n) + b
$$



* **Project Implementation:** We use $3 \times 3$ kernels with an increasing number of filters (e.g., 32 $\rightarrow$ 64 $\rightarrow$ 128) to learn features ranging from simple to complex.

#### b. Activation Function
After each convolutional layer, a non-linear activation function, **ReLU (Rectified Linear Unit)**, is applied to help the model learn complex patterns:

$$
f(x) = \max(0, x)
$$

ReLU addresses the *Vanishing Gradient* problem more effectively than Sigmoid or Tanh in deep networks [2].

#### c. Pooling Layer
We use **MaxPooling** ($2 \times 2$) to reduce the spatial dimensions of the Feature Map by half.



* **Purpose:** Reduces computational cost and makes the model invariant to small translations/shifts of the object.

### 3.2. Classifier (Fully Connected Block)

Once features are extracted, the data is passed to a Fully Connected network for decision-making.

1.  **Flatten:** Unrolls the 3D tensor (e.g., $16 \times 16 \times 128$) into a 1D vector.
2.  **Dense Layers:** Fully connected hidden layers.
3.  **Dropout:** A regularization technique that randomly "drops" a percentage of neurons (e.g., 50%) during training to prevent Overfitting [3].

### 3.3. Output Layer

Based on the inference logic, the model supports binary output using the **Sigmoid** activation function:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* The output value $\hat{y} \in [0, 1]$ represents the probability that the image is a "Dog".
* If $\hat{y} < 0.5 \rightarrow$ Cat, $\hat{y} \ge 0.5 \rightarrow$ Dog.

> **Note:** In the deployment code, we implement a **confidence threshold** (`CONFIDENCE_THRESHOLD = 0.7`). If the predicted probability falls within the ambiguous range of $(0.3, 0.7)$, the system returns **"Unknown"**. This safety mechanism prevents the model from making uncertain guesses on noisy data.

## 4. Loss Function & Optimizer

* **Loss Function:** We use **Binary Cross-Entropy**:
    $$
    L = -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]
    $$
    This function heavily penalizes predictions that are confident but wrong.

* **Optimizer:** We employ **Adam** (Adaptive Moment Estimation). It is currently one of the most popular optimization algorithms due to its ability to adapt learning rates for individual parameters, leading to faster convergence compared to traditional SGD [4].

## 5. Architecture Summary

Below is a summary of the proposed model architecture (compatible with the input size of 128 used in the code):

| Layer (Type) | Output Shape | Param # | Function |
| :--- | :--- | :--- | :--- |
| **Input** | (128, 128, 3) | 0 | RGB Image Input |
| **Conv2D + ReLU** | (126, 126, 32) | ~896 | Low-level feature extraction |
| **MaxPooling2D** | (63, 63, 32) | 0 | Dimensionality reduction |
| **Conv2D + ReLU** | (61, 61, 64) | ~18K | Mid-level feature extraction |
| **MaxPooling2D** | (30, 30, 64) | 0 | Dimensionality reduction |
| **Conv2D + ReLU** | (28, 28, 128) | ~73K | High-level feature extraction |
| **MaxPooling2D** | (14, 14, 128) | 0 | Dimensionality reduction |
| **Flatten** | (25088) | 0 | Vectorization |
| **Dense + ReLU** | (512) | ~12.8M | Non-linear relationship learning |
| **Dropout (0.5)** | (512) | 0 | Regularization (Anti-Overfitting) |
| **Dense (Output)** | (1) | 513 | Probability Prediction (Sigmoid) |

---

### 📚 References
1. LeCun, Y., et al. (1998). "Gradient-based learning applied to document recognition." *Proceedings of the IEEE*.
2. Nair, V., & Hinton, G. E. (2010). "Rectified linear units improve restricted boltzmann machines." *ICML*.
3. Srivastava, N., et al. (2014). "Dropout: A simple way to prevent neural networks from overfitting." *JMLR*.
4. Kingma, D. P., & Ba, J. (2014). "Adam: A Method for Stochastic Optimization." *ICLR*.
