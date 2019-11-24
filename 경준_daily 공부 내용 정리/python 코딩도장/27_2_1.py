# https://wikidocs.net/26
# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
with open('hello.txt', 'w') as file:
    for i in range(7, 14):
        file.write('hello, world! {}\n'.format(i))