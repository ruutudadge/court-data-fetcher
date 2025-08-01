# Court Data Fetcher (Delhi High Court) – Demo Mode

A Flask web app that demonstrates Delhi High Court case search using **mock data** (no live scraping).  
Later, replace mock data with real Playwright-based scraping.

---

## Features
- Search by **Case Type, Case Number, Filing Year**
- Returns **Parties, Filing Date, Next Hearing, Latest Order**
- Mock mode enabled (no CAPTCHA issues)
- SQLite logs queries
- Ready for **Render Deployment**

---

## Local Setup

```bash
pip install -r requirements.txt
python app.py
"# court-data-fetcher" 
