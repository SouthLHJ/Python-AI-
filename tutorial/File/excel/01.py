# csv 데이터 읽어오기
import csv

with open('./tutorial/File/excel/zzzzz.csv','r', encoding='UTF-8') as f :
    data=csv.reader(f)
    # for line in data :
        # print(line)
    data_list = list(data)

print(data_list)
    