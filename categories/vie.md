## 2. Phân nhóm các thuật toán machine learning

### 2.1 Supervised learning (Học có giám sát)

**Supervised learning** là phương pháp học máy trong đó mô hình được huấn luyện trên tập dữ liệu **đã được gán nhãn**. Mỗi mẫu dữ liệu bao gồm **đầu vào** và **đầu ra** mong muốn. Mục tiêu của mô hình là học được mối quan hệ ánh xạ từ đầu vào sang đầu ra để có thể dự đoán chính xác nhãn của các dữ liệu mới **chưa từng quan sát**.

**Ví dụ:**  
Trong bài toán phân loại các bức ảnh chó mèo, ta có dữ liệu huấn luyện gồm hàng nghìn bức ảnh đã được gán nhãn sẵn là `"cat"` hoặc `"dog"`. Chúng ta đưa các bức ảnh này vào trong một thuật toán và chỉ cho nó biết mỗi bức ảnh tương ứng là chó hay mèo. Sau khi thuật toán tạo ra một mô hình, tức một hàm số mà đầu vào là một bức ảnh và đầu ra là một nhãn, khi nhận được một bức ảnh mới mà mô hình **chưa nhìn thấy bao giờ**, nó sẽ dự đoán bức ảnh đó là chó hay mèo.

<figure>
  <img src="./images/supervised learning.png" 
       alt="supervised learning" 
       width="700">
  <figcaption>
    <em>Hình 2.1: Quy trình supervised learning.</em>
  </figcaption>
</figure>

**Ứng dụng:**  
Supervised learning được sử dụng rộng rãi trong các hệ thống dự đoán và ra quyết định như phát hiện gian lận tài chính, chẩn đoán bệnh, nhận dạng hình ảnh và xử lý ngôn ngữ tự nhiên.

Thuật toán supervised learning còn được tiếp tục chia nhỏ ra thành hai loại chính:

---

#### 2.1.1 Classification (Phân loại)

**Classification** là bài toán học có giám sát trong đó đầu ra là nhãn rời rạc. Mục tiêu của mô hình là gán mỗi mẫu dữ liệu đầu vào vào một trong các lớp đã xác định trước.

**Ví dụ:**  
Gmail xác định xem một email có phải là spam hay không; các hãng tín dụng xác định xem một khách hàng có khả năng thanh toán nợ hay không. 

**Một số thuật toán tiêu biểu:**  
- Logistic Regression  
- k-Nearest Neighbors (k-NN)  
- Support Vector Machine (SVM)  
- Decision Tree  

---

#### 2.1.2 Regression (Hồi quy)

**Regression** là bài toán học có giám sát trong đó đầu ra là giá trị liên tục. Mục tiêu của mô hình là dự đoán một đại lượng số dựa trên dữ liệu đầu vào.

**Ví dụ:**  
Một căn nhà rộng x m2, có y phòng ngủ và cách trung tâm thành phố z km sẽ có giá là bao nhiêu?

**Một số thuật toán tiêu biểu:**  
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Decision Tree Regression  

---

### 2.2 Unsupervised learning (Học không giám sát)

**Unsupervised learning** là phương pháp học máy trong đó dữ liệu huấn luyện **không có nhãn**. Thuật toán sẽ dựa vào cấu trúc của dữ liệu để thực hiện một công việc nào đó, ví dụ như phân nhóm (clustering) hoặc giảm số chiều của dữ liệu (dimension reduction) để thuận tiện trong việc lưu trữ và tính toán.

Supervised learning phù hợp khi dữ liệu đã được gán nhãn và mục tiêu là dự đoán chính xác đầu ra. Ngược lại, Unsupervised learning được sử dụng khi dữ liệu chưa có nhãn, nhằm khám phá cấu trúc hoặc mẫu hình ẩn trong dữ liệu.

**Ứng dụng:**  
Unsupervised learning thường được dùng trong phân tích dữ liệu thăm dò, phân khúc khách hàng, phát hiện bất thường và tiền xử lý dữ liệu trước khi áp dụng các mô hình có giám sát.

Các bài toán Unsupervised learning được tiếp tục chia nhỏ thành hai loại:

---

#### 2.2.1 Clustering (phân nhóm)

Là một bài toán phân nhóm toàn bộ dữ liệu X thành các nhóm nhỏ dựa trên sự liên quan giữa các dữ liệu trong mỗi nhóm.

