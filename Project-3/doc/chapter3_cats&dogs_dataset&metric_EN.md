## 3.1. Dataset & Exploratory Data Analysis (EDA)

When working on an image classification project, if you don’t understand the data, it’s very difficult to train an effective model. EDA is the step that helps you review the dataset before feeding it to the model.

For this project, our dataset was taken from Kaggle and contains **25,000 images** of dogs and cats. A convenient point of this dataset is that the label is embedded directly in the file name. For example, files typically look like `cat.1234.jpg` or `dog.5678.jpg`. This makes labeling fast, but you must be careful not to let your pipeline accidentally use the file name as a “feature” for classification.

The goal is to train the model on the training set and predict labels for the test set, which contains **12,500 images** whose file names are just numbers (no labels in the name). The task is to predict the **probability of being a dog** for each image, with the convention **1 = dog**, **0 = cat**.

---

### 3.1.1. Checking label distribution

Before training, we check whether the dataset is class-imbalanced. This dataset is fairly balanced (close to 50/50), so it doesn’t require complicated rebalancing techniques. Our team further split the dataset into 3 smaller subsets:

- **Training set**: 20,000 images, used for the model to learn
- **Validation set**: 2,500 images, used to evaluate quality on unseen data during training
- **Testing set**: 2,500 images, this is an internal test used for a final check before running the model on Kaggle’s 12,500-image test set

![dataset](dataset.png)

---

### 3.1.2. Inspecting images

For image inspection, we first need to check the size, format, and diversity of the data. Our dataset includes images from many different sources on the internet and is quite diverse: some are taken with phones, some are more professional, some are close-ups, some are zoomed out, some have indoor backgrounds, and some have outdoor backgrounds. In addition, a few difficult images may include humans, or more than one cat or dog.

Images in this dataset are typically **.jpg**, in color (RGB), and have **non-uniform** sizes. Since a CNN requires inputs of the same size, you must **resize** them to a fixed shape. In this project, we resized images to **128×128** to balance speed and accuracy.

![sample_dog](sample_dog.png)

![sample_cat](sample_cat.png)

Most images fall into a few common size clusters, but there are some outliers: very small images, extremely large images, very wide images, or very tall images. If you don’t crop/pad properly, images can become distorted, which can make the model’s job harder. We also need to check for corrupted files, files that load but have incorrect color channels, or images that are so small that resizing causes heavy pixelation. Overall, this dataset is large enough for the model to learn real visual features.

---

## 3.2. Metric & Evaluation Strategy

After understanding the dataset, we need to decide how to measure model quality. It may sound simple—just classify cat vs dog—so the natural metric is **accuracy**. However, if you only look at a single accuracy number, it’s very easy to misjudge the model’s true quality, because in practice it might only learn a few easy patterns or be overfitting.

### 3.2.1. Accuracy

As mentioned, accuracy alone is not sufficient to fully evaluate a model, but it is still a core and important metric. It answers this question:

> “Out of all images, how many did the model predict correctly?”

The formula is straightforward: accuracy equals the **number of correct predictions** divided by the **total number of predictions**:

$$
Accuracy = \frac{\text{Number of correct predictions}}{\text{Total number of predictions}}
$$

Another reason accuracy makes sense here is that the number of cats and dogs is relatively balanced in this dataset. If the data were heavily imbalanced (for example 95% dogs, 5% cats), accuracy could be misleading and make it hard to tell whether the model is actually good. Therefore, accuracy is a reasonable metric to use as an “overall score” when reporting results.

However, accuracy has a limitation: it tells you how often the model is right, but not **how** it is wrong or **where** it is wrong. That’s why our EDA and report also include an important tool: the **Confusion Matrix**.

---

### 3.2.2 Confusion Matrix

A confusion matrix helps you see where and how the model makes mistakes. Specifically:
- How many **cat** images are incorrectly predicted as **dog**
- How many **dog** images are incorrectly predicted as **cat**

In binary classification, the confusion matrix has 4 cells:
- **True Positive (TP)**: dog → predicted dog
- **True Negative (TN)**: cat → predicted cat
- **False Positive (FP)**: cat → predicted dog
- **False Negative (FN)**: dog → predicted cat

Suppose you have 100 validation images:
- 50 cats, 50 dogs  
  The model predicts 92 correctly → accuracy = 92%

But the confusion matrix may show:
- The model misclassifies 6 cat images as dogs (FP=6)
- The model misclassifies 2 dog images as cats (FN=2)

![example_matrix](example_matrix.png)

From this, we can immediately see the model may be biased toward predicting dogs more correctly (or it struggles with cat images whose backgrounds look similar to dog images). This is information that accuracy alone cannot reveal. Another reason the confusion matrix is important is that when you improve the model, you don’t only want “higher accuracy”—you also want to reduce the specific type of errors you care about.

---

### 3.2.3. Classification report

In this problem, mistaking a cat for a dog or a dog for a cat is usually equally bad, so accuracy is enough to get started. But to be more complete, we also consider **Precision** and **Recall**, which help us interpret the confusion matrix more deeply. In simple terms:

- **Precision (assume for class dog)**:  
  Among all images the model predicts as “dog”, how many are truly dogs?  
  High precision means the model rarely “assigns dog” incorrectly.

- **Recall (assume for class dog)**:  
  Among all true dog images, how many did the model find?  
  High recall means the model rarely “misses dogs”.

- **F1-score**: the harmonic mean of precision and recall

$$
F1 = \frac{2*Precision*Recall}{Precision + Recall}
$$

	F1 is only high when both precision and recall are high, used when you want the model to **not make many mistakes** and also **not miss many things**.

With a balanced Cats vs Dogs dataset, Precision/Recall are often used to compare different model versions when **accuracy is similar**, and to understand which direction the model’s errors lean.

---

### 3.2.4. Validation

A common mistake, as mentioned, is to train a model and then conclude it is good just because training accuracy is high. But as discussed, accuracy alone is not enough to judge whether the model is truly good. The model may completely “memorize” the training images and fail to generalize—this is called **overfitting**.

A simple way to understand **overfit (overfitting)** is: the model learns the training data too thoroughly, to the point that it remembers specific details of the training set, including noise. In that case, training accuracy can be very high (or training loss very low), but when you evaluate on other datasets different from the training data, accuracy drops—sometimes a lot. That’s why we split the dataset into two additional subsets: a validation set and an internal testing set.

Common split ratios are 80/10/10 (or 80/20 if you only need two sets) or 70/15/15 (70/30). The most important point is to keep the cat/dog distribution balanced across train/validation/test, and to ensure that validation/testing data are truly independent from training data.

> Validation is like a midterm exam. The model learns from the training data, but the score must be based on validation data to see whether it truly understands or just memorized.

#### Signs of overfitting

In this Cats vs Dogs classification project, overfitting often happens because the dataset is highly diverse, which can cause the model to learn the surrounding scene/context instead of the animal itself. Training for too long can also make the model memorize specific details, reducing its ability to generalize.

The easiest signs to observe during training:

- Training loss steadily decreases
- Validation loss starts to increase
- Validation accuracy stagnates or decreases

When that happens, the model is overfitting. This is why we need a validation set, to monitor loss/accuracy curves, and to apply anti-overfitting techniques such as augmentation, dropout, early stopping, …
