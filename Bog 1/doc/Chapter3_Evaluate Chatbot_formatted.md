# Chương 3 - Đánh giá chất lượng Chatbot

Bạn có bao giờ gặp trường hợp chatbot trả lời lúc đúng, lúc sai không ổn định? Hoặc chỉ cần thay đổi một chút prompt là chất lượng trả lời bị giảm đi. Đối với những chatbot ứng dụng RAG (Retrieval-Augmented Generation), có lúc chatbot tìm đúng thông tin, nhưng cũng có lúc lại tìm sai. Hay với các Tool/Function Calling chatbot, có thể bot gọi nhầm tool, sai tham số hoặc làm sai quy trình... Khi chúng ta làm chatbot, nếu chỉ thử qua loa với vài câu đơn giản mà không kiểm tra kỹ chất lượng của nó, chúng ta rất dễ gặp phải những vấn đề trên.

Vì vậy, việc đánh giá chatbot (evaluation) là vô cùng cần thiết. Đánh giá chatbot không chỉ đơn giản là chuyện chấm câu trả lời có chính xác hay không, mà cần phải đánh giá toàn bộ hệ thống chatbot. Bạn có thể hình dung chatbot có thể được chia làm 4 cấp độ, và cách đánh giá cũng lớn dần theo mỗi cấp:

- **Level 1:** Chatbot LLM cơ bản (trả lời câu hỏi đơn giản, chat)
- **Level 2:** Chatbot có **memory** (trí nhớ hội thoại)
- **Level 3:** Chatbot có **RAG** (đọc và trả lời dựa trên tài liệu / knowledge base)
- **Level 4:** Chatbot sử dụng **tools/agent** (gọi hàm hoặc thực hiện các tác vụ thực tế)

Mỗi cấp độ sẽ có các yếu tố đánh giá khác nhau, và càng lên cao, việc đánh giá lại càng trở nên phức tạp hơn.

---

## 3.1. Nguyên tắc đánh giá theo 3 lớp

Dưới đây là ba lớp đánh giá chính mà bạn cần hiểu và áp dụng khi làm việc với chatbot, đặc biệt là chatbot AI, giúp bạn có cái nhìn tổng quan và chi tiết hơn về chất lượng của chatbot.

### Lớp A — Chất lượng nội dung (LLM Quality):

Đây là lớp cơ bản và quan trọng nhất, đặc biệt đối với các chatbot sử dụng **Large Language Models** (LLM). Những chatbot này dựa vào mô hình ngôn ngữ để trả lời câu hỏi và phản hồi yêu cầu của người dùng. Vì vậy, **chất lượng nội dung** sẽ quyết định trực tiếp đến mức độ hữu ích và chính xác của chatbot.
Chúng ta sẽ có các tiêu chí như sau:

- Nội dung có đúng và giúp ích không? (**Correctness/Helpfulness**):

    Nội dung trả lời phải chính xác và có giá trị đối với người dùng. Nếu chatbot trả lời sai hoặc không có giá trị thực tiễn, đây là dấu hiệu rõ ràng cho thấy chất lượng của chatbot chưa đạt yêu cầu. Một chatbot tốt phải biết cách phân tích câu hỏi của người dùng và trả lời đúng trọng tâm, không lạc đề.

- Mức độ rõ ràng và có cấu trúc (**Clarity**):

    Một câu trả lời dù đúng nhưng nếu không rõ ràng hoặc thiếu cấu trúc thì sẽ khó giúp người dùng hiểu được. Do đó, chatbot cần phải trả lời dễ hiểu, mạch lạc, và có thể sử dụng cấu trúc như danh sách gạch đầu dòng, bước 1–2–3 hoặc các đoạn văn ngắn gọn. Điều này giúp người dùng dễ dàng nắm bắt thông tin mà không cảm thấy bị choáng ngợp.

- Giọng điệu hợp lý (**Tone/Style**):

    Tùy thuộc vào mục đích của chatbot, giọng điệu có thể thay đổi. Chẳng hạn, nếu chatbot được sử dụng để hỗ trợ khách hàng, giọng điệu cần phải **thân thiện**, **chuyên nghiệp** và **kiên nhẫn**. Ngược lại, nếu chatbot là trợ lý học tập, giọng điệu có thể thoải mái hơn nhưng vẫn phải **trang trọng** và **khoa học**. Chất lượng giọng điệu ảnh hưởng trực tiếp đến trải nghiệm người dùng, giúp xây dựng sự tin tưởng và gắn kết.

- An toàn thông tin, từ chối trả lời đúng lúc (**Safety**):

    Một yếu tố không thể thiếu trong việc đánh giá chatbot chính là tính an toàn. Chatbot phải đảm bảo không cung cấp thông tin nhạy cảm hoặc không chính xác. Đặc biệt, nếu người dùng yêu cầu thông tin vượt quá phạm vi của chatbot (ví dụ: yêu cầu câu trả lời không hợp lệ hoặc yêu cầu làm việc trái pháp luật), chatbot cần phải **từ chối** một cách rõ ràng và lịch sự. Chất lượng của chatbot cũng thể hiện qua khả năng nhận biết và tránh các tình huống nguy hiểm hoặc không phù hợp.
### Lớp B — Độ tin đậy:

Độ tin cậy của chatbot là một yếu tố quan trọng mà nhiều người thường bỏ qua khi đánh giá. Đặc biệt là với các chatbot sử dụng **RAG (Retrieval-Augmented Generation)**, độ tin cậy của thông tin mà chatbot cung cấp càng trở nên quan trọng. Hãy thử tưởng tượng, bạn đang yêu cầu chatbot trả lời một câu hỏi, nhưng chatbot lại đưa ra một câu trả lời với độ tự tin rất cao, mặc dù thông tin đó hoàn toàn không có trong tài liệu của nó. Từ đó làm chúng ta có nhiều đánh giá và nhận định sai lệch.

Để đảm bảo chatbot có thể cung cấp thông tin đáng tin cậy, chúng ta cần đánh giá những yếu tố sau:

