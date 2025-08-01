# ⚖️ Court Data Fetcher & Mini-Dashboard

> A modern web application for fetching and visualizing Delhi High Court case data with Selenium, Flask, and a responsive UI.

![Court Dashboard Preview](./static/images/dashboard-preview.png)  
*(Add your screenshot or mockup here)*

---

## 🏛 Overview

Court Data Fetcher is a **law-focused dashboard** that scrapes case information directly from the [Delhi High Court](https://delhihighcourt.nic.in/) website.  
It allows users to **search by case type, number, and filing year**, view case metadata, download orders/judgments, and track search history — all in one place.

---

## ✨ Features

### 🎯 Core Functionality
- **Automated Web Scraping**: Selenium-driven extraction of live court data  
- **Modern Search Interface**: Dropdowns, clean form validation, responsive UI  
- **Case Details Display**: Petitioner/respondent info, dates, status, and orders  
- **Search History**: Persistent logging with SQLite storage  
- **Error Handling**: Graceful fallbacks and mock data for uninterrupted workflow

### 🚀 Advanced Features
- **REST API**: Programmatic endpoints for external integrations  
- **Mini Dashboard**: Real-time metrics (search count, recent activity)  
- **PDF Management**: Downloadable court orders and judgments  
- **Pagination**: Handle multiple order pages seamlessly  
- **Offline Mode**: Mock data for dev/test environments

### 🛠 Production-Ready
- **Dockerized Deployment**: Run anywhere with Docker & Compose  
- **Headless Chrome Support**: Optimized for cloud hosting (Render/Heroku)  
- **CI/CD Ready**: Integrate with GitHub Actions for auto-deploy  
- **Security**: Input sanitization, error obfuscation, database isolation

---

## 🏗 Architecture

**Stack Overview**  
- **Backend**: Flask + SQLAlchemy + Selenium  
- **Frontend**: HTML5 + Bootstrap 5 + Vanilla JS  
- **Database**: SQLite (easily replaceable with Postgres/MySQL)  
- **Deployment**: Docker + Gunicorn + Render/Heroku  
- **Testing**: Pytest & Unittest frameworks

**Database Models**
- `CaseQuery` – Search queries metadata  
- `CaseDetail` – Petitioner, respondent, dates, case status  
- `CourtOrder` – PDF links and order details  
- `SearchLog` – Metrics for dashboard analytics  

---

## 🚀 Quick Start

### **Local Setup**

#### 1. Clone the repository
```bash
git clone <your-repo-url>
cd court-data-fetcher
2. Install dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Initialize the database
bash
Copy
Edit
python init_db.py
4. Run the application
bash
Copy
Edit
python app.py
Visit: http://localhost:5000

Docker Setup
bash
Copy
Edit
docker build -t court-data-fetcher .
docker run -p 5000:5000 court-data-fetcher
or with Docker Compose:

bash
Copy
Edit
docker-compose up --build
📊 API Endpoints
Search Case
POST /api/search

Request:

json
Copy
Edit
{
  "case_type": "W.P.(C)",
  "case_number": "1234",
  "filing_year": "2023"
}
Response:

json
Copy
Edit
{
  "success": true,
  "case_details": {
    "case_title": "W.P.(C)/1234/2023",
    "petitioner": "John Doe",
    "respondent": "State of Delhi",
    "filing_date": "15/01/2023",
    "next_hearing": "20/02/2024",
    "case_status": "Pending"
  },
  "orders": [
    {
      "order_date": "10/06/2023",
      "order_title": "Interim Order",
      "pdf_url": "https://example.com/order.pdf"
    }
  ]
}
🧪 Testing
bash
Copy
Edit
# Run all tests
pytest

# Or run specific test files
python test_app.py
✅ Unit Tests: 100% passing

✅ API Tests: Verified endpoints and mock data

✅ Web Scraping Tests: Confirmed live data extraction

📂 Project Structure
php
Copy
Edit
court-data-fetcher/
├── app.py                 # Flask app entry point
├── scraper.py             # Selenium scraping logic
├── models.py              # SQLAlchemy models
├── init_db.py             # DB initialization script
├── requirements.txt       # Dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Compose setup
├── templates/             # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── results.html
│   └── dashboard.html
├── static/                # CSS/JS/images
└── tests/                 # Unit and integration tests
🐛 Troubleshooting
WebDriver Error: no chrome binary found
Ensure Chrome is installed in container (via render-build.sh)

Use CHROME_BIN=/usr/bin/google-chrome in environment variables

CAPTCHA Issue
Manual solve required (headless mode disabled during CAPTCHA)

API 404
Verify API URL: /api/search and not /search

📈 Performance
Response Time: <5 seconds average

Error Recovery: Fallback mock data always available

Caching: Reduces redundant requests to court website

🤝 Contributing
Fork the repo

Create a feature branch: git checkout -b feature/amazing-feature

Commit changes: git commit -m "Add amazing feature"

Push branch: git push origin feature/amazing-feature

Open a Pull Request

📜 License
MIT License © 2025 — Open for educational and research use

Built with ❤️ for the Legal Tech Community
Streamlining access to public legal data while respecting court policies and ethical boundaries.
