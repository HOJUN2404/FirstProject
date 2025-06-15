import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_today_news(keyword):

    # 네이버 뉴스 화면에서 검색 요청했을 때 뜨는 화면 URL
    url = f"https://search.naver.com/search.naver?where=news&query={keyword}&sort=1&pd=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []

    articles_title = soup.select('a > span.sds-comps-text-type-headline1')

    for span in articles_title:

        title = span.text.strip()

        parent_a = span.find_parent('a')
        if parent_a:
            # 링크는 보통 네이버 redirect URL이지만, cru 속성에 실제 URL 있음
            link = parent_a.get('cru') or parent_a.get('href')
            if title and link:
                news_items.append((title, link))

    print(news_items[0][0])

    return news_items



