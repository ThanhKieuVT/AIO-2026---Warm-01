## 3.1. Dataset & Exploratory Data Analysis (EDA)

Khi làm một dự án phân loại ảnh, nếu bạn chưa hiểu dữ liệu thì rất khó để có thể train Model hiệu quả, EDA là bước giúp bạn đọc dataset trước khi giao cho model.

Dataset cho project này được chúng mình lấy từ Kaggle, chứa **25,000 ảnh** chó và mèo. Điểm tiện của dataset này chính là nhãn nằm ngay trong tên file. Ví dụ file sẽ thường có dạng `cat.1234.jpg` hoặc `dog.5678.jpg`. Điều này giúp bạn tạo label nhanh, nhưng cũng cần cẩn thận không nên để pipeline vô tình dùng tên file như một đặc trưng để phân loại.

Mục tiêu là huấn luyện mô hình trên tập train và dự đoán nhãn cho tập test, với **12,500 ảnh**, tên file là số (không có nhãn trong tên). Nhiệm vụ là bạn sẽ dự đoán **xác suất là chó** cho từng ảnh, tức quy ước **1 = dog**, **0 = cat**.

---

### 3.1.1. Kiểm tra phân bố của nhãn

Trước khi huấn luyện, mình kiểm tra xem dataset có bị lệch lớp không. Dataset này khá cân bằng (gần 50/50), nên bài toán không đòi hỏi các kỹ thuật cân bằng dữ liệu phức tạp. Nhóm mình chia dataset ra thêm thành 3 tập nhỏ:

- **Training set**: 20,000 ảnh, dùng để cho mô hình học
- **Validation set**: 2,500 ảnh, kiểm tra chất lượng trên dữ liệu chưa từng thấy trong quá trình học
- **Testing set**: 2,500 ảnh, đây là bài test nội bộ, dùng để kiểm tra lần cuối trước khi chạy model trên tập test 12,500 ảnh của Kaggle

![dataset](dataset.png)


---

### 3.1.2. Kiểm tra ảnh

Về phần kiểm tra ảnh, trước hết chúng ta sẽ cần kiểm tra về kích thước, format, và độ đa dạng của dữ liệu. Dataset của chúng mình sử dụng có ảnh đến từ nhiều nguồn khác nhau trên internet và có độ đa dạng khá cao: có ảnh chụp bằng điện thoại, có ảnh chụp chuyên nghiệp hơn, có ảnh cận cảnh, có ảnh chụp xa, có ảnh nền trong nhà, có ảnh ngoài trời. Ngoài ra một vài ảnh khó còn có sự xuất hiện con người, hoặc có nhiều hơn một con mèo hoặc con chó.

Ảnh trong bộ này thường là **.jpg**, và là ảnh màu (RGB), có kích thước **không đồng nhất**. Và vì CNN cần input cùng kích thước, nên bạn sẽ phải **resize** về một size cố định. Ở project này, nhóm mình chọn resize ảnh về **128×128** vì nó cân bằng giữa tốc độ và độ chính xác

![sample_dog](sample_dog.png)

![sample_cat](sample_cat.png)

Đa số ảnh nằm trong một vài cụm kích thước phổ biến, nhưng sẽ có một vài ngoại lệ: có ảnh rất nhỏ, có ảnh cực lớn, có ảnh cực ngang hoặc cực dọc. Nếu không crop/pad hợp lý, ảnh có thể bị méo, khiến mô hình sẽ gặp khó khăn ít nhiều. Ngoài ra, chúng ta cũng cần kiểm tra trong dataset có file hỏng, file đọc được nhưng sai kênh màu, hoặc ảnh quá nhỏ khiến việc resize bị vỡ hạt hay không. Nhìn chung dataset này đủ lớn để model học được những đặc trưng thật của ảnh.

---

## 3.2. Metric & Evaluation Strategy

Khi đã hiểu về dataset, chúng ta sẽ cần xác định sẽ đo chất lượng mô hình bằng gì. Nghe khá đơn giản, chỉ cần đoán đúng mèo hay chó là được, thông số để thể hiện vấn đề này là **accuracy**. Nhưng nếu ta chỉ nhìn vào một con số accuracy, khả năng chúng ta sẽ đánh giá sai chất lượng của model là rất cao, trong khi thực tế nó chỉ học được vài pattern dễ hoặc đang bị overfit.

### 3.2.1. Accuracy

Mặc dù như đã nói, accuracy không đủ để đánh giá model, nhưng nó vẫn là một thông số cốt lõi và quan trọng. Đây cũng là một metric cơ bản và dễ hiểu nhất, nó trả lời đúng câu hỏi:

> “Trong tổng số ảnh, mô hình đoán đúng bao nhiêu ảnh?”

Công thức của nó khá đơn giản, accuracy bằng **số dự đoán đúng** chia cho **tổng số dự đoán**:

$$
Accuracy = \frac{\text{Number of correct predictions}}{\text{Total number of predictions}}
$$

Một điểm hợp lý nữa để sử dụng accuracy, chính là số lượng mèo và chó khá cân bằng trong dataset này. Nếu dữ liệu bị lệch nặng (ví dụ 95% là chó, 5% là mèo) thì accuracy sẽ đánh lừa, khiến chúng ta khó phân biệt được model đang tốt hay xấu. Vậy nên accuracy là một metric hợp lý để dùng làm "điểm tổng quan" khi báo cáo kết quả.

