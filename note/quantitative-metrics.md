# CHỈ SỐ ĐỊNH LƯỢNG MÔ HÌNH

## Tại sao cần phải đánh giá?

- Overfitting và Underfitting là hai nguyên nhân lớn nhất dẫn đến hiệu suất kém của các thuật toán học máy.

    - **Overfitting**: Xảy ra khi Mô hình hoạt động tốt đối với một tập hợp dữ liệu cụ thể (Dữ liệu đã biết) và do đó có thể không phù hợp với dữ liệu bổ sung (Dữ liệu không xác định).

    - **Underfitting**: Xảy ra khi mô hình không thể nắm bắt đầy đủ cấu trúc cơ bản của dữ liệu.

## Chỉ số đánh giá

- Các chỉ số phân loại (accuracy, precision, recall, F1-score, ROC, AUC, …)
- Chỉ số hồi quy (MSE, MAE)
- Chỉ số xếp hạng (MRR, DCG, NDCG)
- Số liệu thống kê (Correlation)
- Các chỉ số thị giác máy tính (PSNR, SSIM, IoU)
- Các chỉ số NLP (Perplexity, BLEU score)
- Các chỉ số liên quan đến Deep Learning Inception score, Frechet Inception distance. 

- Lưu ý: Để áp dụng cho đồ án có sự kết hợp giữa Federated Learning và Multimodal, chúng tôi đã lên kế hoạch tập trung vào các chỉ số **Phân loại**.

## Chỉ số phân loại

- Khi thực hiện các dự đoán phân loại, có bốn loại kết quả có thể xảy ra:

    - **True positives (TP)** là khi chúng ta dự đoán một quan sát thuộc về một lớp và nó thực sự thuộc về lớp đó.
    - **True Negative (TN)** là khi chúng ta dự đoán một quan sát không thuộc về một lớp và nó thực sự không thuộc lớp đó.
    - **False Positive (FP)** xảy ra khi chúng ta dự đoán một quan sát thuộc về một lớp trong khi thực tế thì không.
    - **False Negative (FN)** xảy ra khi chúng ta dự đoán một quan sát không thuộc về một lớp trong khi thực tế là nó có.

### Accuracy

- Accuracy là một thước đo để đánh giá các mô hình phân loại. Về mặt hình thức, accuracy có thể được định nghĩa là số lần dự đoán đúng trên tổng số lần dự đoán

> Accuracy = Number of correct predictions / Total number of predictions
> Accuracy = TP + TN / TP + TN + FP + FN

> [!NOTE]
> % dự đoán đúng

### Precision

- **Precsion** (còn được gọi là giá trị dự đoán dương) là phần nhỏ của các trường hợp có liên quan trong số các trường hợp được truy xuất

- Trong phân loại, **Precision** là số lượng trường hợp tích cực thực sự (TP) trong tổng số trường hợp được gắn nhãn là thuộc lớp tích cực

> Precision = TP / TP + FP

> [!NOTE]
> Dự đoán đúng trong số dự đoán là ung thư

### Recall

- **Recall** (còn được gọi là độ nhạy) là phần của các trường hợp có liên quan đã được truy xuất.

- **Recall** là số lượng các trường hợp dương thực sự trên tổng số các trường hợp thực sự thuộc về lớp tích cực

>  Recall = TP / TP + FN

> [!NOTE]
> Bắt được bao nhiêu ca ung thư thực sự

- Recall quan trọng hơn Precision Vì mục đích đưa ra không muốn bỏ sót người bệnh. **Thà báo nhầm còn hơn để sót.**

### F1-score

- F1-score là chỉ số tổng hợp giữa Precision và Recall, được thiết kế để cân bằng giữa 2 yếu tố này.

- F1-score là **trung bình điều hòa (harmonic mean)**, không phải trung bình cộng, vì nó phạt nặng nếu 1 trong 2 chỉ số thấp. F1-score chỉ nằm trong khoảng (0,1].

> F1  = (1+B^2) * ((precision * recall) / (B^2 * precision + recall))

-  F1 chính là một trường hợp đặc biệt của Fg khi B = 1. Khi B > 1, recall được coi trọng hơn precision, khi B < 1, precision được coi trọng hơn. Hai đại lượng B thường được sử dụng là B = 2 và B = 0.5.

> [!NOTE]
> Dữ liệu mất cân bằng

- Dữ liệu mất cân bằng là sự phân bổ các mẫu trên các class - label **chênh lệch quá lớn** dẫn tới việc mô hình tập trung chỉ học những đặc trưng của class có nhiều data, không khái quát được toàn bộ mẫu.

### ROC (Receiver Operating Characteristic)

- Là một đồ thị thể hiện hiệu suất của một mô hình phân loại ở tất cả các ngưỡng phân loại.

