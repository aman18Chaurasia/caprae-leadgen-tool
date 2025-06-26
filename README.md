A 5-hour prototype designed for Caprae Capital's AI Readiness Challenge. This tool scrapes company data, enriches it using business logic, and scores the lead based on high-level sales intelligence factors.

---

## ⚙️ Setup Instructions
```bash
git clone <your-repo-url>
cd leadgen_tool_caprae
pip install -r requirements.txt
```

### Start Backend:
```bash
uvicorn src.app:app --reload
```

### Start Frontend:
```bash
streamlit run src/ui.py
```

---

## 📦 Features
- Input: Company domain (e.g., `example.com`)
- Output: Structured business lead profile
- Fields: Name, LinkedIn, Description, Industry, Size, Stage, Score
- Modular structure, API-ready backend

---

## 🧠 Tech Stack
- **FastAPI** – backend API
- **Streamlit** – frontend UI
- **BeautifulSoup** – (placeholder for real scraping)
- **Mocked Enrichment** – upgrade to Clearbit, Hunter.io, Apollo APIs

---

## 📁 Directory Structure
```
leadgen_tool_caprae/
├── src/
│   ├── app.py         # FastAPI app
│   ├── scraper.py     # Scraper logic
│   ├── enrich.py      # Enrichment logic
│   └── ui.py          # Streamlit frontend
├── README.md
```

---

## 📑 Evaluation-Ready Highlights
- Focused on **business alignment**: prioritizes lead scoring
- Simple, elegant **UI/UX** with Streamlit
- **Expandable architecture** to plug in real enrichment APIs

---

## 📄 Report
See `report.md` for project rationale, approach, and next steps.

---

### Author: Aman Chaurasia