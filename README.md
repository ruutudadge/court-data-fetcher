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
