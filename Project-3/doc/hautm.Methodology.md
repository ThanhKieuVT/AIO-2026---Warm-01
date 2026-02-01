\documentclass[a4paper,12pt]{article}

% --- Cấu hình Tiếng Việt và Font chữ ---
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc} % Bắt buộc để hiển thị tiếng Việt đúng
\usepackage[vietnamese]{babel}
\usepackage{mathptmx} % Font giống Times New Roman

% --- Các gói hỗ trợ Toán học và Hình ảnh ---
\usepackage{amsmath, amssymb, amsfonts}
\usepackage{graphicx}
\usepackage{float}
\usepackage{booktabs} % Để tạo bảng đẹp hơn
\usepackage{hyperref} % Tạo liên kết
\usepackage{geometry} % Căn lề
\usepackage{xcolor}

% --- Cấu hình lề trang ---
\geometry{left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm}

% --- Thông tin bài viết ---
\title{\textbf{Methodology: Kiến trúc CNN và Giải pháp cho bài toán Phân loại Ảnh}}
\author{\textit{Dự án Phân loại Chó Mèo}}
\date{\today}

\begin{document}

\maketitle

\section*{Giới thiệu}
Trong phần này, chúng ta sẽ đi sâu vào phương pháp giải quyết bài toán phân loại chó mèo (\textit{Cats vs. Dogs Classification}). Thay vì sử dụng các thuật toán Machine Learning truyền thống (như SVM hay KNN) vốn gặp hạn chế lớn khi xử lý dữ liệu phi cấu trúc, dự án này áp dụng \textbf{Mạng Nơ-ron Tích chập (Convolutional Neural Networks - CNN)} – xương sống của thị giác máy tính hiện đại.

\section{Định nghĩa Bài toán (Problem Formulation)}

Bài toán được định nghĩa là \textbf{Binary Classification} (Phân loại nhị phân). \\
Cho tập dữ liệu $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}$, trong đó:
\begin{itemize}
    \item $x_i \in \mathbb{R}^{H \times W \times C}$: Là hình ảnh đầu vào (trong dự án này, chúng ta resize về kích thước $128 \times 128 \times 3$).
    \item $y_i \in \{0, 1\}$: Là nhãn (label) tương ứng ($0$: Mèo, $1$: Chó).
\end{itemize}

Mục tiêu là huấn luyện một hàm ánh xạ $f(x; \theta)$ (mô hình CNN với tham số $\theta$) sao cho dự đoán $\hat{y} = f(x)$ giảm thiểu hàm mất mát (Loss Function) trên tập dữ liệu.

\section{Tại sao lại chọn CNN?}

Mạng nơ-ron truyền thống (Fully Connected Networks - MLP) gặp hai vấn đề lớn khi xử lý ảnh:
\begin{enumerate}
    \item \textbf{Bùng nổ tham số:} Một ảnh màu $128 \times 128$ có $128 \times 128 \times 3 = 49,152$ điểm ảnh. Nếu dùng MLP, số lượng trọng số sẽ quá lớn, dẫn đến \textit{Overfitting}.
    \item \textbf{Mất thông tin không gian:} Việc duỗi phẳng (flatten) ảnh thành vector 1 chiều làm mất đi mối quan hệ không gian giữa các pixel lân cận (ví dụ: mắt phải nằm gần mũi).
\end{enumerate}

\textbf{CNN giải quyết vấn đề này nhờ 3 cơ chế:}
\begin{itemize}
    \item \textbf{Local Connectivity:} Các nơ-ron chỉ kết nối với một vùng nhỏ của ảnh (Receptive Field).
    \item \textbf{Parameter Sharing:} Dùng chung một bộ lọc (filter) quét qua toàn bộ ảnh, giúp giảm đáng kể số lượng tham số.
    \item \textbf{Translation Invariance:} Khả năng nhận diện đối tượng dù nó nằm ở vị trí nào trong ảnh [1].
\end{itemize}

\section{Cấu trúc chi tiết của Mô hình (Model Architecture)}

Mô hình được thiết kế theo kiến trúc \textbf{Sequential}, bao gồm hai phần chính: \textbf{Feature Extractor} (Trích xuất đặc trưng) và \textbf{Classifier} (Bộ phân loại).

\subsection{Feature Extractor (Khối Tích chập)}
Khối này có nhiệm vụ chuyển đổi ảnh gốc (pixel thô) thành các đặc trưng trừu tượng (cạnh, góc, hình dạng).

\subsubsection*{a. Convolutional Layer (Lớp tích chập)}
Đây là lớp cốt lõi. Một bộ lọc (kernel) $K$ kích thước $k \times k$ trượt qua ảnh đầu vào $I$. Giá trị tại vị trí $(i, j)$ của Feature Map đầu ra được tính bằng phép tích chập:

\begin{equation}
    (I * K)_{ij} = \sum_{m=0}^{k-1} \sum_{n=0}^{k-1} I(i+m, j+n) \cdot K(m, n) + b
\end{equation}

\textbf{Trong dự án:} Sử dụng các kernel $3 \times 3$, số lượng filter tăng dần (ví dụ: $32 \rightarrow 64 \rightarrow 128$) để học các đặc trưng từ đơn giản đến phức tạp.

\subsubsection*{b. Activation Function (Hàm kích hoạt)}
Sau mỗi lớp tích chập, ta áp dụng hàm phi tuyến \textbf{ReLU (Rectified Linear Unit)} để giúp mô hình học được các mối quan hệ phức tạp:

