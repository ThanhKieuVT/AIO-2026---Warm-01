# Tổng quan về chatbot dựa trên truy xuất

## 1. Định nghĩa và đặt nền tảng

Chatbot dựa trên truy xuất (*retrieval-based chatbot*) là phương pháp xây dựng chatbot trong đó hệ thống **không tự sinh ra câu trả lời mới**, mà **lựa chọn câu trả lời phù hợp nhất** từ một tập dữ liệu hoặc cơ sở tri thức đã được chuẩn bị sẵn. Việc lựa chọn này dựa trên **mức độ tương đồng** giữa câu hỏi của người dùng và các mẫu câu hỏi – trả lời đã được lưu trữ.

So với chatbot dựa trên quy tắc, chatbot retrieval-based **linh hoạt hơn** vì không phụ thuộc hoàn toàn vào các điều kiện cố định. Tuy nhiên, khác với chatbot dựa trên mô hình sinh, chatbot retrieval-based vẫn đảm bảo **tính kiểm soát nội dung cao** do chỉ sử dụng các phản hồi có sẵn. Nhờ đó, phương pháp này được ứng dụng rộng rãi trong các hệ thống chatbot doanh nghiệp, đặc biệt là trong **chăm sóc khách hàng** và **tư vấn thông tin**.

---

## 2. Luồng hoạt động

Mặc dù có nhiều biến thể khác nhau, chatbot dựa trên truy xuất nhìn chung tuân theo một luồng hoạt động chung gồm các bước sau:

1. **Tiếp nhận đầu vào**: Người dùng nhập câu hỏi hoặc yêu cầu thông qua giao diện chatbot.  
2. **Tiền xử lý ngôn ngữ**: Hệ thống chuẩn hóa văn bản đầu vào, chẳng hạn như chuyển về chữ thường, loại bỏ ký tự đặc biệt hoặc tách từ.  
3. **Phân tích và hiểu câu hỏi**: Câu hỏi của người dùng được biểu diễn dưới một dạng phù hợp để phục vụ truy xuất, có thể là tập từ khóa, vector ngữ nghĩa hoặc thông tin về ý định.  
4. **Truy xuất phản hồi**: Hệ thống so sánh biểu diễn của câu hỏi với các mục trong cơ sở dữ liệu và tìm ra các phản hồi phù hợp nhất.  
5. **Lựa chọn câu trả lời**: Chatbot chọn phản hồi có mức độ phù hợp cao nhất theo tiêu chí đã xác định.  
6. **Phản hồi người dùng**: Câu trả lời được gửi lại cho người dùng.

Luồng này có thể được tóm tắt như sau:

> **User → Preprocessing → Understanding → Retrieval → Response**

Luồng hoạt động trên là khung xử lý chung cho mọi chatbot retrieval-based; sự khác biệt giữa các phương pháp chủ yếu nằm ở bước **Understanding**.

---

## 3. Cơ chế truy xuất

Trong chatbot retrieval-based, **retrieval** là cơ chế trung tâm quyết định chất lượng của câu trả lời. Cơ chế này có nhiệm vụ tìm kiếm và lựa chọn phản hồi phù hợp nhất từ tập dữ liệu có sẵn dựa trên mức độ tương đồng với câu hỏi của người dùng.

Về bản chất, cơ chế truy xuất luôn bao gồm ba bước chính:

- Biểu diễn câu hỏi của người dùng dưới một dạng nhất định  
- So sánh biểu diễn này với các mục trong cơ sở dữ liệu  
- Lựa chọn phản hồi có độ phù hợp cao nhất  

Cách biểu diễn câu hỏi có thể rất khác nhau, tùy thuộc vào mức độ “hiểu” mà chatbot được thiết kế để đạt tới. Một số hệ thống chỉ dựa trên từ khóa xuất hiện trong câu hỏi, trong khi các hệ thống khác cố gắng nắm bắt **ý nghĩa** hoặc **mục đích** của người dùng. Chính sự khác biệt này dẫn đến nhiều phương pháp xây dựng chatbot truy xuất khác nhau.

---

## 4. Các cách “hiểu” của chatbot dựa trên truy xuất

Mặc dù sử dụng cùng một cơ chế retrieval, chatbot retrieval-based có thể khác nhau đáng kể về khả năng hiểu ngôn ngữ tự nhiên. Dựa trên mức độ hiểu câu hỏi của người dùng, các chatbot dựa trên truy xuất có thể được phân thành ba nhóm chính.

---

### 4.1 Chatbot truy xuất dựa trên từ khóa (Keyword-based Retrieval)

Chatbot truy xuất dựa trên từ khóa là dạng đơn giản nhất của chatbot retrieval-based. Trong phương pháp này, hệ thống xử lý câu hỏi của người dùng bằng cách tách câu thành các từ hoặc cụm từ quan trọng, sau đó so sánh những từ khóa này với các từ khóa đã được lưu trữ trong cơ sở dữ liệu.

Mức độ phù hợp giữa câu hỏi và dữ liệu được xác định dựa trên số lượng và tần suất các từ khóa trùng khớp. Câu trả lời tương ứng với mục có độ trùng khớp cao nhất sẽ được chọn và trả về cho người dùng.