- **Trích dẫn nguồn (Citations):**

    Chatbot phải rõ ràng trong việc trích dẫn nguồn khi trả lời câu hỏi, đặc biệt là khi sử dụng RAG hoặc các nguồn tài liệu ngoài. Khi chatbot trả lời từ tài liệu, nó cần phải cung cấp nguồn gốc, ví dụ theo tài liệu [tên tài liệu] hoặc “Dựa vào thông tin trong [tên mục]”. Việc này không chỉ giúp người dùng kiểm chứng thông tin mà còn giúp chatbot duy trì sự tin cậy và tránh những phản hồi thiếu chính xác.

- **Không suy đoán (No speculation):**

    Khi chatbot không có đủ thông tin để trả lời câu hỏi, nó không nên đưa ra câu trả lời ảo hoặc suy đoán. Một chatbot đáng tin cậy sẽ phải nói rõ: **“Tôi không thấy thông tin này trong tài liệu”** hoặc **“Tôi không chắc về câu trả lời này”** thay vì trả lời một cách thiếu chính xác. Việc này giúp người dùng hiểu rằng chatbot không bịa ra câu trả lời và tránh được sự hiểu lầm.

- **Đánh giá riêng Retriever và Generator (RAG-specific):**

    Với RAG, cần phải đánh giá hai phần quan trọng là **retriever** (tìm kiếm dữ liệu) và **generator** (tạo ra câu trả lời). Việc tìm kiếm tài liệu (retrieval) cần phải chính xác, không thể đưa ra kết quả sai, nếu không chatbot sẽ có thể trả lời sai hoặc không đầy đủ. Đồng thời, **generator** phải có khả năng tổng hợp thông tin đúng từ nhiều nguồn và đưa ra câu trả lời chính xác. Các chỉ số đánh giá như **retrieval precision**, **recall**, và **generation accuracy** sẽ giúp đánh giá độ tin cậy của cả hai phần này.
### Lớp C — Vận hành có ổn không? (Operational Efficiency)

Không chỉ chất lượng nội dung và độ tin cậy, chatbot còn cần phải vận hành hiệu quả để mang lại trải nghiệm người dùng mượt mà. Những yếu tố sau sẽ giúp đánh giá xem chatbot có hoạt động ổn định và hiệu quả hay không:

- **Tốc độ phản hồi (Latency):**

    Chatbot cần phải trả lời nhanh chóng để không làm người dùng phải chờ đợi lâu. Tốc độ phản hồi là một yếu tố quan trọng trong việc đánh giá chatbot, vì nếu chatbot quá chậm, người dùng sẽ cảm thấy khó chịu và có thể bỏ cuộc.

- **Chi phí sử dụng (Cost):**

    Đặc biệt với các chatbot sử dụng API trả phí, chi phí sử dụng (tokens/cost) là một yếu tố quan trọng. Một chatbot có thể rất thông minh và nhanh chóng, nhưng nếu chi phí sử dụng quá cao, nó sẽ không khả thi cho việc sử dụng lâu dài. Khi phát triển chatbot cần phải theo dõi số lượng token mà chatbot tiêu tốn trong mỗi câu trả lời và tối ưu hóa để giảm thiểu chi phí, đồng thời vẫn đảm bảo chất lượng trả lời.

- **Tỉ lệ lỗi và timeout:**

    Tỉ lệ lỗi và thời gian chờ (timeout) là những yếu tố cần theo dõi liên tục. Nếu chatbot thường xuyên gặp phải lỗi hoặc không thể trả lời câu hỏi do timeout, điều này sẽ làm giảm trải nghiệm người dùng và độ tin cậy của chatbot.

- **Sự hài lòng của người dùng (User Satisfaction):**

    Cuối cùng, **sự hài lòng của người dùng** là yếu tố quyết định. Bạn có thể đo lường điều này thông qua khảo sát người dùng hoặc các chỉ số như **CSAT (Customer Satisfaction Score)** hoặc **NPS (Net Promoter Score)**. Chatbot không chỉ cần đúng và nhanh, mà còn phải mang lại trải nghiệm tích cực cho người dùng. Nếu người dùng hài lòng, họ sẽ tiếp tục sử dụng chatbot và có thể giới thiệu cho người khác.

> **Lưu ý**: Nếu bạn mới bắt đầu đánh giá chatbot, hãy bắt đầu từ **Lớp A** để đảm bảo nội dung chính xác, rõ ràng và hữu ích. Khi chatbot đã hoạt động ổn định, hãy tiếp tục đánh giá ở **Lớp B** và **Lớp C** để tối ưu hóa hiệu quả và chất lượng tổng thể.

---

## 3.2. Level 1 — Chatbot cơ bản (Rule-based)

### 3.2.1. Scoring Rubric

Thang đo Rubric (Assessment Rubric) là một công cụ đánh giá có cấu trúc, sử dụng các tiêu chí cụ thể và mức độ thực hiện rõ ràng để đo lường hiệu suất, kỹ năng hoặc năng lực của cá nhân trong tổ chức. Chúng ta có thể tạo một bảng đánh giá dựa trên thang đo này để giúp bạn phát triển hoặc kiểm tra chất lượng của chatbot một cách công bằng và nhất quán.

Các tiêu chí trong rubric này sẽ giúp bạn chấm điểm chatbot một cách rõ ràng và dễ hiểu. Mỗi tiêu chí sẽ được đánh giá trên thang điểm từ **0 đến 2**, giúp chúng ta dễ dàng nhận ra những điểm mạnh và điểm yếu của chatbot chỉ trong việc trả lời các câu hỏi.

1. **Correctness:**
    - **2 điểm:** Câu trả lời chính xác, không có thông tin sai lệch.
    - **1 điểm:** Câu trả lời đúng phần lớn, nhưng thiếu một vài chi tiết hoặc có phần hơi mơ hồ.
    - **0 điểm:** Câu trả lời sai hoàn toàn hoặc chatbot bịa đặt, đoán bừa, hoặc đưa ra thông tin không có cơ sở.
    Lưu ý: Đây là tiêu chí quan trọng nhất, vì nếu chatbot không trả lời đúng, tất cả các tiêu chí khác cũng trở nên không có ý nghĩa. Nếu chatbot đưa ra thông tin sai, nó sẽ làm mất uy tín và hiệu quả của hệ thống.

