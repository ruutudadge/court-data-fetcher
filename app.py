from flask import Flask, render_template, request
from scraper import scrape_case_details
from db import log_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=["POST"])
def result():
    case_type = request.form["case_type"]
    case_number = request.form["case_number"]
    filing_year = request.form["filing_year"]

    # Scrape details using Selenium
    data = scrape_case_details(case_type, case_number, filing_year)

    # Handle errors
    if "error" in data:
        return render_template("result.html", error=data["error"])

    # Log query into database
    log_query(case_type, case_number, filing_year, data.get("raw_html", ""))

    # Render result page with details
    return render_template("result.html", **data)

if __name__ == "__main__":
    app.run(debug=True)
