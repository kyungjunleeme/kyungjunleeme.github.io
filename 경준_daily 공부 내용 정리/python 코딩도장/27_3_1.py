'''
파이썬 객체를 파일에 저장하기, 가져오기
파이썬은 객체를 파일에 저장하는 pickle 모듈을 제공함
다음과 같이 파이썬 객체를 파일에 저장하는 과정을 피클링(pickling)이라고 하고, 
파일에서 객체를 읽어오는 과정을 언피클링(unpickling)이라고 함
'''
import pickle
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 80, 'math': 70}

with open('james.p', 'wb') as file: #바이너리 쓰기 모드(wb) 바이너리 파일은 컴퓨터가 처리하는 파일 형식임
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
