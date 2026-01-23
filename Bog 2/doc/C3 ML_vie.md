# 3. Lộ trình 4 bước cho người mới bắt đầu

Đối với người mới, Machine Learning thường bị “thần thánh hóa” như một lĩnh vực thuần toán học và thuật toán phức tạp. Trên thực tế, nếu tiếp cận đúng cách và đi theo lộ trình phù hợp, bạn hoàn toàn có thể xây dựng nền tảng vững chắc trong thời gian tương đối ngắn. Dưới đây là lộ trình 4 bước cơ bản, được nhiều chuyên gia và chương trình đào tạo áp dụng cho người mới bắt đầu.

## 3.1. Chuẩn bị kiến thức nền tảng

Machine Learning không thể tách rời khỏi toán học và lập trình. Tuy nhiên, bạn không cần trở thành nhà toán học – điều quan trọng là bạn cần hiểu bản chất và cách các khái niệm được áp dụng.

Về Toán học, cần tập trung vào ba mảng chính. 
- Đại số tuyến tính giúp bạn hiểu cách dữ liệu được biểu diễn dưới dạng vector, ma trận và cách các mô hình “học” thông qua phép biến đổi tuyến tính. 

- Giải tích, đặc biệt là đạo hàm, đóng vai trò cốt lõi trong việc tối ưu hóa hàm mất mát (loss function). 
- Xác suất thống kê giúp bạn hiểu dữ liệu, phân 1phối xác suất, kỳ vọng, phương sai và cách đánh giá độ tin cậy của mô hình.

Về lập trình, Python là lựa chọn phổ biến và gần như bắt buộc cho người mới. Bạn cần nắm vững cú pháp cơ bản, cấu trúc dữ liệu (list, dict, tuple), hàm, vòng lặp, và đặc biệt là làm quen với các thư viện nền tảng như NumPy, Pandas và Matplotlib để xử lý và trực quan hóa dữ liệu.

## 3.2. Các thuật toán nhập môn cần biết

Trước khi đi sâu vào thuật toán, người học cần hiểu cách một bài toán Machine Learning được hình thành. Điều này bao gồm việc phân biệt học có giám sát (supervised learning) và học không giám sát (unsupervised learning), hiểu thế nào là dữ liệu đầu vào (features), nhãn (labels), tập huấn luyện, tập kiểm tra, cũng như các khái niệm như overfitting và underfitting.

Khi đã có nền tảng, bạn nên bắt đầu với các thuật toán cơ bản, vừa dễ hiểu vừa mang tính nền móng cho các mô hình phức tạp hơn sau này.

- Linear Regression (Hồi quy tuyến tính) là thuật toán đơn giản nhất nhưng cực kỳ quan trọng. Nó giúp bạn hiểu cách mô hình học mối quan hệ giữa biến đầu vào và đầu ra thông qua việc tối ưu hóa sai số. Gần như mọi khái niệm cốt lõi của Machine Learning – từ hàm mất mát đến gradient descent – đều có thể được minh họa rõ ràng qua hồi quy tuyến tính.

- Logistic Regression tuy có tên là “regression” nhưng thực chất là thuật toán phân loại. Đây là bước chuyển tiếp hoàn hảo từ bài toán dự đoán giá trị liên tục sang bài toán phân loại nhị phân, giúp người học hiểu xác suất dự đoán và ngưỡng quyết định (decision boundary).

- Decision Tree (Cây quyết định) mang lại góc nhìn trực quan về cách mô hình ra quyết định. Thuật toán này giúp bạn hiểu rõ cách chia dữ liệu theo các điều kiện, đồng thời là nền tảng để tiếp cận các mô hình mạnh hơn như Random Forest và Gradient Boosting.

- K-Means Clustering đại diện cho nhóm thuật toán học không giám sát. Thông qua K-Means, bạn sẽ hiểu cách mô hình tự động tìm ra cấu trúc tiềm ẩn trong dữ liệu mà không cần nhãn, một tư duy rất khác so với học có giám sát.