# Xử lý dữ liệu bảng (Tabular Data)

**Decision Trees** và **Random Forests**: Đây là các thuật toán học máy cơ bản, thường dùng để tìm ra các đặc trưng quan trọng trong dữ liệu bảng và có thể giúp tạo ra những đặc trưng quan trọng để huấn luyện mạng đa mô hình.

L**ogistic Regression**: Thường dùng trong các bài toán phân loại nhị phân hoặc đa lớp với dữ liệu bảng và có thể được dùng như baseline để so sánh với các mô hình phức tạp hơn.

# Xử lý dữ liệu ảnh (Image Data)

**Convolutional Neural Networks (CNN):** Đây là mô hình cơ bản trong xử lý ảnh, giúp trích xuất đặc trưng từ ảnh. Bạn có thể dùng các lớp CNN cơ bản như Conv2D, MaxPooling, và Flatten để tạo bộ đặc trưng từ ảnh cho việc kết hợp với dữ liệu bảng.

**Principal Component Analysis (PCA)**: Nếu dữ liệu ảnh quá lớn, bạn có thể dùng PCA để giảm số chiều của ảnh, giúp tối ưu việc huấn luyện và tiết kiệm tài nguyên.

# Kỹ thuật kết hợp mô hình (Fusion Techniques)

**Concatenation:** Là phương pháp đơn giản để kết hợp đặc trưng từ dữ liệu bảng và ảnh bằng cách nối (concatenate) các đầu ra của các lớp trước khi đưa vào layer cuối cùng.

**Weighted Average:** Đôi khi, bạn có thể tính trung bình có trọng số (weighted average) giữa các đầu ra từ các modal khác nhau để tối ưu việc kết hợp.

# Federated Learning (FL)
**Federated Averaging (FedAvg)**: Đây là thuật toán cơ bản nhất trong Federated Learning, giúp tổng hợp các mô hình của client thông qua trung bình hóa trọng số. Dùng FedAvg trong những trường hợp này là hợp lý để thử nghiệm bước đầu.

**Gradient Descent và Stochastic Gradient Descent (SGD):** Các phương pháp này giúp tối ưu các tham số của mô hình và có thể được tích hợp vào từng client trong Federated Learning.
