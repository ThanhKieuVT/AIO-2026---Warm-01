# 4. Tìm hiểu các thư viện:

Python cung cấp một hệ sinh thái các thư viện phục vụ cho việc **xử lý dữ liệu, phân tích và trực quan hóa**. Thư viện là tập hợp các hàm và đối tượng đã được xây sẵn. Bạn có thể sử dụng các thư viện này thay vì viết lại mọi thứ từ đầu.

Trong python, có 4 thư viện bắt buộc phải biết khi mới bước chân vào Machine Learning:

- NumPy
- Pandas
- Matplotlib/ Seaborn
- Scikit-learn
  Hãy hiểu **mỗi thư viện làm gì, dùng lúc nào**, không cần đào sâu lý thuyết ngay.

## 4.1. NumPy - Nền tảng xử lý số liệu:

### 4.1.1. NumPy là gì? Tại sao lại sử dụng NumPy trong Machine Learning?

NumPy giúp bạn thực hiện các **phép toán số học** trên dữ liệu. Với NumPy, bạn có thể **chuyển đổi nhiều dạng dữ liệu khác nhau về dạng số**.

Trong Machine Learning, dữ liệu đôi khi không ở dạng số, vì vậy NumPy đóng vai trò rất quan trọng trong việc xử lý và **biểu diễn toàn bộ dữ liệu nhận được dưới dạng số** để máy có thể học được.

### 4.1.2. Ví dụ minh họa với NumPy:

#### Ví dụ 1: Tạo mảng số

```python
import numpy as np

# Tạo mảng 1 chiều
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

#### Ví dụ 2: Nhân ma trận:

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = A @ B   # Nhân ma trận
print(C)
```

## 4.2. Pandas - Làm việc với dữ liệu dạng bảng:

### 4.2.1. Pandas và DataFrame là gì?

| id  | name | age | salary |
| --- | ---- | --- | ------ |
| 1   | An   | 22  | 500    |
| 2   | Bình | 35  | 1200   |
| 3   | Chi  | 28  | 800    |
| 4   | Dũng | 42  | 1500   |

Pandas là một công cụ **mã nguồn mở** dùng cho **phân tích và xử lý dữ liệu**. Với Pandas, bạn có thể làm việc với **DataFrame** – một cấu trúc dữ liệu dạng bảng, **tương tự như file Excel**, rất thuận tiện cho việc đọc, chỉnh sửa và phân tích dữ liệu.

Trong thực tế, dữ liệu thực tế thường **thiếu giá trị**, lẫn **dữ liệu sai**, **không đúng định dạng**. Do vậy, chung ta phải **làm sạch dữ liệu trước** khi train model.

| name | age      | salary |
| ---- | -------- | ------ |
| An   | 22       | 500    |
| Bình |          | 1200   |
| Chi  | 28       | ???    |
| Dũng | bốn mươi | 1500   |

### 4.2.2. Ví dụ minh họa với Pandas:

#### Ví dụ 1: Tạo một DataFrame giống Excel:

```python
import pandas as pd

data = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "age": [22, 35, 28, 42],
    "salary": [500, 1200, 800, 1500]
}

df = pd.DataFrame(data)
print(df)
```

Kết quả nhận được:

```
   name  age  salary
0   An   22     500
1  Bình  35    1200
2  Chi   28     800
3  Dũng  42    1500
```

#### Ví dụ 2: Thống kê nhanh trên DataFrame:

```python
df.describe()
```

Kết quả nhận được:

```t
       age    salary
mean   31.75  1000
min    22     500
max    42     1500
```

# 4.3. Matplotlib / Seaborn - Trực quan hóa dữ liệu:

### 4.3.1. Matplotlib và Seaborn là gì?

Matplotlib và Seaborn là 2 thư viện phổ biến nhất trong Python, chúng cho phép vẽ biểu đồ và đồ thị từ kết quả phân tích được. Nếu chúng ta chỉ hiểu dự liệu thông qua bảng số thì rất khó khăn, vì vậy việc trực quan hóa những bảng biểu này có thể giúp chúng ta quan sát và dễ dàng rút ra kết luận.

### 4.3.2. Ví dụ minh họa với Matplotlib/ Seaborn:

#### Ví dụ 1: Biểu đồ cột:

```python
import matplotlib.pyplot as plt

names = ["An", "Bình", "Chi", "Dũng"]
salary = [500, 1200, 800, 1500]

plt.bar(names, salary)
plt.xlabel("Tên")
plt.ylabel("Lương")
plt.title("So sánh lương theo từng người")
plt.show()
```

<figure>
  <img src="../image/libraries_ml.png" alt="" width="700">
  <figcaption><em></em></figcaption>
</figure>

#### Ví dụ 2: Biểu độ phân bố theo lương:

```python
import seaborn as sns

sns.histplot(salary, bins=10)
plt.title("Phân bố mức lương")

plt.show()
```

Kết quả nhận được:

<figure>
  <img src="../image/libraries_ml_2.png" alt="" width="700">
  <figcaption><em></em></figcaption>
</figure>
