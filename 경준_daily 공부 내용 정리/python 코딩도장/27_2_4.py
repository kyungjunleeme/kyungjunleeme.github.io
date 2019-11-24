# 파일의 내용을 한 줄씩 읽기
# 만약 파일의 내용을 한 줄씩 순차적으로 읽으려면 readline을 사용함
with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

# 파일에 문자열이 몇 줄이나 있는지 모르기 때문에 readline으로 파일을 읽을 때는
# while 반복문을 활용해야 함
# line을 None이 아닌 ''로 초기화하면 처음부터 line != ''는 거짓이 됨