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
