# Phân loại ảnh Chó và Mèo bằng Convolutional Neural Networks

## 1. Giới thiệu

Trong những năm gần đây, Computer Vision (CV) đã trở thành một trong những lĩnh vực phát triển mạnh mẽ nhất của AI. CV cho phép máy tính nhìn và hiểu được nôi dung trong hình ảnh và video, từ đó mở ra nhiều ứng dụng quan trọng trong đời sống thực tế như nhận dạng khuôn mặt, xe tự hành, giám sát an ninh, y tế và thương mại điện tử.

Một trong những bài toán cơ bản và quan trọng của CV là **Image Classification** – bài toán gán một nhãn cho mỗi hình ảnh đầu vào. Trong bài toán này, hệ thống cần học cách trích xuất các đặc trưng có ý nghĩa từ hình ảnh để đưa ra dự đoán chính xác về lớp mà hình ảnh đó thuộc về.

Trong project này, chúng tôi tập trung vào bài toán **phân loại ảnh chó và mèo (Dog vs Cat Classification)** – một bài toán kinh điển thường được sử dụng như một ví dụ nhập môn cho các mô hình học sâu xử lý ảnh. Mặc dù có cấu trúc bài toán đơn giản, dữ liệu hình ảnh trong thực tế vẫn chứa nhiều biến thiên phức tạp, đòi hỏi mô hình phải học được các đặc trưng không gian ở nhiều mức độ khác nhau.

Để giải quyết bài toán, chúng tôi sử dụng **Convolutional Neural Networks (CNN)** – một kiến trúc mạng nơ-ron được thiết kế đặc biệt cho dữ liệu dạng ảnh. CNN có khả năng tự động học các đặc trưng không gian như cạnh, góc, hoa văn và cấu trúc đối tượng, giúp mô hình đạt hiệu quả cao trong các bài toán thị giác máy tính.

Mục tiêu của project là xây dựng một mô hình CNN có khả năng phân loại chính xác hình ảnh đầu vào thành hai lớp: `dog` hoặc `cat`, đồng thời giúp người học hiểu rõ hơn quy trình xây dựng một hệ thống phân loại ảnh hoàn chỉnh.

## 2. Động lực

Mặc dù con người có thể dễ dàng phân biệt chó và mèo chỉ trong vài giây, nhưng đối với máy tính, đây lại là một nhiệm vụ không hề đơn giản. Hình ảnh trong thực tế có thể khác nhau rất nhiều về:

- Góc chụp  
- Điều kiện ánh sáng  
- Kích thước và độ phân giải  
- Tư thế của đối tượng  
- Bối cảnh nền phía sau  

Những yếu tố này khiến cho việc xây dựng các thuật toán phân loại ảnh dựa trên quy tắc (rule-based) trở nên không khả thi. Do đó, các mô hình học máy, đặc biệt là học sâu, đã trở thành lựa chọn tối ưu cho các bài toán xử lý ảnh.

Bài toán phân loại chó và mèo thường được sử dụng như một **benchmark** trong lĩnh vực CV vì những lý do sau:

- Bài toán có cấu trúc đơn giản, dễ hiểu  
- Dữ liệu phong phú và dễ tiếp cận  
- Đủ thách thức để thể hiện sức mạnh của CNN  
- Phù hợp cho người mới bắt đầu tiếp cận Deep Learning  

**Convolutional Neural Networks (CNN)** đã chứng minh hiệu quả vượt trội trong các bài toán phân loại ảnh nhờ khả năng:

- Tự động học đặc trưng từ dữ liệu thô  
- Giảm số lượng tham số so với mạng fully-connected  
- Bảo toàn thông tin không gian của ảnh  

Thông qua project này, chúng tôi mong muốn:

- Hiểu rõ cách CNN hoạt động trong bài toán phân loại ảnh  
- Thực hành quy trình xây dựng một mô hình học sâu từ dữ liệu đến huấn luyện và đánh giá  
- Tạo nền tảng cho các bài toán Computer Vision phức tạp hơn trong tương lai  

## 3. Mô hình bài toán

### 3.1 Input

Đầu vào của mô hình là một ảnh màu RGB, được biểu diễn dưới dạng tensor:

$$
x \in \mathbb{R}^{H \times W \times 3}
$$

trong đó:

- $H$ là chiều cao của ảnh  
- $W$ là chiều rộng của ảnh  
- 3 tương ứng với ba kênh màu RGB  

Trước khi đưa vào mô hình, các ảnh sẽ được tiền xử lý (resizing, normalization, …) để đảm bảo kích thước và định dạng phù hợp.

### 3.2 Output

Đầu ra của mô hình là một nhãn:

$$
y \in \{0, 1\}
$$

trong đó:

- 0 = cat  
- 1 = dog  

### 3.3 Mô hình học

Mục tiêu của bài toán là học một hàm ánh xạ:

$$
f: x \rightarrow y
$$

sao cho với một ảnh đầu vào chưa từng xuất hiện trong tập huấn luyện, mô hình vẫn có thể dự đoán đúng nhãn tương ứng.

Để thực hiện điều này, chúng tôi sử dụng **Convolutional Neural Network (CNN)** – một mô hình bao gồm các lớp tích chập (convolution), pooling và fully-connected nhằm trích xuất và tổng hợp các đặc trưng quan trọng từ ảnh.

### 3.4 Hàm mất mát

Mô hình sử dụng hàm mất mát **Categorical Crossentropy** kết hợp với lớp đầu ra có 2 node (Softmax). Cách tiếp cận này giúp mô hình đánh giá xác suất riêng biệt cho từng lớp, tạo tiền đề để mở rộng bài toán phân loại đa lớp trong tương lai.
