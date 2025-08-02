from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def scrape_case_details(case_type, case_number, filing_year):
    chrome_options = Options()
    chrome_options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/google-chrome")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(os.getenv("CHROME_DRIVER_PATH", "/usr/bin/chromedriver"))
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")

        # Example: Click "Case Status" (update selector if needed)
        # driver.find_element(By.LINK_TEXT, "Case Status").click()
        # time.sleep(2)

        # Fill case details (replace IDs with actual ones after inspecting the site)
        driver.find_element(By.ID, "case_type").send_keys(case_type)
        driver.find_element(By.ID, "case_number").send_keys(case_number)
        driver.find_element(By.ID, "filing_year").send_keys(filing_year)

        # Wait for manual captcha solving
        print("Solve captcha manually in Chrome window (not possible in headless).")
        input("Press Enter after solving captcha...")

        driver.find_element(By.ID, "submit_button_id").click()
        time.sleep(5)

        petitioner = driver.find_element(By.ID, "petitioner").text if driver.find_elements(By.ID, "petitioner") else "Not Found"
        respondent = driver.find_element(By.ID, "respondent").text if driver.find_elements(By.ID, "respondent") else "Not Found"
        filing_date = driver.find_element(By.ID, "filing_date").text if driver.find_elements(By.ID, "filing_date") else "Not Found"
        next_hearing = driver.find_element(By.ID, "next_hearing").text if driver.find_elements(By.ID, "next_hearing") else "Not Found"

        return {
            "petitioner": petitioner,
            "respondent": respondent,
            "filing_date": filing_date,
            "next_hearing": next_hearing
        }

    finally:
        driver.quit()
