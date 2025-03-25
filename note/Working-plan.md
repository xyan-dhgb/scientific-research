# Kế Hoạch Triển Khai Đồ Án

**Đề Tài:** *Applying Federated Learning and Multimodal Artificial Intelligence to Cancer Diagnosis in Medical Science*  
**Thời Gian:** Từ hiện tại đến 02-06-2025

---

## Tuần 1: Thiết Lập Môi Trường & Khám Phá Dữ Liệu (EDA)

### 🎯 Mục tiêu:
- Thiết lập môi trường làm việc, cài đặt công cụ và thư viện.
- Thực hiện khám phá dữ liệu (EDA) cho ảnh y tế và file CSV.

### 📌 Công việc cụ thể:
- **Thiết lập môi trường:**
  - Cài đặt Python (phiên bản 3.9 trở lên).
  - Thiết lập môi trường ảo (*virtualenv* hoặc *conda*).

- **Cài đặt thư viện:**
  - `pandas`, `numpy`: xử lý dữ liệu CSV.
  - `opencv`, `pillow`: xử lý và tiền xử lý ảnh.
  - `matplotlib`, `seaborn`: trực quan hóa dữ liệu.

- **Khám phá dữ liệu (EDA):**
  - Kiểm tra chất lượng, số lượng và xử lý dữ liệu thiếu của CSV.
  - Tiền xử lý ảnh (resize, normalization, augmentation nếu cần).

---

## Tuần 2: Phát Triển Pipeline Tiền Xử Lý & Mô Hình Baseline

### 🎯 Mục tiêu:
- Xây dựng pipeline tiền xử lý cho từng modality.
- Phát triển mô hình baseline (centralized) cho ảnh và CSV.

### 📌 Công việc cụ thể:
- **Pipeline tiền xử lý:**
  - CSV: Sử dụng `pandas` và `scikit-learn` (chuẩn hóa, mã hóa,...).
  - Ảnh: Sử dụng `opencv`/`pillow` và `tensorflow`/`pytorch` để chuẩn bị input cho CNN.

- **Xây dựng mô hình baseline:**
  - Ảnh: CNN cơ bản với `keras` hoặc `pytorch`.
  - CSV: Mạng neural đơn giản hoặc mô hình cây quyết định.

---

## Tuần 3: Thiết Lập Môi Trường Federated Learning

### 🎯 Mục tiêu:
- Thiết lập môi trường mô phỏng Federated Learning.
- Lựa chọn công cụ/thư viện Federated Learning phù hợp.

### 📌 Công việc cụ thể:
- **Gợi ý công cụ/thư viện:**
  - `TensorFlow Federated (TFF)`: Nếu đã quen với TensorFlow.
  - `Flower (FL)`: Framework độc lập, hỗ trợ cả TensorFlow và PyTorch.

- Cài đặt và làm quen với framework đã chọn.
- Thiết kế cấu trúc phân chia dữ liệu giả lập các client (ví dụ: chia dataset thành các phần theo client).

---

## Tuần 4: Triển Khai Mô Hình Federated Learning cho Từng Modality

### 🎯 Mục tiêu:
- Triển khai mô hình FL cho ảnh y tế và CSV riêng biệt.

### 📌 Công việc cụ thể:
- Tách dữ liệu thành các client (áp dụng cho Horizontal FL khi các client có cùng *sample space*).
- Huấn luyện mô hình FL cơ bản cho từng modality.
- So sánh kết quả với mô hình tập trung (*centralized*).

---

## Tuần 5: Tích Hợp Đa Modality – Xây Dựng Mô Hình Multimodal FL

### 🎯 Mục tiêu:
- Tích hợp các modality thành một mô hình thống nhất trong môi trường FL.

### 📌 Công việc cụ thể:
- **Phát triển chiến lược kết hợp dữ liệu:**
  - *Early Fusion*: Kết hợp dữ liệu sau tiền xử lý, trước khi đưa vào mô hình chính.
  - *Late Fusion*: Kết hợp các đặc trưng/quyết định từ các mô hình riêng biệt.

- **Thử nghiệm kiến trúc mạng phù hợp** (ví dụ: kết hợp CNN cho ảnh và MLP cho CSV).
- **Đánh giá hiệu quả** của mô hình multimodal FL.

---

## Tuần 6: Tối Ưu Hóa & Tinh Chỉnh Mô Hình

### 🎯 Mục tiêu:
- Tinh chỉnh các tham số và cải thiện hiệu suất mô hình.

### 📌 Công việc cụ thể:
- Tuning *hyperparameters* cho mô hình.
- Thử nghiệm các chiến lược aggregation trong FL (ví dụ: *FedAvg*, *FedProx*).
- Đánh giá mô hình với các chỉ số: *accuracy, precision, recall, AUC*, đặc biệt chú trọng hiệu quả chẩn đoán ung thư.

---

## Tuần 7: Áp Dụng Transfer Learning & Cải Tiến Mô Hình

### 🎯 Mục tiêu:
- Áp dụng kỹ thuật *transfer learning* để cải thiện mô hình.

### 📌 Công việc cụ thể:
- Sử dụng *transfer learning* cho mô hình ảnh với các mô hình pretrained như `ResNet`, `DenseNet`.
- Tích hợp các cải tiến từ FL và multimodal để nâng cao hiệu suất.
- So sánh kết quả giữa các chiến lược.

---

## Tuần 8: Tổng Hợp Kết Quả & Phân Tích

### 🎯 Mục tiêu:
- Tổng hợp và phân tích kết quả thực nghiệm.

