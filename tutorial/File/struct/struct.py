import struct

# int , float, float 수치데이터를 바이트로 변환
data = struct.pack('iff', 1,5.5,-10.10,)
print(data)

# 바이트 데이터를 수치데이터로 변환
(x,y,z) = struct.unpack('iff',data)
print(x,y,z)

name = 'hong'
name_bytes = name.encode() # 바이트로 전환
print(name_bytes)
name_data = struct.pack('i', len(name_bytes)) + name_bytes

age,height,weight = 27,180,70
num_data = struct.pack('iff', age, height, weight)
data_b = name_data+ num_data

with open('/tutorial/File/struct/복합데이터.bin','wb') as f :
    f.write(data_b)

with open('/tutorial/File/struct/복합데이터.bin','rb') as f :
    data = f.read()