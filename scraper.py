from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_case_details(case_type, case_number, filing_year):
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/google-chrome"  # <-- IMPORTANT
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open eCourts portal directly
        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")

        # Example: Click "Case Status" (update selector if needed)
        # driver.find_element(By.LINK_TEXT, "Case Status").click()
        # time.sleep(2)

        # Fill case details (replace IDs with real ones after inspecting eCourts site)
        driver.find_element(By.ID, "case_type").send_keys(case_type)
        driver.find_element(By.ID, "case_number").send_keys(case_number)
        driver.find_element(By.ID, "filing_year").send_keys(filing_year)

        # Wait for captcha solving
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
            "next_hearing": next_hearing,
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()
