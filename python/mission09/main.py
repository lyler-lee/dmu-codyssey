
def caesar_cipher_decode(target_text):
    """암호문을 자리수 기반 시저 암호로 복호화하는 함수"""
    decrypted_list = []
    for shift_key in range(26):
        decrypted = []
        for idx, char in enumerate(target_text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift = (shift_key + idx) % 26
                new_ord = (ord(char) - base - shift) % 26
                decrypted.append(chr(new_ord + base))
            else:
                decrypted.append(char)
        decrypted_list.append(''.join(decrypted))
    return decrypted_list


def main():
    """메인 실행 함수"""
    try:
        with open('password.txt', 'r', encoding='utf-8') as file:
            cipher_text = file.read().strip()
    except FileNotFoundError:
        print("Error: password.txt 파일을 찾을 수 없습니다")
        return
    except Exception as e:
        print(f"파일 읽기 오류: {str(e)}")
        return

    decrypted_options = caesar_cipher_decode(cipher_text)

    print("\n[복호화 옵션]")
    
    for key, text in enumerate(decrypted_options):
        print(f"{key:2d}: {text}")

    try:
        selected_key = int(input("\n올바른 키 번호 입력(0-25): "))
        if not 0 <= selected_key < 26:
            raise ValueError
    except ValueError:
        print("잘못된 입력: 0~25 사이 정수만 가능합니다")
        return

    try:
        with open('result.txt', 'w', encoding='utf-8') as file:
            file.write(decrypted_options[selected_key])
        print("result.txt 파일 저장 완료")
    except Exception as e:
        print(f"파일 저장 오류: {str(e)}")

if __name__ == "__main__":
    main()
