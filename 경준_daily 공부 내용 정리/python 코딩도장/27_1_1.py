# 파일 사용하기
# 파일 객체를 얻은 뒤에 write 메서드를 사용
# 파일 열기 모드에는 r(읽기) , w(쓰기), a(추가) 가 있음
file = open('hello.txt', 'w')
file.write("add")
file.close