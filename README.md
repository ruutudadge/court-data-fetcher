⚖️ Court Data Fetcher & Mini-Dashboard
A sleek legal-tech dashboard to fetch Delhi High Court case details in real-time.


🏛 Overview

Court Data Fetcher provides instant case insights from the Delhi High Court portal:

Parties involved (Petitioner vs Respondent)

Filing dates, next hearings, and case status

Downloadable orders & judgments

Search history with export options


🚀 Features

🔍 Smart Search – Query by case type, number, and year

📄 Case Metadata – Extract parties, dates, and current status

📥 PDF Downloads – Direct access to orders/judgments

🕒 History Tracker – Persistent search log with CSV export

🛡 Captcha-Friendly – Manual solve with Selenium automation

📱 Responsive UI – Mobile-first Bootstrap 5 design


🛠 Tech Stack

Backend: Flask (Python)
Frontend: HTML5, CSS3, Bootstrap 5
Scraping: Selenium WebDriver (Headless Chrome)
Database: SQLite (SQLAlchemy ORM)
Deployment: Docker + Gunicorn on Render


⚡ Quick Setup

bash
Copy
Edit
# Clone repository
git clone <repository-url>
cd court-data-fetcher

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
Access via http://localhost:5000

🐳 Docker Deploy

bash
Copy
Edit
docker build -t court-data-fetcher.
docker run -p 5000:5000 court-data-fetcher
🔌 API Endpoint
GET /api/case-data/<query_id>
Returns JSON with case details (parties, filing date, next hearing, status, etc.).

🧩 Project Structure
csharp
Copy
Edit
Court-Data-Fetcher/
├── app.py
├── requirements.txt
├── templates/       # HTML templates
├── static/          # CSS/JS/images
├── data/            # SQLite database
├── Dockerfile
└── README.md


⚖ Legal & Disclaimer

Fetches public data only

Complies with court website’s terms of service

For educational use — not for spam or misuse

