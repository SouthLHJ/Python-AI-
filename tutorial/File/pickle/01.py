import pickle



data = {}
data[1] = {'no' : 1, 'name':'홍길동', 'address' : '광주시', 'age' : 30}
data[2] = {'no' : 2, 'name':'임꺽정', 'address' : '전주시', 'age' : 34}

print(data)

# 데이터를 통째로 바이너리 파일에 저장
with open('./tutorial/File/pickle/picke01.p','wb') as f :
    pickle.dump(data,f)

# 바이너리 파일을 읽어와서 원래의 자료형으로 반환
with open('./tutorial/File/pickle/picke01.p','rb') as f :
    data_r = pickle.load(f)

print(data_r)

