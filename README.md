# FoodSight AI: Multidisciplinary Indian Food Recognition & Tracking Ecosystem

![FoodSight AI Banner](https://img.shields.io/badge/FoodSight-AI-ff6b6b?style=for-the-badge&logo=fastapi)
![Render Deployment](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render)
![IoT Powered](https://img.shields.io/badge/IoT-ESP32--CAM-orange?style=for-the-badge&logo=espressif)
![Deep Learning](https://img.shields.io/badge/AI-MobileNetV3-yellow?style=for-the-badge&logo=tensorflow)

**FoodSight AI** is a comprehensive multidisciplinary research project that bridges the gap between IoT hardware, deep learning, and personal nutrition. Unlike traditional calorie counters that require manual input, FoodSight AI leverages automated visual recognition to make dietary tracking seamless, accurate, and interactive.

---

## 🌟 Project Vision & Goals
The fundamental objective of FoodSight AI is to solve the "tracking fatigue" associated with nutritional logs. By integrating a physical capture trigger (IoT) with a high-accuracy recognition engine (AI), we provide a frictionless experience for users to manage their metabolic health, specifically tailored for the complexities of **Indian Cuisine**.

---

## 🏗️ Technical Architecture (The Three-Tier System)

### 1. Tier 1: The "Smart Kitchen" (IoT/Hardware)
*Developed by the VLSI & Hardware Team*
- **Hardware Core**: ESP32-CAM module acting as a low-power edge capture device.
- **The Workflow**:
    - The module remains in a low-power state until triggered.
    - Captures a high-resolution JPEG of the food item.
    - Transmits the image via a secure Base64 POST request to the centralized Flask API.
- **Key Innovation**: Enables "hands-free" logging where the kitchen itself becomes part of the tracking ecosystem.

### 2. Tier 2: The AI Recognition Engine (Deep Learning)
*Developed by the ML & Backend Team*
- **Architecture**: **MobileNetV3Large** utilizing Transfer Learning from ImageNet.
- **Training Strategy**: 
    - Dataset of 100 Indian food classes (Samosa, Biryani, Poha, etc.).
    - Fine-tuned using **Categorical Crossentropy** and **Adam Optimizer**.
    - Optimized with **Post-Training Quantization** to reduce the model size from ~150MB to ~12MB.
- **Performance Output**: 
    - **91% Training Accuracy** / **78% Validation Accuracy**.
    - Optimized for **LiteRT (TFLite)** to ensure sub-200ms inference on cloud servers with limited RAM.

### 3. Tier 3: Interactive Dashboard (Web/PWA)
*Developed by the UI/UX & Frontend Team*
- **Persistent Logic**: Uses LocalStorage and a synced session system to track daily progress.
- **Nutritional Engine**: 
    - Maps 100+ predicted classes to a high-fidelity nutritional database.
    - Calculates macros (Protein, Carbs, Fats) and provides a **Health Score** based on nutrient density.
- **Visual Persistence**: "Today's Meals" log keeps a visual record of scanned images for better user recall.
- **Universal Access**: Built as a Progressive Web App (PWA), ensuring it works on Android, iOS, and Desktop.

---

## 📊 Model Summary & Metrics
| Parameter | Detail |
|-----------|--------|
| **Backbone Network** | MobileNetV3Large |
| **Num Classes** | 100 Indian Dishes |
| **Dataset Volume** | 60,000+ Images |
| **Framework** | TensorFlow 2.15 + LiteRT |
| **Inference Latency** | ~140ms on standard hardware |
| **Memory Footprint** | ~55MB (Operational) |

---

## 🚀 Deployment & Produciton (Review 4 Updates)
This repository contains the **Production-Optimized Build** designed specifically for Render Free Tier (512MB RAM limit):
- **Optimization**: Switched from heavy TensorFlow to `ai-edge-litert` (lite runtime).
- **Environment**: Locked to **Python 3.12.2** for optimized Linux performance.
- **Server**: Configured with **Gunicorn** using asynchronous workers for higher concurrent requests.

---

## 🧭 Future Roadmap
- [ ] **Voice Integration**: Log meals and query calories via voice commands.
- [ ] **Smart Scale Integration**: Connect to IoT weight scales for exact grams of food.
- [ ] **Dietary Recommendations**: AI-driven suggestions based on your remaining macro-budget for the day.

---

## 👥 Meet the Team

| Name | Branch | Core Responsibility |
|------|--------|------|
| **Tanmay** | CSE | AI Model Optimization & Backend Architecture |
| **Rishabh** | CSE | UI Development & Real-time Tracking Logic |
| **Ishaan** | CSE | Dataset Curation & Nutritional Logic |
| **Mokshesh** | CSE | Technical Documentation & Quality Assurance |
| **Moushikka** | VLSI | IoT Hardware Design & ESP32 Integration |

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


