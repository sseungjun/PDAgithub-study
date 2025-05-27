"""main.py - 간단한 파일 입출력을 수행하는 모듈입니다."""

def say_hello(name):
    print("Hello,", name)

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    say_hello("github actions")
