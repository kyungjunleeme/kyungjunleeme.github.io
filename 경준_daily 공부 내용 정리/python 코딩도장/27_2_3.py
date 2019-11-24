# 파일의 내용을 한 줄씩 리스트로 가져오기
# read는 파일의 내용을 읽어서 문자열로 가져오지만 readlines는
# 파일의 내용을 한 줄씩 리스트 형태로 가져옴
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)