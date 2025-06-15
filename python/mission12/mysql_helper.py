import mysql.connector  # MySQL Connector/Python 라이브러리
# CSV 파일을 읽고 데이터베이스에 삽입하는 작업을 자동화하는 클래스
import csv  # CSV 파일 읽기 위한 라이브러리     
import os  # 파일 경로 작업을 위한 라이브러리
# MySQLHelper 클래스 = 데이터베이스 연결, 쿼리 실행, 자원 정리 자동화  
import datetime  # 날짜와 시간 작업을 위한 라이브러리   


class MySQLHelper:
    """데이터베이스 작업 자동화 클래스"""
    
    def __init__(self, **config):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
    
    def execute_query(self, query, params=None):
        """쿼리 실행 메서드"""
        try:
            self.cursor.execute(query, params or ())
            return self.cursor
        except mysql.connector.Error as e:
            print(f"쿼리 실행 오류: {e}")
    
    def commit(self):
        """변경사항 커밋"""
        self.connection.commit()
    
    def __del__(self):
        """자원 정리"""
        self.cursor.close()
        self.connection.close()
