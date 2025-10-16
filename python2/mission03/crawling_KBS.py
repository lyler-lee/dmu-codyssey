# crawling_KBS.py

import requests
from bs4 import BeautifulSoup

def get_headline_news():
    url = 'http://news.kbs.co.kr/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # KBS 뉴스 홈페이지의 헤드라인 뉴스는 일반적으로 기사 제목에 해당하는 태그 및 클래스가 있음
    # 실제로는 브라우저 개발자 도구로 확인 후 'headline' 또는 주요 뉴스 제목 클래스명을 찾아야 함
    # 아래 예시는 일반적인 headline 클래스 사용 예시, 반드시 실제 클래스명을 확인할 것

    # headlines = soup.find_all('div', class_='headline')  # 실제 클래스를 확인해서 변경
    # 헤드라인 뉴스 기사 제목은 <a> 태그 내에 있음
    headlines = soup.find_all('a', class_='tit')  # 예시. 실제 사용할 tag/class 확인 후 변경

    headline_list = []
    for item in headlines:
        text = item.get_text(strip=True)
        headline_list.append(text)

    return headline_list

def print_headlines(headline_list):
    for idx, headline in enumerate(headline_list, 1):
        print(f'{idx}. {headline}')

if __name__ == '__main__':
    headlines = get_headline_news()
    print_headlines(headlines)


