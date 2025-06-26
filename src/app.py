from fastapi import FastAPI
from src.scraper import scrape_data
from src.enrich import enrich_lead
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/leadgen")
def get_lead(domain: str):
    scraped = scrape_data(domain)
    enriched = enrich_lead(domain)
    lead = {**scraped, **enriched}
    return lead