# FEDERATED LEARNING FOR SMART HEALTHCARE

From the paper: [Federated-Learning-for-Smart-Healthcare-A Survey.pdf](/Paper/Federated-Learning-for-Smart-Healthcare-A%20Survey.pdf)

## What is FL?

Federated Learning (FL) is a distributed artificial intelligence (AI) approach that enables the training of high-quality AI models by **averaging local updates aggregated from multiple clients**, such as hospitals or Internet of Medical Things (IoMT) devices, without needing direct access to the raw data. This approach is particularly attractive for smart healthcare because it can coordinate multiple clients to perform AI training without sharing sensitive raw data

---

## Features of FL

Federated Learning (FL) has several key features that make it attractive for smart healthcare, especially in scenarios where data privacy is a concern. Here's a breakdown of these features:

- Data Privacy Improvement: FL allows local health data to remain at local medical sites and devices, with only local updates, such as model gradients, being required by the central server for AI training. This reduces the risk of sensitive user information being leaked to external third parties, thus providing a higher degree of user privacy.

- Trade-off between Accuracy and Utility: FL offers a balance between accuracy, utility, and privacy. While it retains model generalizability, it may result in a nominal accuracy loss compared to conventional centralized learning.

- Low-Cost Health Data Training: FL can significantly reduce communication costs, such as latency and transmit power, by avoiding the transfer of large data volumes to the server. Model gradients are generally smaller in size compared to actual datasets, which saves network bandwidth and reduces the possibility of network congestion in large healthcare networks.

- Three main categories of FL: Horizontal Federated Learning (HFL), Vertical Federated Learning (VFL), and Federated Transfer Learning (FTL).

Despite these benefits, it is important to note that FL does not fully address the privacy problem in smart healthcare and dedicated privacy protection mechanisms may be needed to enhance FL in healthcare networks

## How does it work?

The federated learning (FL) process for smart healthcare involves several key steps:

1. **System Initialization and Client Selection**: The aggregation server selects a healthcare analytic task, like medical imaging or human motion detection. It also determines model requirements, such as task classification or prediction, and learning parameters like neural node numbers and learning rates. A subset of clients (e.g., hospitals) is chosen to participate in the FL process.

2. **Distributed Local Training and Updates**: The server sends an initial model, including a global gradient, to the selected clients, triggering distributed training. In each communication round, each client trains a local model using its own dataset and calculates its model update, such as the gradient in neural networks. The client then uploads its model update to the server.

3. **Model Aggregation and Download**: The server aggregates the updates received from the selected clients using an aggregation method such as the Federated Averaging (FedAvg) algorithm. In FedAvg, the gradient parameters of local models are averaged element-wise with weights proportional to the sizes of the client datasets. The server then calculates a new version of the global model and broadcasts it to all clients as the basis for further local model updates in the next learning round. The FL process iterates until the global loss function converges

## How many types of FL?

In the context of federated learning (FL) for smart healthcare, there are **three main types of FL** described: **Horizontal FL (HFL)**, **Vertical FL (VFL)**, and **Federated Transfer Learning (FTL)**.

### 1. Horizontal Federated Learning (HFL)
Horizontal FL (HFL) is used when healthcare clients train a shared global model using datasets with the **same feature space** but **different sample spaces**. The key characteristics of HFL include:

- **Local Model Training:** Local FL participants use the same AI model to train their respective datasets.
- **Global Model Aggregation:** A central server combines local updates from participants to create a global update, without requiring direct access to local data.
- **Example:** Detecting speech disorders where multiple users speak the same sentence (feature space) with different voices (sample space) on their smartphones. The local updates are aggregated by a parameter server to enhance the global model.

### 2. Vertical Federated Learning (VFL)
Vertical FL (VFL) applies to scenarios where health datasets share the **same sample space** but have **different feature spaces**. The main features of VFL include:

- **Entity Alignment:** Solutions based on entity alignment address overlapping data samples at distributed clients. Encryption techniques are often integrated during local training to ensure data security.
- **Example:** A shared learning model among entities like hospitals and insurance companies. These entities serve the same patients (sample space) but manage different types of data:
  - Hospitals: Medical records.
  - Insurance companies: Healthcare costs.

### 3. Federated Transfer Learning (FTL)
Federated Transfer Learning (FTL) is designed to handle datasets with **different sample spaces** and **different feature spaces**. FTL leverages transfer learning techniques to:

- Calculate feature values from different feature spaces into a unified representation.
- Train local datasets based on the transformed feature representation.

By leveraging these types of FL, smart healthcare systems can enhance collaboration across distributed data sources while maintaining data privacy and security.

---

## What are some FL designs?

The sources discuss several advanced Federated Learning (FL) designs tailored to smart healthcare applications. These designs address challenges such as resource constraints, security vulnerabilities, privacy concerns, and the need for personalized services. Below is a breakdown of the key FL designs:

### 1. Resource-Aware FL
This design optimizes the use of computing and communication resources in FL systems, particularly in healthcare settings with resource-limited devices, such as IoMT (Internet of Medical Things) devices.

- **Device Scheduling:** Selects a subset of IoMT devices for training to minimize total training time.
- **Resource Allocation:** Jointly optimizes device scheduling and resource allocation to enhance FL performance, including bandwidth allocation among clients using the same or different FL services.
- **Multi-Armed Bandit (MAB) Theory:** Addresses challenges caused by unknown channel state information between IoMT devices and the aggregation server.
- **Hierarchical Federated Edge Learning:** Aggregation is partially performed by intermediary nodes, such as hospitals, to reduce communication overhead.

### 2. Secure FL
This design mitigates security vulnerabilities in FL systems, such as poisoning attacks, inference attacks, and malicious servers, ensuring secure and trustworthy learning.

- **Reputation-Based Device Selection:** Introduces a reputation system to select reliable devices and prevent updates from untrusted devices.
- **Decentralized FL:** Removes reliance on a central server using methods like gossip, consensus, and diffusion. Blockchain can be used to manage user reputation and coordinate global model calculations in a peer-to-peer manner.
- **Secure Aggregation:** Protects the aggregation process at the central server using methods like:
  - Secure communication protocols.
  - Dining Cryptographers (DC)-based secure aggregation.
  - Homomorphic threshold encryption.
  - Pairwise masking.

### 3. Privacy-Enhanced FL
This design addresses privacy concerns, such as membership attacks, unintentional data leakage, and inference attacks.

- **Differential Privacy:** Adds artificial noise to local datasets or model updates to ensure privacy. This requires balancing privacy guarantees with model accuracy.
- **Bandwidth-Efficient FL:** Reduces data transmission by:
  - Sending only the signs of updated values.
  - Using techniques like sparse ternary compression.
- **FL-SIGN-DP:** Ensures that hospitals cannot infer the global model broadcast by the aggregation server.

### 4. Incentive-Aware FL
This design encourages participation in FL by addressing resource limitations, privacy concerns, and trust issues that might discourage IoMT devices from sharing their models.

- **Game Theory:** Uses tools like the Stackelberg game to incentivize user participation by maximizing the utility of both IoMT devices and the aggregation server.
- **Deep Reinforcement Learning (DRL):** Helps:
  - Aggregation servers determine reward strategies.
  - Devices decide on local training schemes.
- **Data Contribution Evaluation:** Evaluates device contributions based on metrics like:
  - Data quantity.
  - Data quality.
  - Device reputation.

### 5. Personalized FL
This design creates personalized models for individual users rather than a single global model, recognizing the unique physical characteristics, environments, and needs of each user.

- **Edge-Cloud Architectures:** Combines local model training at the network edge (e.g., at home) with global model aggregation in the cloud.
- **Label Heterogeneity:** Addresses challenges where each device defines labels differently. Techniques like 𝛼-weighted updates are used to aggregate overlapping label information.

### 6. Combining FL Designs
These FL designs are not mutually exclusive and can be combined to create robust and effective systems. For example:
- A healthcare application might use resource-aware techniques, secure aggregation, and differential privacy simultaneously to address multiple challenges.
- Specific design choices depend on the requirements and constraints of the healthcare application.

By adopting these advanced FL designs, smart healthcare systems can achieve efficient, secure, and personalized solutions while maintaining data privacy and addressing resource limitations.

---

## Keyword
Artificial Intelligence - Federated Learning - Smart healthcare

## Glossary
# Glossary (Thuật ngữ)