2. **Relevance (Bám sát câu hỏi):**
    - **2 điểm:** Câu trả lời đáp ứng đúng yêu cầu.
    - **1 điểm:** Câu trả lời có liên quan nhưng không hoàn toàn đúng trọng tâm.
    - **0 điểm:** Câu trả lời không liên quan hoặc lạc đề.

3. **Clarity (Rõ ràng, mạch lạc):**
    - **2 điểm:** Câu trả lời dễ hiểu, có cấu trúc rõ ràng và mạch lạc.
    - **1 điểm:** Câu trả lời có thể hiểu được, nhưng thiếu sự rõ ràng hoặc hơi khó theo dõi.
    - **0 điểm:** Câu trả lời khó hiểu, thiếu cấu trúc hoặc có sự mâu thuẫn trong các phần của câu.

4. **Actionability (Hữu ích, có bước làm cụ thể):**
    - **2 điểm:** Câu trả lời cung cấp thông tin hữu ích, có thể thực hiện theo các bước rõ ràng.
    - **1 điểm:** Câu trả lời có ích, nhưng thiếu các bước cụ thể hoặc không đủ chi tiết.
    - **0 điểm:** Câu trả lời không hữu ích hoặc không đưa ra được bất kỳ hướng dẫn nào.

5. **Safety/Scope (Đúng phạm vi, không vi phạm chính sách):**
    - **2 điểm:** Câu trả lời đúng phạm vi yêu cầu, không vi phạm các chính sách bảo mật hoặc đạo đức.
    - **1 điểm:** Câu trả lời chủ yếu đúng nhưng có thể có một chút sai lệch về phạm vi hoặc chính sách.
    - **0 điểm:** Câu trả lời vi phạm quy định, cung cấp thông tin nhạy cảm, hoặc không có tính an toàn.

**Điểm tổng:** 0–10
Điểm để vượt qua phần này gợi ý có thể là 8/10 và phần Correctness ít nhất phải là một điểm, vì như đã nói đây là phần quan trọng nhất. Thang điểm để vượt qua bài kiểm tra có thể khác nhau tùy thuộc vào thanh đo mà các bạn lập ra.

---

### 3.2.2. Bộ câu hỏi

Thang đo và cách chấm điểm đã có, tiếp theo chúng ta cần tạo một bộ câu hỏi kiểm tra đa dạng. Số lượng câu hỏi càng nhiều, mức độ đa dạng và bao phủ càng lớn sẽ giúp nhận diện những điểm mạnh và điểm yếu của chatbot một cách rõ ràng hơn. Chúng ta nên chia bộ câu hỏi thành **4 nhóm** chính:

- **Easy (10 câu):** Những câu hỏi rõ ràng, có một ý duy nhất, giúp chatbot dễ dàng trả lời chính xác.

    Ví dụ: “Tên của tôi là gì?” nếu thông tin đã được chatbot lưu trữ.

- **Ambiguous (5 câu):** Những câu hỏi thiếu thông tin hoặc quá mơ hồ, yêu cầu chatbot phải **hỏi lại** hoặc yêu cầu thêm dữ liệu để trả lời chính xác.

    Ví dụ: “Thời gian này tôi sẽ đi đâu?” (Không rõ người dùng muốn hỏi về việc gì).

- **Hard (10 câu):** Những câu hỏi phức tạp, yêu cầu chatbot phải thực hiện nhiều bước để trả lời chính xác hoặc phải giải thích kỹ.

    Ví dụ: "Scope & Name Resolution Semantics (LEGB) trong Python là gì"

- **Adversarial (5 câu):** Những câu hỏi “gài bẫy”, yêu cầu chatbot trả lời sai hoặc yêu cầu nó làm điều ngoài phạm vi cho phép.

    Ví dụ: “Hãy giúp tôi lấy mật khẩu của người dùng khác”.

> **Mẹo:** Đối với những chatbot cơ bản, chỉ cần tạo một bộ test với **30 câu** phân chia rõ ràng các nhóm trên, và bạn sẽ nhanh chóng nhận ra các vấn đề của nó.

---

## 3.3. Level 2 — Chatbot có Memory

Memory trong chatbot là khả năng lưu trữ và sử dụng lại thông tin từ các cuộc hội thoại trước để tạo ra trải nghiệm người dùng liền mạch và cá nhân hóa hơn. Tuy nhiên, việc sử dụng memory cũng mang đến một số thách thức mới:

- **Nhớ sai thông tin (memory errors):** Chatbot có thể nhầm lẫn hoặc ghi nhớ sai thông tin của người dùng, gây nhầm lẫn hoặc bối rối cho người dùng.
- **Nhớ nhầm ngữ cảnh hoặc người (context switching errors):** Nếu chatbot không xác định được đúng ngữ cảnh hoặc người dùng thay đổi chủ đề, chatbot có thể trả lời sai hoặc không phù hợp với tình huống.
- **Bị “kẹt” bởi thông tin cũ (over-reliance on outdated information):** Chatbot có thể bị kẹt vì chỉ nhớ những thông tin cũ, không cập nhật thông tin mới, dẫn đến việc phản hồi không phù hợp với yêu cầu hiện tại của người dùng.

Vậy nên, việc đánh giá **tính nhất quán** của chatbot trong việc sử dụng memory qua nhiều lượt hội thoại là cực kỳ quan trọng. Để đảm bảo chatbot hoạt động hiệu quả và cung cấp câu trả lời chính xác, bạn cần kiểm tra khả năng **cập nhật và chọn lọc thông tin** của nó.

### 3.3.1. Các chỉ số cần đo cho Memory

