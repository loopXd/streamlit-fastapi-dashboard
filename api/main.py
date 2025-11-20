from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

relatorio = [
    {"mes": "Janeiro", "vendas": 120},
    {"mes": "Fevereiro", "vendas": 90},
    {"mes": "Março", "vendas": 150},
]

@app.get("/dados")
def get_dados():
    return relatorio
