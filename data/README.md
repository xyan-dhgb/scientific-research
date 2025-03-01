# CÁCH TÌM DATASET CHO ĐỀ TÀI

Để có được dataset phù hợp cho mô hình AI đa phương thức (Multimodal AI) gồm hình ảnh (image) và văn bản (text) cần nhất quán với nhau, chúng ta có thể thực hiện theo các cách sau:

## 1. Sử dụng Dataset Sẵn Có

Một số nguồn cung cấp dữ liệu đã được gán nhãn đúng chuẩn:

- **Dữ liệu về ung thư**

    - MIMIC-CXR: Tập dữ liệu chẩn đoán X-quang ngực với báo cáo y khoa chi tiết. https://physionet.org/content/mimic-cxr/2.0.0/
    
    - CheXpert: Dữ liệu X-quang với mô tả về bệnh lý. https://stanfordmlgroup.github.io/competitions/chexpert/
    
    - TCGA (The Cancer Genome Atlas): Bộ dữ liệu đa mô thức về hình ảnh mô học và dữ liệu lâm sàng bệnh ung thư. https://portal.gdc.cancer.gov/
    
    - PAIP 2019 Challenge: Bộ dữ liệu hình ảnh bệnh lý ung thư gan, kèm chú thích từ bác sĩ. https://paip2019.grand-challenge.org/

- **Nguồn dữ liệu tổng hợp**

    - MedPix: Kho dữ liệu ảnh y tế với mô tả. https://medpix.nlm.nih.gov/home

    - OpenNeuro: Dữ liệu MRI, PET scan với chú thích đầy đủ. https://openneuro.org/

    - BioMedISeg: Bộ dữ liệu hình ảnh y tế có kèm mô tả. https://biomedseg.github.io/

## 2. Web Scraping để Tạo Dataset Riêng

Nếu không tìm thấy dataset phù hợp, chúng ta có thể thu thập dữ liệu từ nguồn mở bằng cách scrape từ trang web y khoa. Ví dụ:

- *Công cụ scraping*: 

    - BeautifulSoup hoặc Scrapy (Python) để lấy dữ liệu từ trang web y khoa.

    - Selenium nếu trang web cần tải JavaScript.

    - Tesseract OCR nếu cần trích xuất văn bản từ hình ảnh.

- *Nguồn dữ liệu tiềm năng:*

    - PubMed, NIH, WHO: Chứa bài báo y khoa có hình ảnh.

    - Wikipedia + Wikimedia Commons: Hình ảnh y tế với mô tả chi tiết.

    - Reddit / Kaggle Datasets: Các cộng đồng chia sẻ dataset mở.

## 3. Chuyển Đổi Dữ Liệu Hiện Có Thành Multimodal

- Tạo chú thích tự động bằng NLP

    - Dùng BLIP (Bootstrapped Language-Image Pretraining) để tạo mô tả tự động.

    - Dùng BioBERT để chuẩn hóa văn bản mô tả.

- Dịch dữ liệu phi cấu trúc thành có cấu trúc

    - Dùng spaCy + Named Entity Recognition (NER) để trích xuất thông tin từ báo cáo.

    - Gán nhãn dữ liệu bằng Label Studio.

- Sử dụng ChatGPT hoặc GPT-4 để sinh văn bản mô tả từ hình ảnh