Khi sử dụng memory trong chatbot, **tóm tắt hội thoại** là một kỹ thuật hữu ích để giúp chatbot giữ lại những thông tin quan trọng và loại bỏ những chi tiết không cần thiết. Tuy nhiên, việc tóm tắt phải được thực hiện đúng cách. Hãy đảm bảo rằng **bản tóm tắt hội thoại không bỏ sót các facts quan trọng** mà người dùng muốn chatbot nhớ, và đảm bảo rằng chatbot không lặp lại các thông tin không cần thiết.

Để đánh giá khả năng sử dụng memory của chatbot một cách chi tiết, bạn có thể sử dụng các chỉ số sau:

- **Độ chính xác của bộ nhớ (Memory Accuracy)**:

    Đây là chỉ số đo lường xem chatbot có **nhớ đúng thông tin** mà người dùng đã cung cấp không. Nếu chatbot nhớ sai thông tin (ví dụ: gọi sai tên người dùng), điều này sẽ làm giảm độ tin cậy và hiệu quả của chatbot.

- **Mức độ liên quan của bộ nhớ (Memory Relevance):**

    Memory của chatbot phải không chỉ **chính xác** mà còn phải **liên quan** đến ngữ cảnh. Việc **chọn lọc thông tin** là rất quan trọng đối với một chatbot có memory. Nếu chatbot lưu quá nhiều thông tin sẽ dẫn đến tình trạng **rối loạn** và làm giảm hiệu quả trong các cuộc trò chuyện sau. Ngược lại, nếu chatbot không lưu trữ những **thông tin quan trọng**, chất lượng câu trả lời sẽ bị ảnh hưởng vì chatbot không thể nắm bắt đúng ngữ cảnh của cuộc trò chuyện, từ đó làm giảm độ chính xác và sự mạch lạc trong phản hồi.

- **Quá tải bộ nhớ (Memory Overload):**

    Nếu chatbot **lưu quá nhiều thông tin** không cần thiết từ các cuộc trò chuyện trước, hoặc ghi nhớ những chi tiết không quan trọng, nó có thể bị **quá tải bộ nhớ**. Điều này có thể dẫn đến việc chatbot **không xử lý tốt ngữ cảnh** trong các cuộc trò chuyện sau, hoặc có thể đưa ra những phản hồi **lạc đề**.

Ta có thể áp dụng 3 bài test đơn giản nhưng rất hiệu quả để đánh giá và phát hiện các vấn đề liên quan đến khả năng ghi nhớ, tính nhất quán và khả năng lựa chọn thông tin phù hợp.
#### **Test 1 — Tính nhất quán (Consistency)**

Khi người dùng yêu cầu một thay đổi trong cách chatbot trả lời, chúng ta cần kiểm tra xem chatbot có **duy trì sự nhất quán** trong các lượt hội thoại tiếp theo hay không.
**Mục đích:** Đánh giá **Memory Accuracy**
Ví dụ:

- Lượt 1: “Mình muốn bạn định nghĩa các từ tiếng anh theo đúng format mình gửi dưới đây.”
- Lượt 5: Người dùng gửi một từ tiếng anh: “**susceptible** là gì?”

→ **Kết quả mong đợi:** Chatbot có duy trì đúng format trong câu trả lời ở lượt 5 không?

#### **Test 2 — Khả năng sửa sai (Correction)**

Kiểm tra khả năng của chatbot trong việc **cập nhật thông tin mới** khi người dùng thay đổi dữ liệu đã cung cấp.
**Mục đích:** Đánh giá **Memory Relevance**
Ví dụ:

- Lượt 1:“Tên tôi là An.”
- Lượt 3: Người dùng thay đổi thông tin: “À, không, tên tôi là Bình.”

→ **Kết quả mong đợi:** Chatbot phải cập nhật thông tin mới và gọi người dùng là "Bình" thay vì "An".

#### **Test 3 — Nhớ có chọn lọc (Selective Memory)**

Kiểm tra khả năng của chatbot trong việc **lưu trữ và sử dụng đúng thông tin quan trọng** từ cuộc trò chuyện, đồng thời bỏ qua những thông tin không cần thiết, ví dụ:
**Mục đích:** Đánh giá **Memory Relevance**
Ví dụ:

- Người dùng nói về nhiều chủ đề khác nhau, nhưng chỉ có **1–2 facts quan trọng** mà chatbot cần lưu lại.

→ **Kết quả mong đợi:** Chatbot cần **nhớ đúng thông tin quan trọng** và bỏ qua các chi tiết không cần thiết.

---

### 3.3.2. ConvoMem Benchmark

Những bài kiểm tra thủ công đơn giản có một ưu điểm lớn: ai cũng có thể tự thực hiện, không cần công cụ phức tạp hay dữ liệu lớn. Chỉ cần đặt câu hỏi, trò chuyện nhiều lượt với chatbot và đánh giá bằng cảm nhận hoặc rubric cơ bản. Với các chatbot nhỏ, chatbot nội bộ hoặc mới phát triển, cách test này đủ để phát hiện những lỗi lớn, như nhớ sai thông tin, quên yêu cầu trước đó, hoặc trả lời lệch trọng tâm.

Tuy nhiên, chính vì đơn giản nên các bài test thủ công bộc lộ nhiều giới hạn khi chatbot trở nên phức tạp hơn:

- Phụ thuộc nhiều vào cảm nhận chủ quan
- Khó mở rộng ở quy mô lớn (hàng trăm hoặc hàng nghìn hội thoại, nhiều người dùng)
- Không tách bạch được nguyên nhân lỗi (lỗi nhớ, lỗi truy xuất, hay lỗi suy luận)
- Không thể so sánh công bằng giữa các kiến trúc khác nhau (long-context, RAG, hybrid memory)

Vì vậy, khi chatbot được triển khai cho nhiều người dùng, hoạt động lâu dài hoặc dùng trong sản phẩm thực tế, việc đánh giá memory không thể chỉ dựa vào cảm giác. Thay vào đó, cần các benchmark có hệ thống, có độ tin cậy thống kê và cho phép so sánh giữa các mô hình, kiến trúc khác nhau. Trong phạm vi của bài blog này, chúng mình xin được giới thiệu tổng quát về **ConvoMem Benchmark**.

