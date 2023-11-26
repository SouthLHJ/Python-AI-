# 바이너리로 읽어오기
with open('./File/tutorial/code.png','rb') as f:
    data = f.read()
# 바이너리로 파일 쓰기
with open('./File/tutorial/code2.png','wb') as f:
    f.write(data)
    
# 바이너리로 파일 쓰기
str = '안녕하세요 텍스트입니다.'
with open('./File/tutorial/binary_text.txt', 'wb') as f:
    f.write(str.encode())
    
    
    