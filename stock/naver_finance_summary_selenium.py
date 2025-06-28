from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_financial_summary_by_selenium(ticker):
    url = f"https://finance.naver.com/item/coinfo.naver?code={ticker}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    fin_summary = soup.select_one("table#finSummary")
    if not fin_summary:
        return None

    data = {}
    for tr in fin_summary.select("tbody tr"):
        tds = tr.find_all("td")
        if len(tds) < 2:
            continue
        key = tds[0].get_text(strip=True)
        val = tds[1].get_text(strip=True)
        data[key] = val

    return data
