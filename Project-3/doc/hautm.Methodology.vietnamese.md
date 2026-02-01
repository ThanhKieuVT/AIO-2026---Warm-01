# Methodology: Kiến trúc CNN và Giải pháp cho bài toán Phân loại Ảnh

Trong phần này, chúng ta sẽ đi sâu vào phương pháp giải quyết bài toán phân loại chó mèo (**Cats vs. Dogs Classification**). Thay vì sử dụng các thuật toán Machine Learning truyền thống (như SVM hay KNN) vốn gặp hạn chế lớn khi xử lý dữ liệu phi cấu trúc, dự án này áp dụng **Mạng Nơ-ron Tích chập (Convolutional Neural Networks - CNN)** – xương sống của thị giác máy tính hiện đại.

## 1. Định nghĩa Bài toán (Problem Formulation)

Bài toán được định nghĩa là **Binary Classification** (Phân loại nhị phân).
Cho tập dữ liệu $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}$, trong đó:

* $x_i \in \mathbb{R}^{H \times W \times C}$: Là hình ảnh đầu vào (trong dự án này, chúng ta resize về $128 \times 128 \times 3$).
* $y_i \in \{0, 1\}$: Là nhãn (label) tương ứng (0: Mèo, 1: Chó).



<figure style="text-align: center;">
  <img src="/static/uploads/image/dogcat.png" 
       alt="dogcat" 
       width="999">
  <figcaption>
    <em>Hình 1.1 Cats vs. Dogs Classification </em>
  </figcaption>
</figure>
Mục tiêu là huấn luyện một hàm ánh xạ $f(x; \theta)$ (mô hình CNN với tham số $\theta$) sao cho dự đoán $\hat{y} = f(x)$ giảm thiểu hàm mất mát (**Loss Function**) trên tập dữ liệu.

## 2. Tại sao lại chọn CNN?

Mạng nơ-ron truyền thống (**Fully Connected Networks - MLP**) gặp hai vấn đề lớn khi xử lý ảnh:

1.  **Bùng nổ tham số:** Một ảnh màu $128 \times 128$ có $128 \times 128 \times 3 = 49,152$ điểm ảnh. Nếu dùng MLP, số lượng trọng số sẽ quá lớn, dẫn đến *Overfitting*.
2.  **Mất thông tin không gian:** Việc duỗi phẳng (flatten) ảnh thành vector 1 chiều làm mất đi mối quan hệ không gian giữa các pixel lân cận (ví dụ: mắt phải nằm gần mũi).



**CNN giải quyết vấn đề này nhờ 3 cơ chế:**

* **Local Connectivity:** Các nơ-ron chỉ kết nối với một vùng nhỏ của ảnh (Receptive Field).
* **Parameter Sharing:** Dùng chung một bộ lọc (filter) quét qua toàn bộ ảnh, giúp giảm đáng kể số lượng tham số.
* **Translation Invariance:** Khả năng nhận diện đối tượng dù nó nằm ở vị trí nào trong ảnh [1].

## 3. Cấu trúc chi tiết của Mô hình (Model Architecture)

Mô hình được thiết kế theo kiến trúc **Sequential**, bao gồm hai phần chính: **Feature Extractor** (Trích xuất đặc trưng) và **Classifier** (Bộ phân loại).

### 3.1. Feature Extractor (Khối Tích chập)

Khối này có nhiệm vụ chuyển đổi ảnh gốc (pixel thô) thành các đặc trưng trừu tượng (cạnh, góc, hình dạng).

#### a. Convolutional Layer (Lớp tích chập)
Đây là lớp cốt lõi. Một bộ lọc (kernel) $K$ kích thước $k \times k$ trượt qua ảnh đầu vào $I$. Giá trị tại vị trí $(i, j)$ của Feature Map đầu ra được tính bằng phép tích chập:

$$
(I * K)_{ij} = \sum_{m=0}^{k-1} \sum_{n=0}^{k-1} I(i+m, j+n) \cdot K(m, n) + b
$$



* **Trong dự án:** Sử dụng các kernel $3 \times 3$, số lượng filter tăng dần (ví dụ: 32 $\rightarrow$ 64 $\rightarrow$ 128) để học các đặc trưng từ đơn giản đến phức tạp.

#### b. Activation Function (Hàm kích hoạt)
Sau mỗi lớp tích chập, ta áp dụng hàm phi tuyến **ReLU (Rectified Linear Unit)** để giúp mô hình học được các mối quan hệ phức tạp:

$$
f(x) = \max(0, x)
$$

