from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)


if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

#  MODEL (LOAD ON STARTUP) 
model = None
tokenizer = None

@app.on_event("startup")
def load_model():
    global model, tokenizer
    model = T5ForConditionalGeneration.from_pretrained("./t5_summarizer_model")
    tokenizer = T5Tokenizer.from_pretrained("./t5_summarizer_model")
    model.to(device)
    print("Model loaded successfully")

#  TEMPLATES 
from jinja2 import Environment, FileSystemLoader

templates_env = Environment(
    loader=FileSystemLoader("templates"),
    cache_size=0  
)

#  INPUT MODEL 
class DialogueInput(BaseModel):
    dialogue: str

#  CLEANING FUNCTION 
def clean_data(text):
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = text.strip().lower()
    return text

#  SUMMARIZATION FUNCTION 
def summarize_dialogue(dialogue: str) -> str:
    dialogue = clean_data(dialogue)

    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(targets[0], skip_special_tokens=True)
    return summary

# API ROUTES 
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)
    return {"summary": summary}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = templates_env.get_template("index.html")
    return HTMLResponse(template.render()) 