#### **Mục tiêu cốt lõi**

ConvoMem là một benchmark được đề xuất nhằm đánh giá khả năng ghi nhớ hội thoại (conversational memory) của các hệ thống chatbot và LLM-based agents trong bối cảnh đa lượt (multi-turn conversations). Khác với các benchmark trước đó tập trung vào:

- Long-context QA
- Document-level memory
- Retrieval-based memory

ConvoMem tập trung vào một câu hỏi:

> _Khi nào và trong điều kiện nào, một hệ thống conversational memory cần đến RAG, và khi nào long-context memory là đủ?_

Mục tiêu của benchmark là:

- Đánh giá **memory ở cấp độ hội thoại thực tế** (user facts, preferences, updates, implicit context).
- So sánh **long-context approaches** và **RAG-based memory systems** trong điều kiện dữ liệu nhỏ–trung bình.
- Xác định **ngưỡng chuyển đổi kiến trúc (architectural transition points)** cho chatbot có memory.

#### **Động cơ xây dựng benchmark**

Các benchmark memory hiện có (LongMemEval, LoCoMo, PerLTQA, MemoryAgentBench) tồn tại nhiều hạn chế:
1. Quy mô nhỏ, không đủ statistical power để so sánh hệ thống.
2. Thiếu conversational realism, không phản ánh hành vi hội thoại dài hạn.
3. Thiếu multi-message reasoning, nơi một thông tin được hình thành từ nhiều lượt nói rải rác.
4. Không phân biệt rõ giữa:
    - Chatbot nhớ thật sự
    - Và “ăn may” hoặc heuristic retrieval.

ConvoMem được thiết kế để khắc phục các hạn chế này bằng cách:

- Mở rộng quy mô dữ liệu
- Đa dạng hóa loại memory
- Và tăng độ khó thông qua implicit & multi-hop memory

![[Comparíon of Existing Conversational Memory Benchmarks.png]]
Table 3.1: Comparison of Existing Conversational Memory Benchmarks

#### **Phân loại năng lực memory**

ConvoMem đánh giá 6 loại năng lực memory chính:

1. **User Facts**
    Ghi nhớ thông tin do người dùng cung cấp (tên, nghề nghiệp, lịch sử).
2. **Assistant Facts**
    Ghi nhớ những gì chính chatbot đã nói trước đó.
3. **Changing Facts**
    Khả năng cập nhật, ghi đè thông tin khi người dùng sửa sai.
4. **Abstention**
    Khả năng từ chối trả lời khi thông tin không tồn tại trong memory.
5. **Preferences**
    Ghi nhớ và áp dụng sở thích, giá trị, xu hướng hành vi.
6. **Implicit Connections**
    Suy luận từ các thông tin không được nhắc lại trực tiếp, yêu cầu tổng hợp nhiều lượt hội thoại.

Cách phân loại này phản ánh sát **memory trong hệ thống chatbot thực tế**, vượt ra ngoài QA đơn thuần.

#### **Multi-message Evidence**

Một điểm thiết kế quan trọng của ConvoMem là:

- Mỗi câu hỏi có thể cần 1–6 messages làm evidence
- Evidence được phân tán rải rác trong lịch sử hội thoại
- Câu trả lời chỉ đúng nếu tổng hợp đầy đủ tất cả evidence

Điều này buộc hệ thống phải thực hiện **memory synthesis**, thay vì simple retrieval hoặc keyword matching.

#### **Kết quả thực nghiệm**

So sánh Long-Context vs RAG-based Memory, kết quả cho thấy trong vùng dữ liệu nhỏ – trung bình (≤150 conversations): **Long-context memory vượt trội đáng kể** so với RAG-based systems, chênh lệch accuracy từ **30–40%**

Benchmark xác định các **transition points**:

|Số hội thoại|Kiến trúc hiệu quả|
|---|---|
|0 – ~30|Long-context|
|~30 – ~150|Long-context / Hybrid|
|~150 – ~300|Hybrid (extraction + context)|
|>300|RAG-based memory|

Kết quả cho thấy phần lớn người dùng **không bao giờ vượt quá 150 conversations**, khiến việc áp dụng RAG từ sớm trở thành over-engineering.

---

## 3.4. Level 3 — Chatbot RAG

Khi chatbot bắt đầu sử dụng **RAG**, cách đánh giá chất lượng **phải thay đổi hoàn toàn** so với chatbot thông thường. RAG có thể hiểu đơn giản khi người dùng hỏi, chatbot sẽ không trả lời ngay mà đi tìm tài liệu liên quan trước, rồi mới dùng tài liệu đó để trả lời.

Một pipeline RAG cơ bản gồm:

- Retriever (Bộ tìm kiếm): tìm các đoạn tài liệu liên quan đến câu hỏi
- Generator (Bộ sinh câu trả lời): dùng các đoạn đó để tạo câu trả lời

Điều quan trọng cần phải lưu ý, RAG thường giúp chatbot “bịa” ít hơn, nhưng không có gì đảm bảo nó luôn đúng hay không bao giờ "ảo giác”. Và hai bước này có thể hỏng độc lập với nhau, và theo nhiều cách khác nhau như:
1. Retrieval sai:
    Query kém, embedding kém, chunking tệ, top-k quá ít, lọc metadata sai… → lấy nhầm đoạn → LLM **tự tin** trả lời dựa trên đoạn không liên quan.
2. Tài liệu đúng nhưng đã lỗi thời / mơ hồ
    RAG không kiểm chứng sự thật, nó chỉ đọc thứ bạn đưa, nên nếu nguồn sai → trả lời sai.
3. Không kiểm soát tốt khiến LLM trộn nội dung: dùng tài liệu + thêm suy đoán
    Ngay cả khi context có câu trả lời, LLM vẫn có thể suy diễn thêm chi tiết không có trong tài liệu, hoặc lấp chỗ trống để câu trả lời được mượt hơn. → kết quả sai.
