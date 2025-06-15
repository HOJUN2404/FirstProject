import crawler.naver  # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    keyword = input("검색할 키워드를 입력하세요: ")

    dummy = crawler.naver.get_today_news("삼성전자")

    # GPT 한테 넘겨서 받아온 결과값을 저장해놓자.
    # gpt_result = crawler.gpt.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/





