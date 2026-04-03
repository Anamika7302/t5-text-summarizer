
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