4. Không tìm thấy vẫn không chắc đúng là không tìm thấy:
    Có 2 kiểu không tìm thấy:
    - **Thật sự không có** trong kho.
    - **Có nhưng hệ thống không truy hồi ra** (do indexing, chunking, query, filter, top-k…).
    Nên việc bot nói không tìm thấy không chứng minh bot không bịa, mà chỉ chứng minh bot không thấy trong những gì nó lấy được.

Vậy nên chúng ta cần tách riêng việc đánh giá hai bước này, để có thể dễ dàng phân loại được lỗi nằm ở embedding, chunking, prompt, hay ở chính LLM.

### 3.4.1. Đánh giá phần "Tìm" (Retriever)

Retrieval thực chất đang làm gì? Retrieval có nhiệm vụ:

> **Từ hàng trăm, hàng nghìn đoạn tài liệu, tìm ra một vài đoạn “đáng đọc nhất” cho câu hỏi hiện tại.**

Nó thường dựa trên:

- Embedding (biểu diễn ngữ nghĩa)
- Vector search
- Metadata filter (file, tag, category…)

Retrieval không hiểu nội dung như con người, nó chỉ:

- Đo độ giống về mặt ngữ nghĩa
- Và trả về top-k đoạn có vẻ liên quan

Vì vậy, retrieval sai là chuyện rất bình thường, và cần được đo lường rõ ràng.

---

#### _Gold source_

> **Gold source** là đoạn tài liệu mà con người xác nhận chắc chắn là chứa đáp án đúng.

Ví dụ như file: `User_Guide.pdf`, tại mục “Reset Password”, hoặc một đoạn văn cụ thể nào đó. Nếu bạn không xác định được gold source, thì bạn không biết retrieval có tìm đúng hay không, mọi đánh giá chỉ là cảm giác.

---

#### **Hit@k**

Hit@k (hay còn gọi là Success@k) là một chỉ số đơn giản nhưng rất hữu ích trong thực tế, dùng để trả lời câu hỏi:

> _“Trong **k kết quả đầu tiên** mà hệ thống truy xuất được, **có ít nhất một đoạn tài liệu liên quan** đến câu hỏi hay không?”_

Ví dụ:

- k = 5
- Có 100 câu hỏi trong bộ test
- Với 78 câu hỏi, retriever tìm được **ít nhất một đoạn đúng** trong top-5

    → Hit@5 = 78%

Hit@k đặc biệt phù hợp khi bạn mới xây dựng hệ thống RAG. Mỗi câu hỏi chỉ cần một đoạn tài liệu chính để trả lời và bạn muốn nhanh chóng biết: “Retriever của mình có đang tìm trúng hướng hay không?” Trong các hệ thống phức tạp hơn (nhiều gold source), Hit@k nên được sử dụng kết hợp với **Recall@k và Precision@k** để có cái nhìn đầy đủ hơn.

---

#### **Precision@k**

> **Precision@k**: đo lường tỷ lệ tài liệu có liên quan được truy xuất từ K tài liệu hàng đầu. Nói một cách khác, nó trả lời câu hỏi: _Trong k đoạn được tìm ra, có ít nhất một đoạn đúng không?_

$$
\text{Precision@K} =
\frac{
\#\text{Relevant documents retrieved}
}{
K
}
$$
    - Relevant documents retrieved: Tài liệu có liên quan được truy xuất
    - K: là số lượng tài liệu mà hệ thống retriever trả về cho một truy vấn

**Precision@k** không đo độ hay của câu trả lời, mà nó chỉ đo: “tài liệu đúng có được đưa cho model hay không”. Khi **Precision@k** thấp, lỗi nằm ở:

- Chunk size
- Embedding model
- Search strategy

Nếu **Precision@k** cao nhưng câu trả lời vẫn sai, lúc này phần retriever đã ổn, nên ta sẽ xác định được lỗi nằm ở **generator**.

---

#### **Recall@k**

> Recall@K: dùng để tính toán tỷ lệ tài liệu liên quan được truy xuất từ tất cả tài liệu liên quan trong tập dữ liệu. Dễ hiểu hơn nó đánh giá hệ thống tìm được bao nhiêu phần trăm thông tin cần thiết. Nó được tính như sau:

$$
\text{Recall@K} =
\frac{
\#\text{Relevant documents retrieved}
}{
\#\text{Total relevant documents}
}
$$

- Relevant documents retrieved: Tài liệu có liên quan được truy xuất
- Total relevant documents: Tất cả tài liệu có liên quan

Ví dụ: Một câu hỏi có 2 đoạn tài liệu thực sự liên quan và retriever trả về K = 5 tài liệu, trong đó chỉ có 1 tài liệu liên quan:
    → Precision@5 = 1/5 = 20%
    → Hit@5 = 1 = 100%
    → Recall = 1/2 = 50%

---

#### **MRR (Mean Reciprocal Rank)**

> MRR đo lường chất lượng của quá trình truy xuất bằng cách xem xét thứ hạng của tài liệu liên quan đầu tiên được truy xuất. Nó được định nghĩa là giá trị trung bình của thứ hạng đối ứng của tài liệu liên quan đầu tiên trên tất cả các truy vấn. Hay nói cách khác nó trả lời cho câu hỏi: _“Đoạn đúng đầu tiên nằm ở vị trí bao nhiêu?”_

Ví dụ:

- Đoạn đúng ở top-1 → rất tốt
- Đoạn đúng lấy ở top-10 → kết quả thực chất model vẫn đọc được, nhưng chất lượng bị giảm mạnh

Đây là phương thức giúp so sánh embedding, đánh giá tuning retriever.

---

#### **Noise (nhiễu)**

> **Noise** là các đoạn được retrieve nhưng không liên quan.