### 📌 Công việc cụ thể:
- So sánh kết quả giữa các mô hình: centralized, FL đơn modality và multimodal FL.
- Chuẩn bị biểu đồ, báo cáo thống kê.
- Xác định hạn chế và đề xuất cải tiến cho tương lai.

---

## Tuần 9: Hoàn Thiện Báo Cáo & Chuẩn Bị Bảo Vệ

### 🎯 Mục tiêu:
- Hoàn thiện báo cáo đồ án và chuẩn bị slide, tài liệu cho buổi bảo vệ.

### 📌 Công việc cụ thể:
- Viết báo cáo chi tiết (*phương pháp, kết quả, thảo luận,...*).
- Soạn slide thuyết trình và tập dượt bảo vệ.
- Kiểm tra lại toàn bộ code, tài liệu hướng dẫn và backup dự án.

---

# 📌 Gợi Ý Công Cụ và Thư Viện Python

### 🔹 **Federated Learning:**
- `TensorFlow Federated (TFF)`
- `Flower (FL)`

### 🔹 **Deep Learning & Multimodal Fusion:**
- `TensorFlow/Keras` hoặc `PyTorch`
- `PyTorch Lightning` (tùy chọn)

### 🔹 **Xử lý Dữ Liệu:**
- `pandas`, `numpy`
- `opencv`, `pillow`

### 🔹 **Trực Quan Hóa & Đánh Giá:**
- `matplotlib`, `seaborn`
- `scikit-learn` (cho các chỉ số như *accuracy, precision, recall, ROC AUC,...*)

---

Kế hoạch này cung cấp lộ trình rõ ràng từ việc tiền xử lý dữ liệu, xây dựng mô hình baseline, thiết lập môi trường FL cho đến tích hợp và tối ưu hóa mô hình multimodal.  
📌 **Bạn có thể linh hoạt điều chỉnh theo tiến độ thực tế. Chúc bạn thành công với đồ án của mình!** 🚀

# Bảng Tổng Hợp Các Thư Viện Quan Trọng

| **Thư viện**         | **Định nghĩa** | **Công dụng** | **Link Documentation** |
|----------------------|---------------|--------------|-----------------------|
| **TensorFlow** | Một framework mã nguồn mở phổ biến để xây dựng và huấn luyện mô hình học sâu (Deep Learning). | - Xây dựng mô hình CNN, MLP cho ảnh y tế và CSV. <br>- Huấn luyện và đánh giá mô hình FL. | [🔗 TensorFlow Docs](https://www.tensorflow.org/) |
| **TensorFlow Federated (TFF)** | Framework mở rộng của TensorFlow hỗ trợ mô phỏng và triển khai Federated Learning. | - Mô phỏng hệ thống FL. <br>- Triển khai các thuật toán FL như FedAvg. | [🔗 TFF Docs](https://www.tensorflow.org/federated) |
| **Flower (FL)** | Framework linh hoạt hỗ trợ cả TensorFlow và PyTorch để phát triển FL. | - Tạo môi trường FL với nhiều client. <br>- Huấn luyện mô hình FL đa dạng. | [🔗 Flower Docs](https://flower.ai/docs/) |
| **PyTorch** | Framework Deep Learning mạnh mẽ với khả năng tùy chỉnh cao. | - Xây dựng và huấn luyện mô hình DL. <br>- Kết hợp với Flower để triển khai FL. | [🔗 PyTorch Docs](https://pytorch.org/docs/stable/index.html) |
| **PyTorch Lightning** | Một wrapper giúp đơn giản hóa PyTorch, tăng tốc huấn luyện. | - Giúp code PyTorch dễ quản lý hơn. <br>- Tích hợp tốt với FL. | [🔗 PyTorch Lightning Docs](https://lightning.ai/docs/pytorch/stable/) |
| **NumPy** | Thư viện xử lý mảng số học nhanh trong Python. | - Xử lý dữ liệu ảnh và CSV. <br>- Hỗ trợ các phép toán ma trận, vector hóa. | [🔗 NumPy Docs](https://numpy.org/doc/) |
| **Pandas** | Thư viện xử lý dữ liệu dạng bảng mạnh mẽ. | - Tiền xử lý dữ liệu CSV. <br>- Hỗ trợ chuyển đổi dữ liệu thành DataFrame. | [🔗 Pandas Docs](https://pandas.pydata.org/docs/) |
| **OpenCV** | Thư viện xử lý ảnh mạnh mẽ, hỗ trợ Computer Vision. | - Tiền xử lý ảnh y tế (resize, augmentation). <br>- Xử lý và hiển thị ảnh. | [🔗 OpenCV Docs](https://docs.opencv.org/) |
| **Pillow (PIL)** | Thư viện xử lý ảnh đơn giản, nhẹ hơn OpenCV. | - Đọc, ghi và chuyển đổi định dạng ảnh. | [🔗 Pillow Docs](https://pillow.readthedocs.io/en/stable/) |
| **Matplotlib** | Thư viện vẽ biểu đồ dữ liệu mạnh mẽ. | - Trực quan hóa dữ liệu CSV. <br>- Hiển thị hình ảnh, biểu đồ kết quả. | [🔗 Matplotlib Docs](https://matplotlib.org/stable/contents.html) |
| **Seaborn** | Thư viện vẽ biểu đồ mở rộng từ Matplotlib. | - Biểu đồ thống kê đẹp hơn, dễ đọc hơn. | [🔗 Seaborn Docs](https://seaborn.pydata.org/) |
| **Scikit-learn** | Thư viện học máy (Machine Learning) phổ biến trong Python. | - Chuẩn hóa dữ liệu CSV. <br>- Tính toán độ chính xác, ROC AUC. | [🔗 Scikit-learn Docs](https://scikit-learn.org/stable/) |