"""main.py - 파일을 읽고 인사를 출력하는 메인 실행 모듈입니다."""

from hello import say_hello

def read_file(filename):
    """지정된 파일을 utf-8로 읽고 내용을 반환합니다."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    say_hello("github actions")
