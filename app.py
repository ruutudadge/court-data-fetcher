from flask import Flask, render_template, request
from scraper import scrape_case_details

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/fetch", methods=["POST"])
def fetch_case():
    case_type = request.form["case_type"]
    case_number = request.form["case_number"]
    filing_year = request.form["filing_year"]

    result = scrape_case_details(case_type, case_number, filing_year)

    if "error" in result:
        return render_template("index.html", error=result["error"])
    else:
        return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
