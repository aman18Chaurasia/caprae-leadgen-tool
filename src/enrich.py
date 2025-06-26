import random

def enrich_lead(domain):
    # Simulated enrichment logic (replace with Clearbit/Hunter.io)
    return {
        "industry": "Software",
        "employee_count": random.randint(10, 500),
        "funding_stage": random.choice(["Seed", "Series A", "Series B"]),
        "score": random.randint(60, 95)
    }