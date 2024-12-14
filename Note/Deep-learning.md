# TỔNG QUAN VỀ DEEP LEARNING (HỌC SÂU)
Là một lĩnh vực của Trí tuệ nhân tạo (AI), bắt chước cách hoạt động của não bộ con người để xử lý dữ liệu, tạo ra các mẫu để sử dụng cho việc đưa ra quyết định.

## Mục lục
1. [Deep Learning là gì?](#deep-learning-là-gì)
2. [Ưu điểm và nhược điểm](#ưu-điểm-và-nhược-điểm)
3. [Cách hoạt động của Deep Learning](#cách-hoạt-động-của-deep-learning)
4. [Kĩ thuật Deep Learning](#kĩ-thuật-deep-learning)
    * [ANN](#artificial-neural-network-ann---mạng-nơ-ron-cổ-điển)
    * [CNN](#convolutional-neural-network-cnn)
    * [RNN](#recurrent-neural-network-rnn)
    * [GAN](#generative-adversarial-networks-gan)
    * [Boltzmann machine](#boltzmann-machine)
    * [Deep Reinforcement Learning](#deep-reinforcement-learning)
    * [Autoencoder](#autoencoder)
    * [Backpropagation](#backpropagation)
5. [Deep Learning giải quyết những vấn đề gì?](#deep-learning-giải-quyết-những-vấn-đề-gì)
6. [Có nên sử dụng Deep Learning thay cho Machine Learning?](#có-nên-sử-dụng-deep-learning-thay-cho-machine-learning)

## Deep Learning là gì?

- Deep Learning (DL) - học sâu, được xem là một lĩnh vực con của trí tuệ nhân tạo, ở đây, các máy tính **sẽ học và cải thiện chính nó thông qua các thuật toán**. Deep learning chủ yếu hoạt động với các **mạng nơ-ron nhân tạo** để bắt chước khả năng tư duy và suy nghĩ của con người.

![Deep learning](/Asset/Image/deeplearning-la-gi.webp)

- Mạng nơ-ron nhân tạo chính là động lực để phát triển DL. Mạng nơ-ron sâu (DNN) bao gồm nhiều lớp nơ-ron khác nhau, có khả năng thực hiện các phép tính phức tạp.

## Ưu điểm và Nhược điểm

- Ưu điểm:
    - Kiến trúc mạng nơ-ron linh hoạt, có thể dễ dàng thay đổi dựa trên các yêu cầu khác nhau.
    - Có khả năng giải quyết nhiều bài toán với tính chính xác rất cao.
    - Tính tự động hoá cao, có khả năng tự điều chỉnh và tự tối ưu.
    - Có khả năng thực hiện tính toán song song, hiệu năng tốt, xử lý được lượng dữ liệu lớn.

- Nhược điểm:
    - Cần có khối lượng dữ liệu rất lớn để tận dụng sức mạnh của DL.
    - Chi phí tính toán cao.
    - Chưa có nền tảng lý thuyết mạnh mẽ để lựa chọn các công cụ tối ưu cho Deep Learning.

## Cách hoạt động của Deep Learning

- Một mạng nơ-ron bao gồm nhiều lớp (layer) khác nhau, số layer càng nhiều thì mạng sẽ càng "sâu". Nhưng về thực tế chỉ có 3 loại layer khác nhau:
    - *Input layer*: Nhận dữ liệu
    - *Hidden layer*: Thực hiện các phép tính trung gian và trích xuất đặc trưng từ dữ liẹu
    - *Output layer*: Đưa ra kết quả cuối cùng.
- Trong các kiến trúc hiện đại, như mạng ResNet hay Transformer, còn có thêm khái niệm như **skip connections** hoặc **attention layers**, nhưng chúng vẫn tuân theo nguyên tắc cơ bản của ba loại lớp trên.

- Trong mỗi layer là các nút mạng (node) và được liên kết với những lớp liền kề khác. Mỗi kết nối giữa các node sẽ có một **trọng số** tương ứng (xác định mức độ quan trọng của kết nối giữa 2 nơ-ron), trọng số càng cao thì ảnh hưởng của kết nối này đến mạng nơ-ron càng lớn.

- Bên cạnh đó, chúng ta còn có **độ chệch (bias)**, giá trị giúp điều chỉnh đầu ra của nơ-ron, đảm bảo học được các mối quan hệ *phi tuyến tính* trong dữ liệu.

- Các hidden layer thực hiện các phép tính cho các input đầu vào. Thử thách lớn nhất đó chính là quyết định số lượng mạng nơ-ron cho mỗi layer cũng như các hidden layer, dựa trên các yếu tố sau:
    - Đặc trưng của dữ liệu.
    - Độ phức tạp của bài toán.
    - Nguy cơ **overfitting** nếu dùng quá nhiều nơ-ron/layers.

- Mỗi nơ-ron sẽ có một **hàm kích hoạt** (Activation function), về cơ bản thì có nhiệm vụ “chuẩn hoá” đầu ra từ nơ-ron này. 

![Layer của Deep Learning](/Asset/Image/dl-noron.webp)

## Kĩ thuật Deep Learning

### Artificial Neural Network (ANN - Mạng nơ-ron cổ điển)

- Về cơ bản, đây là một mô hình tính toán được xây dựng dựa trên cấu trúc và chức năng của mạng lưới nơ ron trong Sinh học.

- Nói cách khác, đây là loại mạng mô phỏng bộ não con người và được sử dụng trong Machine Learing và Deep Learning để đưa ra **dự đoán và thu thập thông tin chi tiết từ dữ liệu**.

- ANN là dữ liệu thống kê **phi tuyến tính.**

- Kiến trúc ANN tương đối đơn giản, phù hợp nhất với các bộ dữ liệu có **dạng bảng** hoặc **những bài toán phân loại, hồi quy** có đầu vào là **giá trị thực.**

![ANN](/Asset/Image/ANN.png)

- Có 2 loại ANN:    
    
    - FeedForward ANN:

        * Chỉ gồm luồng thông tin 1 chiều, khong xuất hiện vòng phản hồi (gửi ngược thông tin về lại). Mô hình này được sử dụng để nhận dạng một mẫu cụ thể, vì chúng chứa các đầu vào và ra cố định
![FeedForwar ANN](/Asset/Image/FeedForward-ANN.png)

    - FeedBack ANN:

        * Cho phép các vòng lặp phản hồi. Sử dụng mô hình này trong các bộ nhớ có thể giải quyết nội dung.
![FeedBack ANN](/Asset/Image/FeedBack-ANN.png)


### Convolutional Neural Network (CNN)

### Recurrent Neural Network (RNN)

### Generative Adversarial Networks (GAN)

### Boltzmann machine

### Deep Reinforcement Learning 

### Autoencoder

### Backpropagation

## Deep Learning giải quyết những vấn đề gì?

- Trợ lý ảo
- Hệ thống lái xe tự động
- Mạng xã hội
- Phân tích cảm xúc

## Có nên sử dụng Deep Learning thay cho Machine Learning?

- Phụ thuộc phần lớn vào mục tiêu và chiến lược kinh doanh cụ thể, số lượng dữ liệu, tài nguyên,… 

## Trang web tham khảo:

https://vietnix.vn/deep-learning-la-gi/#cac-ky-thuat-deep-learning

https://viettelidc.com.vn/tin-tuc/cam-nang-ai-artificial-neural-network-la-gi-cau-truc-cach-hoat-dong-va-ung-dung-cua-mo-hinh-nay
