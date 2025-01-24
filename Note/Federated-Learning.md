# FEDERATED LEARNING FOR SMART HEALTHCARE

From the paper: [Federated-Learning-for-Smart-Healthcare-A Survey.pdf](/Paper/Federated-Learning-for-Smart-Healthcare-A%20Survey.pdf)

## What is FL?

Federated Learning (FL) is a distributed artificial intelligence (AI) approach that enables the training of high-quality AI models by **averaging local updates aggregated from multiple clients**, such as hospitals or Internet of Medical Things (IoMT) devices, without needing direct access to the raw data. This approach is particularly attractive for smart healthcare because it can coordinate multiple clients to perform AI training without sharing sensitive raw data

## Features of FL

## How does it work?

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

## Keyword
