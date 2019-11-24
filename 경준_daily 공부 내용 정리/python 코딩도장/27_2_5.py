# for 반복문으로 파일의 내용을 줄 단위로 읽기
# 다음은 for 반복문에 파일 객체를 지정하여 줄 단위로 파일의 내용을 읽음
with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))