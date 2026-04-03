
#  Text Summarization App using Transformers

A production-ready **Text Summarization Web Application** that leverages the power of **Transformer-based Deep Learning models (T5)** to generate concise, meaningful summaries from long-form text. This project demonstrates end-to-end integration of **Natural Language Processing (NLP)** with a scalable backend and interactive frontend.

Built with a focus on **real-world applicability**, this system showcases how modern ML models can be deployed as responsive web services.

---

##  Features

-  Abstractive text summarization using **T5 Transformer**
-  High-performance backend powered by **FastAPI**
-  Interactive and user-friendly web interface
-  Real-time text processing and inference
-  Input preprocessing using regex for cleaner outputs
-  Modular and scalable project architecture
-  Ready for deployment (API-first design)

---

##  Tech Stack

**Machine Learning**
- PyTorch  
- Hugging Face Transformers (T5)

**Backend**
- FastAPI  
- Uvicorn  

**Frontend**
- HTML  
- CSS  
- JavaScript  

**Templating & Utilities**
- Jinja2  
- Regex (text preprocessing)

---

##  Project Architecture / Workflow

```text
User Input (Frontend UI)
        ↓
FastAPI Backend Endpoint (/summarize)
        ↓
Text Preprocessing (Regex Cleaning)
        ↓
Tokenizer (T5 Tokenizer)
        ↓
T5 Transformer Model (Inference)
        ↓
Generated Summary
        ↓
Response to Frontend (JSON)
        ↓
Display Output on UI
```

---
## Model Access

Due to GitHub file size limitations, the trained model is not included in this repository.

### Option 1: Download Model Manually

Download the model from the link below and place it in the project root directory:

```
t5_summarizer_model/
```

Download Link: [https://huggingface.co/google-t5/t5-small]

---

### Option 2: Load from Hugging Face (Recommended)

Modify your `app.py` as follows:

```python
model = T5ForConditionalGeneration.from_pretrained("your-username/your-model-name")
tokenizer = T5Tokenizer.from_pretrained("your-username/your-model-name")
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Anamika7320/t5-text-summarization-app.git
cd t5-text-summarization-app
```

### 2. Create Virtual Environment

```bash
conda create -n summarizer python=3.10
conda activate summarizer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
uvicorn app:app
```

Open in browser:

```
http://127.0.0.1:8000
```


---

## Model Details

* Model: T5 (Text-to-Text Transfer Transformer)
* Variant: T5-small
* Framework: Hugging Face Transformers
* Task: Abstractive Summarization
* Input Length: Up to 512 tokens

---





