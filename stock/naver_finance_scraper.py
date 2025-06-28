import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

def get_ticker_by_name(company_name):
    encoded_query = urllib.parse.quote(company_name.encode('euc-kr'))
    url = f"https://finance.naver.com/search/search.naver?query={encoded_query}&endUrl="
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    res.encoding = 'euc-kr'
    html = res.text

    redirect_match = re.search(r"parent\.location\.href\s*=\s*'\/item\/main\.naver\?code=(\d+)'", html)
    if redirect_match:
        return redirect_match.group(1)

    soup = BeautifulSoup(html, "html.parser")
    first_link = soup.select_one("table.tbl_search tbody tr td.tit a")
    if first_link and 'href' in first_link.attrs:
        list_match = re.search(r'code=(\d+)', first_link['href'])
        if list_match:
            return list_match.group(1)

    return None

def get_key_ratios(ticker):
    url = f"https://finance.naver.com/item/main.naver?code={ticker}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    res.encoding = 'euc-kr'
    soup = BeautifulSoup(res.text, "html.parser")

    try:
        per_table = soup.find("table", {"class": "per_table"})
        if not per_table:
            return {"PER": "-", "PBR": "-", "배당률": "-"}
        
        tds = per_table.find_all("td")
        per = tds[0].text.strip() if len(tds) > 0 else "-"
        pbr = tds[2].text.strip() if len(tds) > 2 else "-"
        dvr = tds[4].text.strip() if len(tds) > 4 else "-"

        return {"PER": per, "PBR": pbr, "배당률": dvr}

    except Exception as e:
        print("Error in get_key_ratios:", e)
        return {"PER": "-", "PBR": "-", "배당률": "-"}

def get_all_indicators(ticker):
    url = f"https://finance.naver.com/item/main.naver?code={ticker}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    res.encoding = 'euc-kr'
    soup = BeautifulSoup(res.text, "html.parser")

    indicators = {}

    try:
        tables = soup.select("div.section.cop_analysis div.sub_section table")
        for table in tables:
            for tr in table.select("tbody tr"):
                th = tr.select_one("th")
                td = tr.select_one("td")
                if th and td:
                    label = th.get_text(strip=True)
                    value = td.get_text(strip=True)
                    indicators[label] = value

    except Exception as e:
        print("지표 크롤링 오류:", e)

    return indicators
