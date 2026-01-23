# 2. Cách thức hoạt động của Chatbot

## 2.1. Tổng quan luồng hoạt động của Chatbot

Về cơ bản, một chatbot AI hoạt động theo một **pipeline xử lý (luồng xử lý)** gồm nhiều bước liên tiếp.  
Mỗi bước đảm nhiệm một vai trò riêng, giúp chatbot có thể **hiểu câu hỏi của người dùng và tạo ra câu trả lời phù hợp**.

Luồng hoạt động tổng quát của chatbot AI được minh họa trong **Hình 2.1** và có thể mô tả theo các bước sau.

<figure>
  <img src="../image/Pasted image 20260116172851.png" alt="Luồng hoạt động của chatbot AI" width="700">
  <figcaption><em>Hình 2.1: Luồng xử lý cơ bản của một chatbot AI.</em></figcaption>
</figure>

---

### 🔹 Bước 1: Người dùng nhập dữ liệu (Input from user)

Quá trình bắt đầu khi **người dùng nhập câu hỏi hoặc yêu cầu** cho chatbot.

Dữ liệu đầu vào có thể ở nhiều dạng khác nhau, phổ biến nhất là:

- **Văn bản** (người dùng gõ câu hỏi)
- **Giọng nói** (đối với các trợ lý ảo như Google Assistant, Siri)

**Ví dụ:**

> “Thời tiết hôm nay thế nào?”  
> “Tôi muốn đặt lịch hẹn.”

Ở bước này, chatbot **chưa hiểu nội dung câu hỏi**, mà chỉ tiếp nhận **dữ liệu thô** từ người dùng.

---

### 🔹 Bước 2: Phân tích yêu cầu của người dùng

_(Analyze user’s request)_

Sau khi nhận dữ liệu đầu vào, chatbot tiến hành **phân tích câu hỏi** bằng các kỹ thuật **Xử lý ngôn ngữ tự nhiên (NLP)**.

Mục tiêu của bước này bao gồm:

- Làm sạch câu chữ
- Tách từ
- Chuẩn hóa ngôn ngữ
- Giảm nhiễu do lỗi chính tả hoặc cách diễn đạt khác nhau

**Ví dụ:**

> “Cho mình hỏi hôm nay trời có mưa không?”

Câu hỏi được phân tích thành một yêu cầu liên quan đến **thời tiết**, với các thông tin chính là **hôm nay** và **mưa**.

---

### 🔹 Bước 3: Nhận diện ý định và thực thể

_(Identify intent and entities)_

Ở bước này, chatbot xác định hai thành phần quan trọng:

- **Ý định (Intent):** người dùng muốn làm gì?
- **Thực thể (Entities):** các thông tin quan trọng xuất hiện trong câu hỏi

**Ví dụ:**

| Thành phần | Giá trị                 |
| ---------- | ----------------------- |
| Intent     | Hỏi thông tin thời tiết |
| Entities   | Thời gian: hôm nay      |

Việc nhận diện đúng **ý định** và **thực thể** giúp chatbot **trả lời chính xác và đúng ngữ cảnh**, ngay cả khi người dùng diễn đạt theo nhiều cách khác nhau.

---

### 🔹 Bước 4: Tạo câu trả lời

_(Compose reply)_

Dựa trên ý định đã xác định, chatbot tiến hành:

- Truy vấn dữ liệu (nếu có)
- Áp dụng các luật hoặc logic xử lý
- Hoặc sử dụng mô hình AI để sinh câu trả lời

Kết quả cuối cùng là một phản hồi **tự nhiên, dễ hiểu và phù hợp với ngữ cảnh**.

**Ví dụ:**

> “Hôm nay trời có mưa nhẹ vào buổi chiều, bạn nên mang theo áo mưa.”

---

## 2.2. Phân loại Chatbot và cách thức hoạt động của từng loại

Dựa trên cách xử lý và tạo phản hồi, chatbot có thể được chia thành **ba nhóm chính**:

- **Rule-based chatbot**
- **Retrieval-based chatbot**
- **Generative chatbot**

Mỗi loại chatbot có **cách thức hoạt động**, **mức độ thông minh** và **phạm vi ứng dụng** khác nhau.

---

### 2.2.1. Rule-based Chatbot (Chatbot dựa trên luật)

**Rule-based chatbot** hoạt động dựa trên một tập **luật và kịch bản được định nghĩa sẵn**.  
Chatbot sử dụng các cấu trúc như **IF–ELSE** hoặc **cây quyết định** để xác định câu trả lời phù hợp với đầu vào của người dùng.

Loại chatbot này thường được sử dụng trong các hệ thống đơn giản, có phạm vi hội thoại hẹp.

---

### 2.2.2. Retrieval-based Chatbot (Chatbot truy xuất câu trả lời)

**Retrieval-based chatbot** sử dụng AI để **lựa chọn câu trả lời phù hợp nhất** từ một tập dữ liệu có sẵn.

Đặc điểm chính:

- Không tự sinh câu trả lời mới
- Truy xuất câu trả lời gần nhất trong cơ sở dữ liệu
- Độ ổn định cao hơn rule-based chatbot

---

### 2.2.3. Generative Chatbot (Chatbot sinh nội dung)

**Generative chatbot** có khả năng **tự sinh câu trả lời mới**, thay vì chọn từ các câu trả lời có sẵn.

Loại chatbot này thường sử dụng **mô hình ngôn ngữ lớn (Large Language Models – LLMs)**, cho phép hội thoại linh hoạt và tự nhiên hơn.

---

## Tài liệu tham khảo

1. [How Do Chatbots Work? – BotsCrew](https://botscrew.com/blog/what-are-bots/)
2. Building Vietnamese Chatbot using LLMs and RLHF – AI Vietnam