\begin{equation}
    f(x) = \max(0, x)
\end{equation}

ReLU giúp giải quyết vấn đề \textit{Vanishing Gradient} (triệt tiêu đạo hàm) tốt hơn Sigmoid hay Tanh trong các mạng sâu [2].

\subsubsection*{c. Pooling Layer (Lớp gộp)}
Sử dụng \textbf{MaxPooling} ($2 \times 2$) để giảm kích thước không gian của Feature Map đi một nửa. Mục đích là giảm chi phí tính toán và giúp mô hình bất biến với các dịch chuyển nhỏ của vật thể.

\subsection{Classifier (Khối Phân loại)}
Sau khi trích xuất đặc trưng, dữ liệu được đưa vào mạng Fully Connected để ra quyết định.
\begin{enumerate}
    \item \textbf{Flatten:} Duỗi tensor 3D (ví dụ $16 \times 16 \times 128$) thành vector 1D.
    \item \textbf{Dense Layers:} Các lớp ẩn kết nối đầy đủ.
    \item \textbf{Dropout:} Một kỹ thuật Regularization, ngẫu nhiên "tắt" một số nơ-ron (ví dụ 50\%) trong quá trình train để ngăn chặn Overfitting [3].
\end{enumerate}

\subsection{Output Layer (Đầu ra)}
Dựa trên đoạn code Inference, mô hình hỗ trợ hai dạng đầu ra, nhưng tối ưu nhất cho bài toán nhị phân là sử dụng \textbf{Sigmoid}:

\begin{equation}
    \sigma(z) = \frac{1}{1 + e^{-z}}
\end{equation}

\begin{itemize}
    \item Giá trị đầu ra $\hat{y} \in [0, 1]$ biểu thị xác suất ảnh là "Chó".
    \item Nếu $\hat{y} < 0.5 \rightarrow$ Mèo, $\hat{y} \ge 0.5 \rightarrow$ Chó.
\end{itemize}

\noindent\fbox{
    \parbox{\textwidth}{
        \textbf{Lưu ý:} Trong code deployment, chúng ta sử dụng thêm một ngưỡng tin cậy (\texttt{CONFIDENCE\_THRESHOLD = 0.7}). Nếu xác suất nằm trong khoảng $(0.3, 0.7)$, hệ thống sẽ trả về \textbf{"Unknown"}. Đây là cơ chế an toàn để tránh việc mô hình "đoán mò" khi gặp dữ liệu nhiễu.
    }
}

\section{Hàm Mất mát và Tối ưu hóa (Loss \& Optimizer)}

\textbf{Loss Function:} Sử dụng \textbf{Binary Cross-Entropy}:
\begin{equation}
    L = -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]
\end{equation}
Hàm này phạt nặng các dự đoán sai lệch lớn so với nhãn thực tế.

\textbf{Optimizer:} Sử dụng \textbf{Adam} (Adaptive Moment Estimation). Đây là thuật toán tối ưu phổ biến nhất hiện nay nhờ khả năng tự điều chỉnh learning rate cho từng tham số, giúp hội tụ nhanh hơn SGD truyền thống [4].

\section{Tổng kết Kiến trúc (Summary)}
Dưới đây là bảng tóm tắt kiến trúc mô hình đề xuất cho dự án (tương thích với input size 128 trong code):

\begin{table}[H]
\centering
\caption{Kiến trúc CNN chi tiết}
\vspace{0.3cm}
\begin{tabular}{@{}llrl@{}}
\toprule
\textbf{Layer (Type)} & \textbf{Output Shape} & \textbf{Param \#} & \textbf{Chức năng} \\ \midrule
Input & (128, 128, 3) & 0 & Nhận ảnh RGB \\
Conv2D + ReLU & (126, 126, 32) & $\approx$896 & Trích xuất đặc trưng cấp thấp \\
MaxPooling2D & (63, 63, 32) & 0 & Giảm chiều dữ liệu \\
Conv2D + ReLU & (61, 61, 64) & $\approx$18K & Trích xuất đặc trưng trung cấp \\
MaxPooling2D & (30, 30, 64) & 0 & Giảm chiều dữ liệu \\
Conv2D + ReLU & (28, 28, 128) & $\approx$73K & Trích xuất đặc trưng cao cấp \\
MaxPooling2D & (14, 14, 128) & 0 & Giảm chiều dữ liệu \\
Flatten & (25088) & 0 & Chuyển đổi sang vector \\
Dense + ReLU & (512) & $\approx$12.8M & Học quan hệ phi tuyến \\
Dropout (0.5) & (512) & 0 & Chống Overfitting \\
Dense (Output) & (1) & 513 & Dự đoán xác suất (Sigmoid) \\ \bottomrule
\end{tabular}
\end{table}

\begin{thebibliography}{9}
    \bibitem{lecun} LeCun, Y., et al. (1998). "Gradient-based learning applied to document recognition." \textit{Proceedings of the IEEE}.
    \bibitem{relu} Nair, V., \& Hinton, G. E. (2010). "Rectified linear units improve restricted boltzmann machines." \textit{ICML}.
    \bibitem{dropout} Srivastava, N., et al. (2014). "Dropout: A simple way to prevent neural networks from overfitting." \textit{JMLR}.
    \bibitem{adam} Kingma, D. P., \& Ba, J. (2014). "Adam: A Method for Stochastic Optimization." \textit{ICLR}.
\end{thebibliography}

\end{document}