Các kỹ thuật thường được sử dụng bao gồm **Bag-of-Words (BoW)** và **TF-IDF**, kết hợp với các thước đo độ tương đồng như **Cosine Similarity**. Do chỉ dựa trên sự xuất hiện và tần suất của từ, chatbot loại này không thực sự hiểu ngữ nghĩa của câu hỏi.

**Ưu điểm**: Dễ triển khai, chi phí tính toán thấp.  
**Hạn chế**: Khả năng xử lý ngữ nghĩa kém, khó nhận diện các câu hỏi diễn đạt khác nhau nhưng có cùng ý nghĩa.

---

### 4.2 Chatbot truy xuất dựa trên ngữ nghĩa (Semantic Retrieval)

Để khắc phục hạn chế của phương pháp dựa trên từ khóa, chatbot truy xuất dựa trên ngữ nghĩa được phát triển nhằm biểu diễn câu hỏi của người dùng ở mức độ **ý nghĩa**.

Trong phương pháp này, câu hỏi được chuyển thành một **vector số** trong không gian đặc trưng thông qua các mô hình học máy, sao cho những câu hỏi có nội dung tương tự sẽ có vị trí gần nhau.

Khi người dùng nhập câu hỏi mới, chatbot so sánh vector của câu hỏi này với các vector đã được lưu trữ và chọn phản hồi gắn với câu hỏi có biểu diễn ngữ nghĩa gần nhất.

Các mô hình embedding như **Word2Vec**, **GloVe** hoặc các mô hình embedding câu hiện đại thường được sử dụng. Nhờ đó, chatbot có thể nhận diện các câu hỏi có cách diễn đạt khác nhau nhưng mang cùng một nội dung.

Tuy nhiên, chatbot loại này vẫn **chưa xác định rõ ý định của người dùng**, mà chỉ dựa trên mức độ tương đồng về nội dung.

---

### 4.3 Chatbot truy xuất kết hợp nhận diện ý định (Intent-based Retrieval)

Chatbot truy xuất kết hợp nhận diện ý định là dạng nâng cao của chatbot retrieval-based, trong đó hệ thống không chỉ đánh giá mức độ tương đồng ngữ nghĩa mà còn xác định **ý định (intent)** của người dùng.

Câu hỏi của người dùng trước hết được đưa qua mô-đun nhận diện ý định để gán nhãn intent phù hợp. Sau đó, chatbot chỉ thực hiện truy xuất trong phạm vi các phản hồi thuộc intent đó, giúp quá trình phản hồi trở nên chính xác và có định hướng hơn.

Nhận diện ý định không trực tiếp tạo ra câu trả lời mà đóng vai trò **định hướng cho quá trình truy xuất**, đặc biệt hiệu quả trong các hệ thống có cấu trúc nghiệp vụ rõ ràng như chăm sóc khách hàng hoặc tài chính – ngân hàng.

---

## 5. Quy trình xây dựng một chatbot truy xuất

Dù sử dụng kỹ thuật từ khóa đơn giản hay các thuật toán ngữ nghĩa phức tạp, quy trình tạo ra một chatbot dựa trên truy xuất đều xoay quanh việc xây dựng một **hệ thống tìm kiếm thu nhỏ**. Quy trình này bao gồm ba bước nền tảng:

### Bước 1: Xây dựng cơ sở tri thức (Knowledge Base Construction)

Người phát triển xây dựng một kho dữ liệu bao gồm các cặp **câu hỏi mẫu (query)** và **câu trả lời (response)**.

- Với chatbot từ khóa/ngữ nghĩa: Dữ liệu là danh sách các câu hỏi thường gặp và câu trả lời tương ứng.  
- Với chatbot nhận diện ý định: Dữ liệu được gom nhóm theo các **intent**.

> **Mấu chốt**: Chất lượng và độ phủ của kho dữ liệu quyết định trực tiếp độ thông minh của chatbot.

---

### Bước 2: Biểu diễn và số hóa dữ liệu (Data Representation)

Toàn bộ câu hỏi mẫu cần được chuyển sang dạng biểu diễn toán học thông qua:
- Đánh chỉ mục từ khóa (*Indexing*)
- Vector hóa câu hỏi (*Vectorization*)

Bước này giúp hệ thống có thể nhanh chóng tính toán độ tương đồng khi nhận câu hỏi mới.

---

### Bước 3: So khớp và xếp hạng (Matching & Ranking Logic)

Hệ thống thực hiện:
- **Tính điểm tương đồng (Similarity Score)** giữa câu hỏi người dùng và dữ liệu đã lưu  
- **Thiết lập ngưỡng tin cậy (Confidence Threshold)**  

Nếu không có phản hồi nào vượt ngưỡng, chatbot sẽ trả về phản hồi mặc định (*fallback*) để tránh trả lời sai.

---

## 6. Ưu và nhược điểm

### Ưu điểm
- Độ chính xác cao  
- Dễ kiểm soát nội dung  
- Chi phí triển khai thấp  
- Phù hợp với các hệ thống yêu cầu tính ổn định  

### Nhược điểm
- Phụ thuộc lớn vào chất lượng và phạm vi dữ liệu  
- Khó phản hồi linh hoạt với câu hỏi ngoài tập dữ liệu  
- Khả năng hội thoại tự nhiên còn hạn chế so với chatbot sinh
