from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_case_details(case_type, case_number, filing_year):
    """
    Scrapes case details from eCourts using Selenium and webdriver-manager.
    """

    # Configure Chrome options
    chrome_options = Options()
    # Comment next line if you want to see the browser window (needed for captcha)
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")


    # Initialize driver with webdriver-manager
    chrome_options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open eCourts website
        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")

        # TODO: Navigate to "Case Status" page (depends on website)
        # Example (replace with actual selectors):
        # driver.find_element(By.LINK_TEXT, "Case Status").click()
        # time.sleep(2)

        # Fill form fields (replace IDs with actual ones from website)
        driver.find_element(By.ID, "case_type").send_keys(case_type)
        driver.find_element(By.ID, "case_number").send_keys(case_number)
        driver.find_element(By.ID, "filing_year").send_keys(filing_year)

        # Pause for manual captcha solving
        print("Solve the captcha in the browser window, then press Enter here...")
        input()

        # Submit form (replace with actual submit button ID)
        driver.find_element(By.ID, "submit_button_id").click()

        # Wait for results page to load
        time.sleep(5)

        # Extract details (replace with actual IDs)
        petitioner = driver.find_element(By.ID, "petitioner").text if driver.find_elements(By.ID, "petitioner") else "Not Found"
        respondent = driver.find_element(By.ID, "respondent").text if driver.find_elements(By.ID, "respondent") else "Not Found"
        filing_date = driver.find_element(By.ID, "filing_date").text if driver.find_elements(By.ID, "filing_date") else "Not Found"
        next_hearing = driver.find_element(By.ID, "next_hearing").text if driver.find_elements(By.ID, "next_hearing") else "Not Found"

        return {
            "petitioner": petitioner,
            "respondent": respondent,
            "filing_date": filing_date,
            "next_hearing": next_hearing,
            "raw_html": driver.page_source  # Optional: store full HTML
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()
