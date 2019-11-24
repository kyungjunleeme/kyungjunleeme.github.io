import pickle
with open('james.p', 'rb') as file: #바이너리 읽기모드(rb)
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)

'''
파일에서 파이썬 객체 읽기
- 마찬가지로 파일에서 객체(값)를 가져올 때도 pickle.load를 네 번 사용해야 함
- name, age, address, scores 순으로 저자했으므로 가져올 때도 같은 순서로 가져오면 됨
- 이 순서대로 안하면 출력이 이상하게 됨
'''
'''
파일 모드 조합.png 참고
'''