| **Term** | **Definition** | **Translation (Tiếng Việt)** |
|----------|--------------|---------------------------|
| **Federated Learning (FL)** | A distributed AI approach that enables training AI models without sharing raw data, by aggregating local updates from multiple clients. | Học liên kết (FL) là một phương pháp AI phân tán cho phép huấn luyện mô hình AI mà không cần chia sẻ dữ liệu gốc, bằng cách tổng hợp các bản cập nhật cục bộ từ nhiều thiết bị khác nhau. |
| **Horizontal Federated Learning (HFL)** | FL type where clients share the same feature space but have different sample spaces. | Học liên kết ngang (HFL) là một loại FL trong đó các khách hàng có cùng không gian đặc trưng nhưng khác không gian mẫu. |
| **Vertical Federated Learning (VFL)** | FL type where clients share the same sample space but have different feature spaces. | Học liên kết dọc (VFL) là một loại FL trong đó các khách hàng có cùng không gian mẫu nhưng khác không gian đặc trưng. |
| **Federated Transfer Learning (FTL)** | FL type where clients have both different sample spaces and different feature spaces, leveraging transfer learning techniques. | Học liên kết chuyển giao (FTL) là một loại FL trong đó các khách hàng có cả không gian mẫu và không gian đặc trưng khác nhau, tận dụng kỹ thuật học chuyển giao. |
| **Federated Averaging (FedAvg)** | A method for aggregating local updates in FL by averaging model gradients proportionally to dataset sizes. | Phương pháp trung bình liên kết (FedAvg) là một cách tổng hợp các bản cập nhật cục bộ trong FL bằng cách lấy trung bình các gradient mô hình theo kích thước tập dữ liệu. |
| **Internet of Medical Things (IoMT)** | A network of medical devices that collect and share health-related data. | Internet vạn vật y tế (IoMT) là mạng lưới các thiết bị y tế thu thập và chia sẻ dữ liệu sức khỏe. |
| **Differential Privacy** | A privacy-enhancing technique that adds noise to data to prevent individual data identification. | Bảo mật vi sai là một kỹ thuật bảo vệ quyền riêng tư bằng cách thêm nhiễu vào dữ liệu để ngăn chặn việc nhận dạng cá nhân. |
| **Secure Aggregation** | A method in FL that ensures updates from clients remain private during the aggregation process. | Tổng hợp bảo mật là phương pháp trong FL giúp bảo vệ tính riêng tư của các bản cập nhật từ khách hàng trong quá trình tổng hợp mô hình. |
| **Personalized FL** | An FL approach that creates tailored AI models for individual users instead of a single global model. | Học liên kết cá nhân hóa là phương pháp FL tạo ra mô hình AI phù hợp với từng người dùng thay vì một mô hình chung. |
| **Reputation-Based Device Selection** | A technique in FL that selects trustworthy clients based on their past performance and reputation. | Chọn thiết bị dựa trên danh tiếng là kỹ thuật trong FL dùng để chọn các thiết bị đáng tin cậy dựa trên hiệu suất trước đó và danh tiếng của chúng. |
| **Decentralized FL** | A federated learning method that eliminates reliance on a central server, often using blockchain. | Học liên kết phi tập trung là phương pháp FL không phụ thuộc vào máy chủ trung tâm, thường sử dụng blockchain. |
| **Multi-Armed Bandit (MAB) Theory** | A decision-making algorithm used in FL to optimize resource allocation under uncertainty. | Lý thuyết Multi-Armed Bandit (MAB) là thuật toán ra quyết định được sử dụng trong FL để tối ưu hóa phân bổ tài nguyên trong điều kiện không chắc chắn. |
| **Game Theory in FL** | Used to design incentive mechanisms for encouraging client participation in FL. | Lý thuyết trò chơi trong FL được sử dụng để thiết kế các cơ chế khuyến khích sự tham gia của khách hàng trong FL. |
| **Deep Reinforcement Learning (DRL)** | A machine learning technique used in FL to improve training strategies and resource allocation. | Học tăng cường sâu (DRL) là một kỹ thuật máy học được sử dụng trong FL để cải thiện chiến lược huấn luyện và phân bổ tài nguyên. |
| **Aggregation Server** | A central server that collects local model updates from clients and combines them to update the global model. | Máy chủ tổng hợp là máy chủ trung tâm thu thập các bản cập nhật mô hình từ các thiết bị khách và kết hợp chúng để cập nhật mô hình toàn cục. |
| **Communication Round** | A cycle in FL where local clients train models and send updates to the central server. | Vòng giao tiếp là một chu kỳ trong FL, trong đó các thiết bị khách huấn luyện mô hình và gửi bản cập nhật lên máy chủ trung tâm. |
| **Local Model Training** | The process where each client trains a model using its own data before sending updates to the aggregation server. | Huấn luyện mô hình cục bộ là quá trình trong đó mỗi thiết bị khách tự huấn luyện mô hình bằng dữ liệu của chính nó trước khi gửi bản cập nhật đến máy chủ tổng hợp. |
| **Model Convergence** | The state where the global model reaches an optimal accuracy after several training iterations. | Hội tụ mô hình là trạng thái khi mô hình toàn cục đạt độ chính xác tối ưu sau nhiều vòng huấn luyện. |
| **Non-IID Data** | Data that is not independently and identically distributed across clients, making FL training more challenging. | Dữ liệu không độc lập và đồng nhất (Non-IID) là dữ liệu không được phân phối đồng đều giữa các thiết bị khách, làm cho quá trình huấn luyện FL khó khăn hơn. |
| **Heterogeneous Data** | Data collected from different sources with varying distributions and formats. | Dữ liệu không đồng nhất là dữ liệu được thu thập từ các nguồn khác nhau với sự phân bố và định dạng khác nhau. |
| **Model Poisoning Attack** | A security attack where malicious clients send manipulated updates to corrupt the global model. | Tấn công làm nhiễm độc mô hình là một kiểu tấn công an ninh trong đó các thiết bị khách độc hại gửi bản cập nhật bị thay đổi để phá hoại mô hình toàn cục. |
| **Inference Attack** | A privacy attack where an adversary attempts to infer sensitive information from a trained model. | Tấn công suy luận là một kiểu tấn công quyền riêng tư, trong đó kẻ tấn công cố gắng suy ra thông tin nhạy cảm từ mô hình đã được huấn luyện. |
| **Secure Multi-Party Computation (SMPC)** | A cryptographic technique allowing multiple parties to jointly compute a function while keeping inputs private. | Tính toán đa bên an toàn (SMPC) là một kỹ thuật mã hóa cho phép nhiều bên cùng tính toán một hàm mà không cần tiết lộ dữ liệu đầu vào. |
| **Homomorphic Encryption** | An encryption method that allows computation on encrypted data without decryption. | Mã hóa đồng hình là một phương pháp mã hóa cho phép thực hiện tính toán trên dữ liệu đã mã hóa mà không cần giải mã. |
| **Blockchain for FL** | Using blockchain to decentralize FL, ensuring trust, security, and transparency in the learning process. | Blockchain trong FL là việc sử dụng blockchain để phân cấp FL, đảm bảo tính tin cậy, bảo mật và minh bạch trong quá trình học máy. |
| **Edge Computing** | A computing paradigm that processes data closer to its source rather than relying on a centralized server. | Điện toán biên là mô hình xử lý dữ liệu gần với nguồn dữ liệu thay vì phụ thuộc vào máy chủ tập trung. |
| **Overfitting in FL** | When a local model becomes too specialized in client data, leading to poor generalization in the global model. | Quá khớp trong FL xảy ra khi mô hình cục bộ trở nên quá chuyên biệt với dữ liệu của thiết bị khách, dẫn đến khả năng tổng quát kém trong mô hình toàn cục. |
| **Bandwidth-Efficient FL** | An FL approach that minimizes communication overhead by reducing data transmission size. | Học liên kết tiết kiệm băng thông là phương pháp FL giúp giảm tải truyền thông bằng cách giảm kích thước dữ liệu truyền tải. |
| **Gradient Compression** | A technique in FL that reduces the size of model updates sent to the central server to save bandwidth. | Nén gradient là một kỹ thuật trong FL giúp giảm kích thước của các bản cập nhật mô hình gửi đến máy chủ trung tâm để tiết kiệm băng thông. |
| **Model Distillation** | A method to transfer knowledge from a larger model to a smaller one in FL. | Chưng cất mô hình là phương pháp truyền tải kiến thức từ một mô hình lớn sang một mô hình nhỏ hơn trong FL. |
| **Federated Hyperparameter Tuning** | The process of optimizing hyperparameters in FL without sharing raw data. | Điều chỉnh siêu tham số liên kết là quá trình tối ưu hóa siêu tham số trong FL mà không cần chia sẻ dữ liệu gốc. |
