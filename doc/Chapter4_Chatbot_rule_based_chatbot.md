
# Chương 4 - Chatbot dựa trên Luật (Rule-Based Approach)
## 4.1. Khái niệm và cơ chế hoạt động

### Khái niệm

> ✏️ **Định nghĩa:** Là chatbot hoạt động dựa trên tập hợp các quy tắc và kịch bản được lập trình sẵn.

### Cơ chế hoạt động

Chatbot dựa trên luật hoạt động như một cấu trúc **If – Then** đã được hệ thống kịch bản hoá sẵn: **Nếu** người dùng nói A, chatbot sẽ trả lời B.

### Các phương thức nhập

- **Chatbot dựa trên nút bấm hoặc menu**: cung cấp cho người dùng danh sách các câu hỏi được xác định trước để lựa chọn và nhận câu trả lời tương ứng. Điều này đặt ra những giới hạn nghiêm ngặt cho cuộc hội thoại, vì vậy những chatbot này thường được sử dụng cho các dịch vụ hỗ trợ khách hàng cơ bản nhất.
- **Chatbot dựa trên nhận diện từ khóa**: cho phép người dùng tự đặt câu hỏi và chatbot sẽ nhận diện các từ khóa trong câu hỏi đó để đưa ra câu trả lời tương ứng. Tuy nhiên, chatbot nhận diện từ khóa có thể đưa ra câu trả lời không liên quan nếu từ khóa được diễn đạt khác với những từ khóa đã được định nghĩa trước trong cơ sở dữ liệu.
- **Chatbot lai**: kết hợp cả nút bấm/menu và nhận diện từ khóa trong một hệ thống, cho phép doanh nghiệp kết hợp ưu điểm của cả hai loại chatbot trên.

## 4.2. Quy trình xử lý thông tin

Quy trình này diễn ra theo 3 bước chính:

1. **Nhận diện (Input Analysis):** Khi người dùng nhập tin nhắn hoặc nhấn nút, chatbot sẽ quét văn bản đó để tìm **từ khóa (keywords)** hoặc mẫu câu cụ thể đã được cài đặt trước.
2. **Đối chiếu quy tắc (Rule Matching):** Hệ thống so sánh dữ liệu đầu vào với cơ sở dữ liệu các quy tắc. Ví dụ: nếu nội dung người dùng nhập có từ “giá”, hệ thống sẽ tìm câu trả lời tương ứng với nhóm quy tắc về “giá”.
3. **Phản hồi (Response):** Chatbot đưa ra câu trả lời đã được soạn sẵn (cố định). Nếu không tìm thấy quy tắc phù hợp, nó sẽ đưa ra thông báo mặc định (ví dụ: “Tôi không hiểu, vui lòng chọn lại”).

![Minh hoạ quy trình xử lý thông tin](image.png)

### Mô hình cây quyết định (Decision Tree)

Hầu hết các rule-based chatbot điều hướng người dùng đi qua một **cây quyết định**. Người dùng thường được cung cấp các **nút bấm (buttons)** hoặc **menu** để chọn, thay vì gõ văn bản tự do, nhằm tránh sai sót.

![Minh hoạ mô hình cây quyết định](image%201.png)

## 4.3. Ưu điểm – Nhược điểm

### Ưu điểm

- **Chi phí thấp:** Dễ xây dựng và triển khai, không cần dữ liệu huấn luyện lớn.
- **Kiểm soát hoàn toàn:** Doanh nghiệp kiểm soát chính xác 100% những gì chatbot nói.
- **Phản hồi nhanh:** Tốc độ xử lý cực nhanh vì chỉ là tra cứu quy tắc đơn giản.

### Nhược điểm

- **Cứng nhắc:** Chỉ hiểu đúng những gì đã lập trình. Nếu khách hàng gõ sai chính tả hoặc dùng từ đồng nghĩa mà chưa được cài đặt, bot sẽ không hiểu.
- **Khó mở rộng:** Muốn thêm tính năng mới, lập trình viên phải viết thêm quy tắc thủ công.
- **Trải nghiệm hạn chế:** Khách hàng có thể cảm giác giống như đang tương tác với một cỗ máy, không tự nhiên.

### So sánh với AI Chatbot

| Đặc điểm     | Rule-based Chatbot                   | AI Chatbot                              |
| ------------ | ------------------------------------ | --------------------------------------- |
| Cơ chế       | Quy tắc If–Then                      | Học máy & Xử lý ngôn ngữ tự nhiên (NLP) |
| Đầu vào      | Từ khóa chính xác, nút bấm           | Ngôn ngữ tự nhiên, ngữ cảnh phức tạp    |
| Khả năng học | Không tự học, phải cập nhật thủ công | Tự học từ dữ liệu và tương tác          |
| Độ linh hoạt | Thấp (rất cứng nhắc)                 | Cao (hiểu ý định, cảm xúc)              |

## 4.4. Cách xây dựng và cải thiện chatbot dựa trên luật

### Cách xây dựng

- Xác định mục tiêu và phạm vi hoạt động của chatbot.
- Xây dựng luồng hội thoại.
- Chọn nền tảng xây dựng chatbot.
- Soạn thảo nội dung và cài đặt.
- Kiểm thử và tối ưu.

### Cách cải thiện

- Sử dụng các tuỳ biến về tên, đại từ nhân xưng (theo giới tính), lịch sử mua hàng.
- Đa dạng kịch bản chat theo ngữ cảnh.
- Có tuỳ chọn “phản hồi khác” hoặc “gặp nhân viên” để doanh nghiệp không bỏ sót những thông tin mang tính cá biệt từ khách hàng, đồng thời để khách hàng không bị ức chế khi chatbot không giải quyết được vấn đề.
- Vẫn duy trì cá nhân trực hệ thống để phát hiện sai sót và tối ưu hoá kịch bản.