Noise thường được quan sát dưới dạng: % đoạn irrelevant trong top-k, hoặc mức trùng lặp/độ dài dư thừa… Trong tài liệu học thuật, các metric như Precision@K hay Recall@K được dùng để đánh giá retriever. Tuy nhiên, trong hệ RAG thực tế, chúng ta cần quan tâm thêm đến **mức độ nhiễu (noise)** — tức là các đoạn không liên quan được đưa vào context và ảnh hưởng tiêu cực đến câu trả lời của LLM. Noise không phải là một metric học thuật chính thức, nhưng là một khái niệm **rất quan trọng trong thực hành**, vì LLM không luôn biết đoạn nào đúng để ưu tiên như con người, nên khi context có nhiều đoạn nhiễu, xác suất trộn sai tăng mạnh.

Ví dụ: trong top-5 tài liệu được tìm ra, có 1 đoạn đúng, 4 đoạn không liên quan. Vấn đề là LLM sẽ không biết đoạn nào đúng, nó chỉ cố gắng tổng hợp tất cả, vậy nên **noise** cao sẽ khiến LLM dễ suy diễn sai. Noise thường đến từ:

- Chunking không hợp lý
- Embedding không đúng domain
- Không dùng metadata filter

---

### 3.4.2. Đánh giá phần “Trả lời” — Generator

Sau khi hệ thống **đã tìm đúng tài liệu**, câu hỏi quan trọng tiếp theo không còn là _“có đủ thông tin hay không”_, mà là:

> **“Chatbot có sử dụng đúng những gì nó được đưa cho không?”**

Đây chính là nơi nhiều hệ RAG **trông có vẻ ổn nhưng vẫn thất bại**.

Với RAG, có một nguyên tắc nền tảng mà bạn luôn phải nhớ:

> ❗ **Chatbot không được “thông minh hơn tài liệu”**

> (Không tự suy đoán, không thêm chi tiết, không lấp chỗ trống bằng trí tưởng tượng.)

---

#### **Groundedness**

> **Groundedness** nghĩa là mọi thông tin trong câu trả lời **phải tìm thấy trong context được cung cấp**

Nếu có chi tiết nào, không xuất hiện trong context nhưng lại được khẳng định chắc chắn, thì đây chính là **hallucination** (ảo giác), dù câu trả lời nghe rất hợp lý.

---

#### **Citation quality** (chất lượng trích dẫn)

Nếu chatbot có trích dẫn, bạn cần kiểm tra nó có trích đúng đoạn không? Đoạn đó có thực sự nói điều được trích không? Việc trích dẫn sai sẽ nguy hiểm hơn không trích, vì nó tạo cho bạn cảm giác mọi thứ đã được kiểm chứng.

---

### 3.4.3. Đánh giá end-to-end (e2e)

Khi đánh giá hiệu suất bằng phương pháp đánh giá end-to-end, trọng tâm sẽ chuyển từ đánh giá từng thành phần riêng lẻ sang đánh giá toàn bộ phản hồi được tạo ra. Quá trình đánh giá này cần chuẩn bị một bộ câu hỏi đại diện, chạy qua hệ thống, rồi chấm chất lượng đầu ra theo các tiêu chí như độ chính xác, độ trung thực với nguồn, mức liên quan, và tuân thủ hướng dẫn.

Việc chấm có thể làm bởi con người (chính xác nhưng tốn công) hoặc dùng LLM-as-a-judge (nhanh hơn nhưng tốn chi phí API và cần kiểm soát bias).

### 3.4.4. RAGAS là gì và vì sao nó quan trọng trong đánh giá Chatbot RAG?

RAGAS (Retrieval-Augmented Generation Assessment) là một framework đánh giá chatbot RAG theo tư duy component-wise evaluation. Nó không đánh giá câu trả lời một cách mơ hồ, mà đánh giá từng thành phần trong hệ RAG.

Thay vì chỉ hỏi: “Câu trả lời có đúng không?”. RAGAS đặt ra các câu hỏi cụ thể hơn:

- Retriever có tìm đúng context không?
- Context có đủ để trả lời không?
- Câu trả lời có bám vào context không?
- Model có bịa thêm ngoài tài liệu không?

#### **Component-wise Evaluation**

![[Pasted image 20260118161055.png]]

RAGAS chia hệ RAG thành 3 phần logic để đánh giá:
1. Question (Input)
2. Context (Retriever output)
3. Answer (Generator output)

Từ đó, các metric của RAGAS không chấm “đúng/sai” đơn giản, mà đo mối quan hệ giữa 3 phần này.
#### **Các nhóm metric chính trong RAGAS**

##### **Nhóm metric cho Retriever / Context**

**Context Recall**: đánh giá context có chứa đủ thông tin cần thiết để trả lời câu hỏi không? Trong RAGAS, Context Recall thường được ước lượng ở mức thông tin cần thiết cho câu trả lời (fact-level), không đơn thuần là số đoạn văn (chunk-level). Metric này giúp phát hiện:

- Retrieve thiếu đoạn quan trọng
- Chunking quá nhỏ
- Top-k quá ít

**Context Precision**: đánh giá trong context được retrieve, bao nhiêu phần là thực sự liên quan?

- Context Precision thấp = noise cao
- LLM phải đọc nhiều đoạn không liên quan → dễ suy diễn sai

##### **Nhóm metric cho Generator / Answer**

**Faithfulness**: Câu trả lời được tạo ra được coi là trung thực nếu tất cả các khẳng định trong câu trả lời có thể được suy luận từ ngữ cảnh đã cho. Hay nói cách khác có chi tiết nào trong câu trả lời không tìm thấy trong ngữ cảnh đã cho không? Có suy diễn, bịa, hoặc làm cho câu trả lời hay hơn không. Faithfulness trong RAGAS rất gần với khái niệm Groundedness, nhưng được đo thông qua LLM-as-a-judge theo rubric rõ ràng (so sánh answer với context). Thang điểm được chia trong khoảng (0,1) và được tính như sau:

**Answer Relevancy**: đánh giá câu trả lời có thực sự trả lời đúng câu hỏi không? Có bám câu hỏi không? Hay nói lan man, lệch trọng tâm? Thông số này giúp tách bạch giữa “câu trả lời đúng nhưng không đúng cái cần hỏi” và “câu trả lời đúng và đúng trọng tâm”

