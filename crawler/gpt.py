import requests
from bs4 import BeautifulSoup
import openai
from fpdf import FPDF
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🔑 GPT API 키 설정
openai.api_key = 'your-openai-api-key-here'

# ✅ 1. 뉴스 제목 & 링크 크롤링
def get_naver_news_links(keyword, max_count=5):
    query = urllib.parse.quote(keyword)
    url = f"https://search.naver.com/search.naver?where=news&query={query}&sort=1&pd=1"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    articles = soup.select('a > span.sds-comps-text-type-headline1')
    news = []

    for span in articles[:max_count]:  # 최대 max_count개까지만 수집
        title = span.text.strip()
        # print("title : ", title)
        link = span.find_parent('a').get('cru') or span.find_parent('a').get('href')
        # print("link : ", link)
        if title and link:
            news.append((title, link))  # 리스트에 튜플로 추가
    return news


# ✅ 2. 본문 크롤링 (사이트별 구조가 달라 단순히 <p> 태그 추출)
def get_article_content(url):
    try:
        # 브라우저 열기
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # 창 안 띄우는 모드
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL 접속
        driver.get(url)
        time.sleep(3)  # JS 로딩 기다리기

        # HTML 파싱
        soup = BeautifulSoup(driver.page_source, "html.parser")
        paragraphs = soup.find_all("p")

        # 본문 텍스트 출력
        for p in paragraphs:
            print(p.get_text(strip=True))

        driver.quit()
    except:
        return ""

# ✅ 3. GPT에게 요약 요청
def summarize_with_gpt(news_texts):
    combined = "\n\n".join(news_texts)
    prompt = f"""다음 뉴스 기사 내용을 종합해서 한글로 요약해줘. 중요한 키워드와 흐름 중심으로 정리해줘:\n\n{combined}"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()

# ✅ 4. PDF 저장
def save_to_pdf(text, filename="뉴스_요약.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)
    print(f"✅ PDF로 저장 완료: {filename}")

# ✅ 전체 파이프라인 실행
def full_pipeline(keyword):
    print(f"🔍 '{keyword}' 키워드로 뉴스 수집 중...")
    news_items = get_naver_news_links(keyword)

    news_contents = []
    for title, link in news_items:
        print(f"📰 {title} -> {link}")
        content = get_article_content(link)
        if content:
            news_contents.append(content)
        time.sleep(1)  # 네이버/언론사 서버에 부담 줄이기

    if not news_contents:
        print("❌ 뉴스 본문을 가져오지 못했어요.")
        return

    print("\n🤖 GPT에게 요약 요청 중...")
    summary = summarize_with_gpt(news_contents)
    print("\n📝 요약 결과:\n", summary)

    print("\n📄 PDF로 저장 중...")
    save_to_pdf(summary)





# 🚀 실행 예시
if __name__ == "__main__":
    keyword = input("검색할 키워드를 입력하세요: ")
    full_pipeline(keyword)
