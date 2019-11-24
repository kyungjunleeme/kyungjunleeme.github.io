# 리스트 들어있는 문자열을 파일에 쓰기
lines = ['안녕하세요.\n', '파이썬\n', '코딩도장입니다.\n']
with open('hello.txt', 'w') as file:
    file.writelines(lines)