# FEDERATED LEARNING FOR SMART HEALTHCARE

From the paper: [Federated-Learning-for-Smart-Healthcare-A Survey.pdf](/Paper/Federated-Learning-for-Smart-Healthcare-A%20Survey.pdf)

## What is FL?

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

## Keyword