ReLU giúp giải quyết vấn đề *Vanishing Gradient* (triệt tiêu đạo hàm) tốt hơn Sigmoid hay Tanh trong các mạng sâu [2].

#### c. Pooling Layer (Lớp gộp)
Sử dụng **MaxPooling** ($2 \times 2$) để giảm kích thước không gian của Feature Map đi một nửa.



* **Mục đích:** Giảm chi phí tính toán và giúp mô hình bất biến với các dịch chuyển nhỏ của vật thể.

### 3.2. Classifier (Khối Phân loại)

Sau khi trích xuất đặc trưng, dữ liệu được đưa vào mạng Fully Connected để ra quyết định.

1.  **Flatten:** Duỗi tensor 3D (ví dụ $16 \times 16 \times 128$) thành vector 1D.
2.  **Dense Layers:** Các lớp ẩn kết nối đầy đủ.
3.  **Dropout:** Một kỹ thuật Regularization, ngẫu nhiên "tắt" một số nơ-ron (ví dụ 50%) trong quá trình train để ngăn chặn Overfitting [3].

### 3.3. Output Layer (Đầu ra)

Dựa trên đoạn code Inference, mô hình hỗ trợ hai dạng đầu ra, nhưng tối ưu nhất cho bài toán nhị phân là sử dụng **Sigmoid**:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* Giá trị đầu ra $\hat{y} \in [0, 1]$ biểu thị xác suất ảnh là "Chó".
* Nếu $\hat{y} < 0.5 \rightarrow$ Mèo, $\hat{y} \ge 0.5 \rightarrow$ Chó.

> **Lưu ý:** Trong code deployment, chúng ta sử dụng thêm một ngưỡng tin cậy (`CONFIDENCE_THRESHOLD = 0.7`). Nếu xác suất nằm trong khoảng $(0.3, 0.7)$, hệ thống sẽ trả về **"Unknown"**. Đây là cơ chế an toàn để tránh việc mô hình "đoán mò" khi gặp dữ liệu nhiễu.

## 4. Hàm Mất mát và Tối ưu hóa (Loss & Optimizer)

* **Loss Function:** Sử dụng **Binary Cross-Entropy**:
    $$
    L = -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]
    $$
    Hàm này phạt nặng các dự đoán sai lệch lớn so với nhãn thực tế.

* **Optimizer:** Sử dụng **Adam** (Adaptive Moment Estimation). Đây là thuật toán tối ưu phổ biến nhất hiện nay nhờ khả năng tự điều chỉnh learning rate cho từng tham số, giúp hội tụ nhanh hơn SGD truyền thống [4].

## 5. Tổng kết Kiến trúc (Summary)

Dưới đây là bảng tóm tắt kiến trúc mô hình đề xuất cho dự án (tương thích với input size 128 trong code):

| Layer (Type) | Output Shape | Param # | Chức năng |
| :--- | :--- | :--- | :--- |
| **Input** | (128, 128, 3) | 0 | Nhận ảnh RGB |
| **Conv2D + ReLU** | (126, 126, 32) | ~896 | Trích xuất đặc trưng cấp thấp |
| **MaxPooling2D** | (63, 63, 32) | 0 | Giảm chiều dữ liệu |
| **Conv2D + ReLU** | (61, 61, 64) | ~18K | Trích xuất đặc trưng trung cấp |
| **MaxPooling2D** | (30, 30, 64) | 0 | Giảm chiều dữ liệu |
| **Conv2D + ReLU** | (28, 28, 128) | ~73K | Trích xuất đặc trưng cao cấp |
| **MaxPooling2D** | (14, 14, 128) | 0 | Giảm chiều dữ liệu |
| **Flatten** | (25088) | 0 | Chuyển đổi sang vector |
| **Dense + ReLU** | (512) | ~12.8M | Học quan hệ phi tuyến |
| **Dropout (0.5)** | (512) | 0 | Chống Overfitting |
| **Dense (Output)** | (1) | 513 | Dự đoán xác suất (Sigmoid) |

---

### 📚 Tài liệu tham khảo (References)
1. LeCun, Y., et al. (1998). "Gradient-based learning applied to document recognition." *Proceedings of the IEEE*.
2. Nair, V., & Hinton, G. E. (2010). "Rectified linear units improve restricted boltzmann machines." *ICML*.
3. Srivastava, N., et al. (2014). "Dropout: A simple way to prevent neural networks from overfitting." *JMLR*.
4. Kingma, D. P., & Ba, J. (2014). "Adam: A Method for Stochastic Optimization." *ICLR*.