Tuy nhiên, accuracy có một giới hạn rằng: nó chỉ cho bạn biết kết quả đúng bao nhiêu, chứ không cho biết mô hình **đang sai kiểu gì** và **đang sai ở đâu**. Vì vậy, trong EDA và báo cáo, nhóm mình có đi kèm thêm một công cụ quan trọng: **Confusion Matrix**.

---

### 3.2.2 Confusion Matrix

Confusion matrix (ma trận nhầm lẫn) giúp bạn nhìn ra mô hình sai ở đâu, sai theo kiểu nào? Cụ thể:
- Có bao nhiêu ảnh **cat** bị đoán nhầm thành **dog**
- Có bao nhiêu ảnh **dog** bị đoán nhầm thành **cat**

Trong bài toán nhị phân, confusion matrix có 4 ô:
- **True Positive (TP)**: dog → đoán dog
- **True Negative (TN)**: cat → đoán cat
- **False Positive (FP)**: cat → đoán dog
- **False Negative (FN)**: dog → đoán cat

Giả sử bạn có 100 ảnh validation:
- 50 mèo, 50 chó  
    Mô hình dự đoán đúng 92 ảnh → accuracy = 92%

Nhưng confusion matrix có thể cho thấy:
- Mô hình đoán nhầm 6 ảnh mèo thành chó (FP=6)
- Mô hình đoán nhầm 2 ảnh chó thành mèo (FN=2)

![example_matrix](example_matrix.png)

Nhìn vào đây, ta có thể hiểu ngay mô hình đang thiên về đoán chó đúng nhiều hơn (hoặc gặp khó với những ảnh mèo có nền giống chó). Đây là thông tin mà accuracy một mình không thể hiện rõ. Ngoài ra, một lý do khiến confusion matrix quan trọng là khi bạn cải thiện mô hình, bạn không chỉ muốn “accuracy tăng” mà còn muốn giảm đúng loại lỗi bạn quan tâm.

---

### 3.2.3. Classification report

Trong bài toán này, việc nhầm mèo thành chó hay chó thành mèo thường tương đương nhau về mặt bài toán, vì vậy nên accuracy là đủ để bắt đầu. Nhưng để đầy đủ hơn, ta còn có **Precision** và **Recall**, là những metric giúp chúng ta hiểu sâu hơn từ confusion matrix. Hiểu đơn giản như sau:

- **Precision ( giả sử tính cho class dog)**:  
    Trong tất cả ảnh mà mô hình đoán là “dog”, có bao nhiêu ảnh thật sự là dog?  
    Precision cao nghĩa là mô hình ít “gán nhầm dog”.

- **Recall (giả sử tính cho class dog)**:  
    Trong tất cả ảnh dog thật, mô hình tìm ra được bao nhiêu ảnh?  
    Recall cao nghĩa là mô hình ít “bỏ sót dog”.

- **F1-score**: trung bình điều hòa giữa precision và recall

$$
F1 = \frac{2*Precision*Recall}{Precision + Recall}
$$

	F1 chỉ cao khi precision và recall cùng cao, dùng khi bạn muốn model **không nhầm nhiều** và cũng **không bỏ sót nhiều**.

Với bài toán cân bằng lớp như Cats vs Dogs, Precision/Recall thường được dùng để so sánh các phiên bản mô hình khi **accuracy tương đương**, và hiểu rõ mô hình đang sai theo hướng nào.

---

### 3.2.4. Validation

Một sai lầm phổ biến như đã đề cập là sau khi train xong, chúng ta thấy chỉ số accuracy trên train cao rồi kết luận mô hình tốt. Nhưng như đã nói, accuracy không đủ để đánh giá mô hình tốt hay chưa. Mô hình hoàn toàn có thể “học thuộc” ảnh train và không tổng quát được, đây gọi là **overfitting**.

Dễ hiểu về **overfit (overfitting)** là khi mô hình học quá kỹ dữ liệu train, đến mức nó nhớ những chi tiết riêng của tập train, kể cả dữ liệu nhiễu. Nên khi đó thông số accuracy khi train rất cao hoặc train loss rất thấp. Nhưng khi đem model đi thử nghiệm trên những tập dữ liệu khác dữ liệu được train, accuracy lại giảm và có khi giảm rất nhiều. Đó là lí do vì sao chúng ta cần chia dataset ra thêm 2 tập nhỏ là validation set và testing set nội bộ.

Một tỉ lệ chia phổ biến là 80/10/10 (80/20 nếu bạn chỉ cần 2 bộ) hoặc 70/15/15 (70/30). Quan trọng nhất là đảm bảo cat/dog trong data train và validation/testing data vẫn cân bằng, ngoài ra validation/testing data phải thực sự độc lập với data train.

> Validation giống như một bài kiểm tra giữa kỳ. Mô hình học từ training data, nhưng điểm số phải dựa trên validation data để biết nó có thật sự hiểu bài hay chỉ học thuộc.

#### Dấu hiệu overfitting

Trong bài dự án phân loại Cats and Dogs này, overfitting thường xảy ra vì dataset có độ đa dạng cao, dẫn đến việc model có thể học cảnh vật, nên xung quanh thay vì con vật. Ngoài ra việc train quá lâu cũng dễ khiến model học thuộc các chi tiết riêng, từ đó mô hình không còn khả năng tự tổng quát.

Dấu hiệu dễ thấy nhất khi train:

- Train Loss giảm đều
- Loss trên validation data bắt đầu tăng
- Accuracy trên validation data đứng hoặc giảm

Khi gặp tình huống đó, nghĩa là mô hình đang overfitting. Đây là lý do chúng ta cần validation set, theo dõi curve loss/accuracy, và các kỹ thuật chống overfit như augmentation, dropout, early stopping,…