- Đường cong này vẽ hai tham số:
    - Tỷ lệ Tích cực Thực sự (True Positive Rate (TPR)) = Recall = % bắt đúng bệnh
    - False Positive Rate (FPR) = % báo nhầm người khoẻ là bệnh

-  Nói cách khác, ROC thể hiện “được việc” và “báo nhầm” trên cùng 1 biểu đồ khi ta thay đổi ngưỡng dự đoán.    

- Cụ thể

| Ngưỡng | Dự đoán kiểu gì?           |
| ------ | -------------------------- |
| 0.1    | Cực kỳ dễ báo bệnh (nhạy)  |
| 0.5    | Cân bằng                   |
| 0.9    | Chỉ báo khi cực kỳ chắc ăn |


### AUC (Area Under the Curve)

- Diện tích dưới đường cong (AUC), là thước đo tổng hợp hiệu suất của bộ phân loại nhị phân trên tất cả các giá trị ngưỡng có thể có (và do đó nó là ngưỡng bất biến)

- Nói cách khác, biểu diễn khả năng phân biệt tốt – xấu tổng thể của mô hình, không phụ thuộc ngưỡng.

- Cụ thể:

| AUC  | Ý nghĩa            |
| ---- | ------------------ |
| 1.0  | Mô hình hoàn hảo |
| 0.9+ | Rất tốt          |
| 0.8+ | Tốt              |
| 0.7+ | Trung bình       |
| 0.5  | Đoán ngẫu nhiên  |
| <0.5 | Tệ hơn đoán bừa   |

## Chỉ số hiệu năng FL (Federated System Performance)

- Nhóm này đánh giá độ trễ, khả năng mở rộng và tính thực tiễn của hệ thống phân tán.

- Bảng tổng hợp

| Chỉ số                           | Ý nghĩa                                                     | Cách đo                          |
| -------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| **Communication latency**        | Thời gian gửi/nhận model giữa client & server trong 1 round | `time.time()` trước/sau mỗi vòng |
| **Training time per client**     | Thời gian train nội bộ trên mỗi client                      | `time()` đo từng client          |
| **Aggregation time**             | Thời gian server tổng hợp các model client                  | `time()` trong server            |

## Chỉ số về kích thước và tải mô hình (Model Size & Bandwidth)

| Chỉ số                          | Mục tiêu                                        | Mối quan hệ                         |
| ------------------------------- | ----------------------------------------------- | ----------------------------------- |
| **Model size (KB/MB)**          | Kích thước mô hình gửi đi giữa client và server | Tỷ lệ thuận với băng thông tiêu tốn |
| **Bandwidth usage**             | Dung lượng truyền qua mạng mỗi round            | ≈ model size x số client            |

## Chỉ số về tính riêng tư và độ tin cậy (Privacy & Robustness) (Tùy chọn)

-  Nhấn mạnh lý do dùng FL thay vì Centralized Learning.

| Chỉ số / Thuộc tính                  | Ghi chú                                       | Định lượng                                                |
| ------------------------------------ | --------------------------------------------- | --------------------------------------------------------- |
| **Khả năng phục hồi khi mất client** | Server vẫn tổng hợp mô hình nếu 1 client down | Mô tả qualitative                                         |
| **Reproducibility**                  | Các round có deterministic nếu seed cố định   | Có thể kiểm tra bằng log                                  |
| **Privacy by design**                | Không gửi dữ liệu gốc, chỉ gửi model          | Đưa vào phần lý thuyết chứ không cần code test            |
| **Attack resistance**                | Kháng mô hình giả mạo, poisoning attack       | Nếu đồ án nâng cao, thử nghiệm FedProx hoặc robust FedAvg |

## Tổng hợp

| **Nhóm tiêu chí**                     | **Chỉ số cần đánh giá**                                                                        | **Lý do cần thiết**                                                                      |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
|  **Hiệu quả mô hình (core ML)**     | - Accuracy<br>- Precision<br>- Recall<br>- F1-score<br>- AUC/ROC                               | Đánh giá mô hình có học hiệu quả và phân biệt đúng không. Bắt buộc trong mọi báo cáo AI. |
|  **Hiệu quả huấn luyện FL**         | - Số vòng (rounds) đến hội tụ<br>- Accuracy theo từng round<br>- Thời gian huấn luyện mỗi vòng | Kiểm tra xem FL có học ổn định, đủ nhanh và tiết kiệm tài nguyên không.                  |
|  **Hiệu suất truyền thông (Comm.)** | - Độ trễ (latency)<br>- Kích thước mô hình truyền mỗi vòng<br>- Tổng số byte truyền qua mạng   | Rất quan trọng với FL – mô hình truyền qua mạng, cần tối ưu băng thông.                  |