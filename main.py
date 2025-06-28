#import crawler.naver  # This is a sample Python script.
#import crawler.gpt
from stock.abbreviation_resolver import resolve_abbreviation
from stock.naver_finance_scraper import get_ticker_by_name, get_key_ratios, get_all_indicators
from stock.naver_finance_summary_selenium import get_financial_summary_by_selenium


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    # keyword = input("검색할 키워드를 입력하세요: ")

    # dummy = crawler.naver.get_today_news("삼성전자")

    # GPT 한테 넘겨서 받아온 결과값을 저장해놓자.
    # gpt_result = crawler.gpt.


    # 네이버 뉴스 튜플 담은 리스트로 변환하는 코드
    # news_links = crawler.gpt.get_naver_news_links('삼성전자', 5)
    # print(news_links)

    # 테스트용 뉴스 URL
    # https://www.news1.kr/politics/president/5814189

    #test = crawler.gpt.get_article_content('https://www.news1.kr/politics/president/5814189')
    # print(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#종목 stock info
def resolve_and_show(input_name):

    name = resolve_abbreviation(input_name)

    ticker = get_ticker_by_name(name)
    if not ticker:
        print(f"'{name}'의 종목코드를 찾을 수 없습니다.")
        return

    #ratios = get_key_ratios(ticker)

    all_indicators = get_all_indicators(ticker)

    #fin_summary = get_financial_summary_by_selenium(ticker)
    '''
    print("\n기업 정보 요약")
    print(f"기업명     : {name}")
    print(f"종목코드   : {ticker}")
    print(f"PER        : {ratios['PER']}")
    print(f"PBR        : {ratios['PBR']}")
    print(f"배당률     : {ratios['배당률']}")
    '''
    print("\n전체 투자지표")
    if all_indicators:
        for k, v in all_indicators.items():
            print(f"{k:15}: {v}")
    else:
        print("전체 투자지표 정보를 가져올 수 없습니다.")

    '''print("\n재무요약 정보")
    if fin_summary:
        for k, v in fin_summary.items():
            print(f"{k:15}: {v}")
    else:
        print("재무요약 정보를 가져올 수 없습니다.")
    '''
if __name__ == "__main__":
    print("줄임말 또는 기업명을 입력하세요. (종료: q)")
    while True:
        user_input = input("입력: ").strip()
        if user_input.lower() == 'q':
            break
        if not user_input:
            continue
        resolve_and_show(user_input)
