import mysql.connector
import csv
from mysql_helper import MySQLHelper  # MySQLHelper 클래스가 정의된 파일을 임포트
# Mars Weather 데이터베이스에 CSV 데이터를 삽입하는 스크립트

def create_connection():
    """MySQL 데이터베이스 연결 생성"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # 사용자 환경에 맞게 수정
            password='',  # 실제 패스워드 입력 필요
            database='mars_db'  # 미리 생성된 데이터베이스
        )
        return conn
    except mysql.connector.Error as e:
        print(f"데이터베이스 연결 오류: {e}")
        return None

def create_table(conn):
    """mars_weather 테이블 생성 함수"""
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS mars_weather (
        weather_id INT AUTO_INCREMENT PRIMARY KEY,
        mars_date DATETIME NOT NULL,
        temp INT,
        storm INT
    )
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        print("테이블 생성 완료")
    except mysql.connector.Error as e:
        print(f"테이블 생성 실패: {e}")

def insert_data(conn, data):
    """CSV 데이터 삽입 함수"""
    insert_query = '''
    INSERT INTO mars_weather (mars_date, temp, storm)
    VALUES (%s, %s, %s)
    '''
    try:
        cursor = conn.cursor()
        cursor.executemany(insert_query, data)
        conn.commit()
        print(f"{cursor.rowcount}개 레코드 삽입 성공")
    except mysql.connector.Error as e:
        print(f"데이터 삽입 실패: {e}")
        conn.rollback()

def read_csv_file(filename):
    """CSV 파일 읽기 함수"""
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # 헤더 스킵
            for row in reader:
                # 날짜 형식 변환 필요시 추가 처리
                data.append((row[0], int(row[1]), int(row[2])))
        return data
    except FileNotFoundError:
        print("CSV 파일을 찾을 수 없습니다")
        return []
    except ValueError as e:
        print(f"데이터 형식 오류: {e}")
        return []

def main():

    db = MySQLHelper(host='localhost', user='root', password='', database='mars_db')
    # db.execute_query(...) 등 추가 기능 사용 시 mySQLHelper 클래스 활용

    """메인 실행 함수"""
    conn = create_connection()
    if not conn:
        return

    create_table(conn)
    
    csv_data = read_csv_file('mars_weathers_data.csv')
    if csv_data:
        insert_data(conn, csv_data)
    
    conn.close()

if __name__ == "__main__":
    main()
