str, secStr = '',''

while True : 
    line = input('암호화할 메시지 ==>')
    if line == '':
        break
    else :
        str += line + '\n'

def convertSecret(word, reverse = False) : 
    """
        문자열 암호화 함수
    """
    if reverse :
        convert =''
        for alpa in word :
            num = ord(alpa)
            num -= 100
            convert += chr(num)
            
        return convert
    
    else :
        convert =''
        for alpa in word :
            num = ord(alpa)
            num += 100
            convert += chr(num)
            
        return convert
        
        

secStr = convertSecret(str)

with open('./File/tutorial/secret_text.txt','w',encoding='UTF-8') as f:
    f.write(secStr)

with open('./File/tutorial/secret_text.txt','r',encoding='UTF-8') as f:
    read_secStr = f.read()
    
rev_str = convertSecret(read_secStr,True)    

print(rev_str)
    



        