**Ví dụ:** Phân cụm khách hàng  
Giả sử ta có dữ liệu của hàng nghìn khách hàng, bao gồm các đặc trưng như độ tuổi, thu nhập, tần suất mua sắm và giá trị hóa đơn trung bình. Tập dữ liệu này không chứa nhãn cho biết khách hàng thuộc nhóm nào. Thuật toán học không giám sát được áp dụng để tự động phân chia các khách hàng thành những cụm khác nhau dựa trên mức độ tương đồng của các đặc trưng. Kết quả phân cụm giúp doanh nghiệp nhận diện các nhóm khách hàng có hành vi tương tự mà không cần thông tin phân loại có sẵn trước đó.

<figure>
  <img src="./images/clustering.png" 
       alt="clustering" 
       width="700">
  <figcaption>
    <em>Figure 2.2: Phân cụm khách hàng.</em>
  </figcaption>
</figure>

**Một số thuật toán tiêu biểu:**  
- K-means  
- Hierarchical Clustering  
- DBSCAN  

---

#### 2.2.2 Association rule (Luật kết hợp)

Là một dạng học không giám sát nhằm khai phá các mối quan hệ hoặc quy luật thường xuyên giữa các đối tượng trong dữ liệu, mà không cần nhãn đầu ra.

**Ví dụ:**  
những khách hàng nam mua quần áo thường có xu hướng mua thêm đồng hồ hoặc thắt lưng; những khán giả xem phim Spider Man thường có xu hướng xem thêm phim Bat Man, dựa vào đó tạo ra một hệ thống gợi ý khách hàng (Recommendation System), thúc đẩy nhu cầu mua sắm.

**Một số thuật toán tiêu biểu:**  
- Apriori  
- FP-Growth  
- Eclat  

---

### 2.3 Semi-supervised learning (Học bán giám sát)

**Semi-supervised learning** là phương pháp học máy kết hợp giữa học có giám sát và học không giám sát, trong đó tập dữ liệu huấn luyện gồm một phần nhỏ dữ liệu có nhãn và một phần lớn dữ liệu không có nhãn. Mục tiêu là tận dụng dữ liệu không nhãn để cải thiện hiệu quả học so với việc chỉ sử dụng dữ liệu có nhãn.

**Ví dụ:**  
Trong bài toán nhận dạng chữ viết tay, giả sử ta chỉ có một số ít ảnh chữ số được gán nhãn chính xác, trong khi phần lớn ảnh còn lại không có nhãn. Thuật toán học bán giám sát sử dụng các ảnh đã gán nhãn để định hướng quá trình học, đồng thời khai thác cấu trúc của dữ liệu không nhãn nhằm nâng cao độ chính xác khi dự đoán chữ số trong các ảnh mới.

**Ứng dụng:**  
Semi-supervised learning được sử dụng rộng rãi trong các bài toán mà dữ liệu có nhãn khan hiếm hoặc tốn kém chi phí gán nhãn. Phương pháp này đặc biệt hiệu quả trong các lĩnh vực như nhận dạng hình ảnh, xử lý ngôn ngữ tự nhiên và dữ liệu y sinh, nơi việc gán nhãn thường đòi hỏi chuyên gia.

**Một số thuật toán tiêu biểu:**  
- Self-training (Pseudo-labeling)  
- Label Propagation  

---

### 2.4 Reinforcement learning (Học tăng cường)

Reinforcement learning là phương pháp học máy trong đó một **tác nhân (agent)** học cách đưa ra hành động thông qua tương tác trực tiếp với **môi trường**. Thay vì học từ dữ liệu có nhãn, tác nhân nhận được **phần thưởng (reward)** hoặc **hình phạt (penalty)** sau mỗi hành động và dần dần học được chiến lược tối ưu nhằm tối đa hóa tổng phần thưởng trong dài hạn.

**Ví dụ:** Robot học cách di chuyển  
Giả sử một robot được đặt trong một môi trường có nhiều chướng ngại vật và mục tiêu cần đạt tới. Robot không được cung cấp trước đường đi đúng mà chỉ nhận được phần thưởng khi tiến gần đến mục tiêu và hình phạt khi va chạm hoặc đi sai hướng. Thông qua quá trình tương tác liên tục với môi trường và thử–sai các hành động, robot dần học được một chiến lược tối ưu để di chuyển đến mục tiêu với hiệu quả cao nhất.

**Ứng dụng:**  
Reinforcement learning phù hợp với các bài toán ra quyết định tuần tự, trong đó mô hình cần học chiến lược tối ưu thông qua tương tác với môi trường và phản hồi từ phần thưởng. Phương pháp này được áp dụng trong các hệ thống tự động và môi trường động, nơi không tồn tại dữ liệu gán nhãn sẵn.

**Một số thuật toán tiêu biểu:**  
- Q-learning  
- SARSA  
- Deep Q-Network (DQN)