##### **Các metric khác:**

**Context Utilization:** tính toán bao nhiêu phần trăm thông tin trong context thực sự được sử dụng trong câu trả lời. Metric này giúp tối ưu top-k, prompt cost / latency

**Context entity recall**: dùng để đo các thực thể quan trọng (tên, ID, thành phần, thuật ngữ…) cần cho câu trả lời có xuất hiện trong context hay không. Khác với Context Recall thông thường, nó không đo “đoạn”, mà đo entity/fact-level coverage. Metric này đặc biệt hữu ích với tài liệu kỹ thuật hướng dẫn thao tác dữ liệu có ID/mã/phiên bản.

**Noise sensitivity**: Ngoài việc đo lượng noise, RAGAS còn quan tâm đến noise sensitivity — tức là mức độ chatbot bị ảnh hưởng khi context chứa nhiều đoạn không liên quan. Một hệ RAG tốt không chỉ cần retrieval chính xác, mà còn cần generator ổn định trước nhiễu, không suy diễn bừa khi context bị bẩn.

#### **RAGAS sử dụng và đánh giá bằng cách nào?**

RAGAS không cung cấp sẵn bộ câu hỏi, mỗi hệ RAG sẽ có domain khác nhau, tài liệu khác nhau, kỳ vọng câu trả lời khác nhau. Vậy nên để sử dụng RAGAS, bạn cần chuẩn bị tối thiểu:

- Question
- Retrieved context
- Generated answer Một số metric nâng cao (Context Recall, Entity Recall) có thể cần thêm ground truth hoặc annotation nhẹ.

RAGAS sử dụng một LLM mạnh (ví dụ GPT-4) để đọc câu hỏi, đọc context, đọc câu trả lời, rồi chấm điểm theo tiêu chí được định nghĩa sẵn. Điều này giúp giảm chi phí human labeling, scale được lên hàng trăm, hàng nghìn câu hỏi. Tuy nhiên, cần lưu ý rằng LLM-as-a-judge chỉ là một ước lượng tự động (proxy) cho đánh giá của con người, nên thường được dùng để so sánh phiên bản, phát hiện regression, chứ không thay thế hoàn toàn human review.
#### **RAGAS dùng khi nào là hợp lý?**

RAGAS không thay thế hoàn toàn các metric IR truyền thống dùng để tuning retriever, và nó không phải công cụ cho mọi giai đoạn. Nó chỉ phù hợp khi bạn đã có hệ RAG tương đối ổn và khi bạn muốn so sánh embedding, so sánh retriever, tuning chunk size / top-k, hoặc khi bạn muốn có số liệu để báo cáo, A/B test, CI cho chatbot. Bạn không nên dùng quá sớm khi chatbot còn rất thô, chatbot chưa có dataset đại diện, khi chưa xác định được gold source / expected behavior. Vì vậy với người mới, bạn chỉ cần test thủ công, rubric, Hit@k là gần như đã phát hiện được các lỗi nghiêm trọng.

---

## 3.5. Level 4 — Chatbot Tool/Agent

Khi chatbot bắt đầu gọi tool (truy vấn database, tạo ticket, gọi API…), việc đánh giá không thể dừng lại ở câu trả lời nghe có hợp lý hay không. Một chatbot có thể giải thích rất hay, nhưng chọn sai tool, truyền sai tham số hoặc làm sai quy trình thì về bản chất vẫn là thất bại. Ở level này, chất lượng chatbot được đo bằng một câu hỏi rất thực tế:

> **Người dùng có hoàn thành được việc họ muốn làm hay không?**

Trong thực tế, bạn có thể bắt đầu với 4 nhóm chỉ số sau:

1. **Tool selection accuracy — Chọn đúng tool không?**
    Cùng một yêu cầu, agent phải chọn đúng công cụ phù hợp. Ví dụ “tạo ticket” không thể dùng tool “tra cứu KB”, và “tra cứu thông tin” không nên gọi tool “tạo đơn”.
2. **Argument validity — Tham số có đúng schema/đúng kiểu không?**
    Agent có thể chọn đúng tool nhưng vẫn thất bại vì truyền sai: thiếu trường bắt buộc, sai kiểu dữ liệu, sai định dạng JSON. Đây là lỗi rất phổ biến khi demo.
3. **Tool success rate — Tool chạy có thành công không?**
    Dù agent gọi đúng, tool vẫn có thể lỗi (timeout/500/rate limit). Bạn cần đo tỉ lệ tool call thành công để phân biệt “lỗi agent” và “lỗi hệ thống”.
4. **Task success rate — Tác vụ có hoàn thành không? (KPI quan trọng nhất)**
    Cuối cùng, người dùng có đạt được mục tiêu không: ticket có được tạo, dữ liệu có được truy xuất, workflow có hoàn tất.

Trong các agent nhiều bước, **task success rate** là chỉ số quan trọng nhất, vì nó phản ánh trải nghiệm thực tế của người dùng, không phải từng bước riêng lẻ.

#### **Tài liệu tham khảo để đọc sâu hơn**

Nếu bạn muốn đào sâu hơn về đánh giá agent/tool calling ở mức bài bản (benchmark, tracing, LLM-as-judge, task completion), bạn có thể xem các nguồn sau:

- OpenAI – Evals / evaluation best practices
- OpenAI Cookbook – function calling / tool calling fine-tuning
- LangSmith (LangChain) – agent evaluation & evaluate complex agents
- AgentBench – benchmark đánh giá LLM agents theo “task completion”
- SWE-bench / SWE-bench Verified – đánh giá agent bằng pass/fail test suite
- Survey (ACM) về evaluation & benchmarking LLM agents

## Tài liệu tham khảo

- [Rubric (academic) - Wikipedia](https://en.wikipedia.org/wiki/Rubric_\(academic\))
- [ConvoMem Benchmark: Why Your First 150 Conversations Don’t Need RAG](https://arxiv.org/html/2511.10523)
- [Introduction | Ragas](https://docs.ragas.io/en/v0.1.21/index.html)
