from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class NaverCrawler:
    def __init__(self, driver_path=None):
        self.driver_path = driver_path
        self.driver = None
        self.wait = None
        self.before_login_contents = []
        self.after_login_contents = []

    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        if self.driver_path:
            self.driver = webdriver.Chrome(self.driver_path, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        # self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.wait = WebDriverWait(self.driver, 15)

    def open_naver_main(self):
        self.driver.get('https://www.naver.com')
        time.sleep(4)

    def collect_before_login_contents(self): # 로그인 전 메인 상단 메뉴 텍스트 수집."""
        self.before_login_contents.clear()
        try:
            # 개발자도구에서 실제 상단 메뉴 중 하나를 선택 후 Copy selector 해서 붙여넣기
            elements = self.driver.find_elements(
                By.CSS_SELECTOR,
                'div#account.Layout-module__content_area___b_3TU'  # 예시: 실제 selector로 교체
            )
            for element in elements:
                text = element.text.strip()
                if text:
                    self.before_login_contents.append(text)
            
            print(self.driver.current_url)
            print('elements 개수:', len(elements))
        
        except Exception as error:
            print(f'로그인 전 콘텐츠 수집 오류: {error}')

    # def collect_before_login_contents(self):
    #     """로그인 전 상단 메뉴 수집"""
    #     try:
    #         nav_elements = self.driver.find_elements(By.CSS_SELECTOR, '#gnb > div.gnb_menu > div.list_menu > ul > li > a')
    #         for element in nav_elements:
    #             text = element.text.strip()
    #             if text and len(text) > 1:
    #                 self.before_login_contents.append(text)
    #     except Exception:
    #         pass

    def go_to_login_page(self):
        """로그인 페이지로 이동"""
        self.driver.get('https://nid.naver.com/nidlogin.login')
        print('로그인 페이지가 열렸습니다. 아이디/비밀번호와 자동입력 방지를 직접 입력한 뒤, 로그인을 눌러 주세요.') # 자동입력 방지 문자는 사람이 직접 입력
        
        time.sleep(50) # 사람이 입력할 시간을 충분히 준다.

    def wait_until_logged_in(self): # 사람이 로그인 버튼을 누른 뒤, 로그인 성공 여부만 확인. 
        # 최대 60초 동안 로그인 성공 여부 확인
        for _ in range(60):
            current_url = self.driver.current_url
            # 로그인 성공 시 nid 도메인을 벗어나 naver.com 등으로 이동
            if 'nid.naver.com' not in current_url:
                print('로그인 성공 감지')
                return True
            time.sleep(1)
        print('로그인 실패 또는 시간 초과')
        return False

    def login(self, user_id, user_password):
        """JavaScript로 직접 입력하여 자동입력 방지 우회"""
        try:
            # JavaScript로 직접 값 입력 (자동입력 방지 우회)
            self.driver.execute_script("""
                document.getElementById('id').value = arguments[0];
                document.getElementById('pw').value = arguments[1];
            """, user_id, user_password)
            
            time.sleep(2)
            
            # 로그인 버튼 클릭
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, 'log.login'))
            )
            login_button.click()
            
            time.sleep(6)
            
            # 로그인 성공 여부 확인
            if 'nid.naver.com' in self.driver.current_url:
                print('로그인 실패: 자동입력 방지 또는 비밀번호 오류')
                return False
            
            print('로그인 성공')
            return True
            
        except Exception as e:
            print(f'로그인 오류: {e}')
            return False

    def collect_after_login_contents(self):
        """로그인 후 실제 보이는 콘텐츠 수집"""
        self.after_login_contents.clear()
        try:
            # 혹시 로그인이 끝난 직후라면 메인으로 한 번 더 이동
            self.driver.get('https://www.naver.com')
            time.sleep(4)

            # 로그인 후에만 보이는 영역의 selector 사용
            elements = self.driver.find_elements(
                By.CSS_SELECTOR,
                'div#account.Layout-module__content_area___b_3TU'
            )
            for element in elements:
                text = element.text.strip()
                if text:
                    self.after_login_contents.append(text)

            print(self.driver.current_url)
            print('elements 개수:', len(elements))

        except Exception as error:
            print(f'로그인 후 콘텐츠 수집 오류: {error}')

    def print_contents(self):
        print('\n=== 로그인 전 콘텐츠 (' + str(len(self.before_login_contents)) + '개) ===')
        for i, content in enumerate(self.before_login_contents[:8], 1):
            print(f'{i:2d}. {content}')
        
        print('\n=== 로그인 후 콘텐츠 (' + str(len(self.after_login_contents)) + '개) ===')
        for i, content in enumerate(self.after_login_contents[:8], 1):
            print(f'{i:2d}. {content}')

    def quit(self):
        if self.driver:
            self.driver.quit()


def main():
    # 수동 로그인으로 대체
    # user_id = ''
    # user_password = ''

    crawler = NaverCrawler()
    crawler.start_driver()
    
    try:
        print('1. 네이버 메인 페이지 접속 중...')
        crawler.open_naver_main()
        
        print('2. 로그인 전 콘텐츠 수집 중...')
        crawler.collect_before_login_contents()     # 로그인 전 로그인 배너 요소 수집
        
        print('3. 로그인 페이지 이동 중...')
        crawler.go_to_login_page()                  # 이 부분에서 직접 로그인
        
        print('4. 로그인 완료 대기 중...')
        if crawler.wait_until_logged_in():
            print('5. 로그인 후 콘텐츠 수집 중...')
            crawler.collect_after_login_contents()  # 로그인 후 로그인 배너 요소 수집
            crawler.print_contents()
        else:
            print('로그인 실패로 크롤링 중단')
            
    except KeyboardInterrupt:
        print('\n사용자 중단')
    except Exception as e:
        print(f'오류 발생: {e}')
    finally:
        crawler.quit()


if __name__ == '__main__':
    main()
