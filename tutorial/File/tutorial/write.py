f = open('/tutorial/File/tutorial/example.txt', 'w', encoding='UTF-8')
f.write('테스트글자')
f.write('\n테스트글자1')
f.write('\n테스트글자2')
f.close()

#  w는 새로 열릴 때마다 파일이 덮여쓰여짐
f = open('/tutorial/File/tutorial/example.txt', 'w', encoding='UTF-8')
f.write('테스트글자 -')
f.writelines(["\n월",'\n화','\n수','\n목','\n금'])
f.close()


# a 는 내용르 추가하고 파일이 없으면 새로 생성
f = open('/tutorial/File/tutorial/example.txt', 'a', encoding='UTF-8')

f.writelines(['\n토', '\n일'])
f.close()
