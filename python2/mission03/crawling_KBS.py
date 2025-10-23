# crawling_KBS.py

import requests
from bs4 import BeautifulSoup

def get_headline_news():
    url = 'http://news.kbs.co.kr/news/pc/main/main.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # KBS 뉴스 홈페이지의 헤드라인 뉴스는 일반적으로 기사 제목에 해당하는 태그 및 클래스가 있음
    # 실제로는 브라우저 개발자 도구로 확인 후 'headline' 또는 주요 뉴스 제목 클래스명을 찾아야 함

    # headlines = soup.find_all('div', class_='headline')  # 실제 사이트 내에 있는 클래스를 확인해서 변경하면 됨
    # 헤드라인 뉴스 기사 제목은 <div> 태그 내에 있음
    headlines = soup.find_all('div', class_='main-news-wrapper')  # 가져오고 싶은 내용이 있는 tag와 class를 사용

    headline_list = []
    for item in headlines:
        link = item.find('a')
        if link:
            text = item.get_text(strip=True)
            headline_list.append(text)

    return headline_list

def print_headlines(headline_list):
    for idx, headline in enumerate(headline_list, 1):
        print(f'{idx}. {headline}')

if __name__ == '__main__':
    headlines = get_headline_news()
    print_headlines(headlines)              # 헤드라인 뉴스 내용의 서두 일부 출력
    # print(len(headlines))                   # 헤드라인 뉴스 내용 서두를 가져온 횟수를 출력