## 6. Triển khai ứng dụng Web:

Sau khi hoàn tất quá trình huấn luyện mô hình phân loại ảnh **chó và mèo**, nhóm tiến hành triển khai mô hình lên ứng dụng web nhằm cho phép người dùng tương tác trực tiếp với mô hình thông qua giao diện trực quan.  
Phần xây dựng giao diện người dùng (UI) và triển khai ứng dụng web được thực hiện bằng thư viện **Gradio**. Toàn bộ mã nguồn, mô hình và giao diện được đóng gói và chạy trên hệ sinh thái **Hugging Face Spaces**, giúp ứng dụng có thể truy cập trực tuyến và sử dụng ngay mà không cần cấu hình máy chủ thủ công.

🔗 **Link ứng dụng web**:  
[Cats and Dogs Classifier – Hugging Face Space](https://huggingface.co/spaces/oriontk24/animals-classification-demo)

![Animals Classification Demo UI](/AIO-2026---Warm-01/Project-3/image/app.png)
_Hình 6.1: Giao diện ứng dụng web phân loại ảnh chó và mèo được triển khai trên Hugging Face Spaces._

## 6.1. Kiến trúc dự án:

```
project/
├── app.py                # Gradio UI + inference logic
├── final_model.keras     # Mô hình CNN đã huấn luyện
├── requirements.txt      # Danh sách thư viện
└── conq011-cats-vs-dogs-classification-using-cnn.ipynb     # File huấn luyện model
```

## 6.2. Quy trình xử lý và dự đoán:

Luồng hoạt động của ứng dụng được mô tả như sau:

1. Người dùng tải ảnh đầu vào (mèo hoặc chó) thông qua giao diện web
2. Ảnh sẽ được upload lên và được resize về kích thước chuẩn (mặc định 128×128) và chuẩn hóa giá trị pixel
3. Sau khi nhấn nút dự đoán trên ứng dụng thì ảnh sẽ được đưa vào mô hình suy luận
4. Hệ thống trả về xác suất dự đoán cho từng lớp:
   - CAT 🐱
   - DOG 🐶
5. Trong trường hợp độ tin cậy thấp hơn ngưỡng xác định, ảnh sẽ được gán nhãn **Unknown / Not a Pet**

**Link video demo ứng dụng**: [Cats and Dogs Classifier - Demo](https://drive.google.com/file/d/1s9i0Z5QHi0cxrMzn3MoHzVdI-zEVvfCl/view?usp=sharing)
