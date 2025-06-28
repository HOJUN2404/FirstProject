from rapidfuzz import process

abbreviation_dict = {
    "삼전": "삼성전자",
    "하닉": "SK하이닉스",
    "삼바": "삼성바이오로직스",
    "현차": "현대자동차",
    "카겜": "카카오게임즈",
    "NAVER": "네이버",
    "엘지화학": "LG화학",
    "엘지전자": "LG전자",
    "celtrion": "셀트리온",
    "kakao": "카카오",
    "현바": "현대바이오",
    "KIA": "기아",
    "솔루엠": "솔루엠"
}

company_list = list(set(abbreviation_dict.values()))

def resolve_abbreviation(abbrev):
    if abbrev in abbreviation_dict:
        return abbreviation_dict[abbrev]

    match = process.extractOne(abbrev, company_list, score_cutoff=70)
    if match:
        return match[0]
    
    return abbrev
