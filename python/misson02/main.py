import csv

# 파일 경로
input_file = "./Mars_Base_Inventory_List.csv"
output_file = "./Mars_Base_Inventory_danger.csv"

try:
    # 파일 읽기
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = [row for row in reader] # 전체 내용을 리스트로 저장

    # 전체 내용 출력
    for row in data:
        print(row)

    # (파이썬에서 csv를 자유롭게 수정하기 위해) 리스트 객체로 변환
    inventory_list = data[1:] # 첫 번째 행(헤더) 제외

    # 인화성 지수가 0.7 이상인 항목 필터링
    header = data[0] # 헤더 저장
    dangerous_items = [row for row in inventory_list if float(row[4]) >= 0.7] # 인화성 지수 0.7 이상

    # 인화성 지수가 높은 순으로 정렬
    dangerous_items.sort(key=lambda x: float(x[4]), reverse=True)

    # 필터링된 목록 출력
    print("\n[ 인화성 지수 0.7 이상 목록 ]")
    
    for row in dangerous_items:
        print(row)

    # 새로운 CSV 파일로 저장
    with open(output_file, "w", encoding="utf-8", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(header) # 헤더 추가
        writer.writerows(dangerous_items) # 데이터 추가

    print(f"\n[ 인화성 지수 0.7 이상 데이터가 '{output_file}'에 저장되었습니다. ]")

except FileNotFoundError:
    print(f"오류: 파일 '{input_file}'을 찾을 수 없습니다.")
except ValueError:
    print("오류: 데이터 변환 중 문제가 발생했습니다.")
except Exception as e:
    print(f"예기치 않은 오류 발생: {e}")

