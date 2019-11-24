# 파이썬에서는 with as를 사용하면 파일을 사용한 뒤 자동으로 객체를 닫아줌
# with open(파일이름, 파일모드) as 파일객체
# 코드

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)