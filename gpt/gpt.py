import json
import google.generativeai as genai

# 🔑 Gemini API 키 입력 (Google AI Studio에서 발급받은 키)
genai.configure(api_key="AIzaSyCETJxavrchZfNN0lTS4LieXxTJSnDhRck")

# 📦 예시 데이터 (네가 준 stock_data 그대로 사용)
stock_data = {
    "ticker": "005930",
    "company_name": "삼성전자",
    "date": "2025-06-28",
    "news": [
        {
            "title": "삼성전자, 반도체 실적 개선 기대",
            "content": "삼성전자의 2분기 실적은 예상보다 양호할 것으로 분석된다.",
            "published_at": "2025-06-27"
        }
    ],
    "metrics": {
        "PER": 14.3,
        "PBR": 1.5,
        "ROE": 10.2,
        "EPS": 3600,
        "BPS": 24000
    }
}

# 🎯 Gemini에 질문하기
def ask_gemini(json_data, user_question):
    system_prompt = "너는 기업 뉴스 및 재무지표를 바탕으로 투자 분석을 해주는 금융 애널리스트야."

    user_prompt = f"""다음은 기업의 기사 및 지표 정보야:

{json.dumps(json_data, indent=2, ensure_ascii=False)}

질문: {user_question}"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=[])
    response = chat.send_message(f"{system_prompt}\n\n{user_prompt}")
    return response.text

# 🚀 실행
if __name__ == "__main__":
    print("Gemini에게 질문할 내용을 입력하세요:")
    question = input(">>> ")

    print("\n📊 Gemini 분석 결과:\n")
    answer = ask_gemini(stock_data, question)
    print(answer)
