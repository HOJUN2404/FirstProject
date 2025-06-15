import crawler.naver  # This is a sample Python script.
import crawler.gpt

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # keyword = input("검색할 키워드를 입력하세요: ")

    # dummy = crawler.naver.get_today_news("삼성전자")

    # GPT 한테 넘겨서 받아온 결과값을 저장해놓자.
    # gpt_result = crawler.gpt.


    # 네이버 뉴스 튜플 담은 리스트로 변환하는 코드
    # news_links = crawler.gpt.get_naver_news_links('삼성전자', 5)
    # print(news_links)

    # 테스트용 뉴스 URL
    # https://www.news1.kr/politics/president/5814189

    test = crawler.gpt.get_article_content('https://www.news1.kr/politics/president/5814189')
    # print(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





