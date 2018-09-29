

# Assignment Number... : 9
# Student Name........ : 이택윤
# File Name........... : hw9_이택윤
# Program Description. : 이것은 csv파일을 불러와 읽고 txt파일을 파싱하는 방법을 적용해보는 과제입니다. 

file = open('C:/Users/renz/Desktop/python/cars.csv',mode= 'r', encoding = 'utf-8')   # open()함수를 이용하여 cars.csv파일을 읽어옵니다.     
for line in file :                                                                   # for문을 돌려서 cars.csv 파일의 각 줄을 출력합니다. 
    print(line)
    
file = open('C:/Users/renz/Desktop/python/cars.csv',mode= 'r', encoding = 'utf-8')   # open()함수를 이용하여 cars.csv파일을 읽어옵니다.
a = []                                                                               # 빈 리스트를 생성하고 for문을 돌면서 각 라인을 ','기준으로 분리한 뒤
for line in file : 
       a.append(tuple(line.split(',')))                                              # ','기준으로 분리된것을 튜플로만들고 그것들을 리스트에 추가한다.
print(a)

file = open('C:/Users/renz/Desktop/python/My way.txt', mode='r', encoding ='utf-8')  # open()함수를 이용하여 My way.txt 파일을 읽어옵니다.
for line in file :                                                                   # for문을 돌려서 My way.txt 파일의 각 줄을 출력합니다.
    print(line)
    
file = open('C:/Users/renz/Desktop/python/My way.txt', mode='r', encoding ='utf-8')  # open()함수를 이용하여 My way.txt 파일을 읽어옵니다.
b = []                                                                               # 빈 리스트를 생성하고 for문을 돌면서 각 행의 내용을 리스트 요소로 저장합니다.
for line in file : 
       b.append(line)
print(b[2])                                                                          # 리스트에서 3번째 요소를 출력합니다.

file = open('C:/Users/renz/Desktop/python/My way.txt', mode='a', encoding ='utf-8')  # open()을 이용하고 mode ='a'를 이용하여 문구를 기존에 있던 것에서 추가 입력한다.  
file.write('\nI\'ll state my case, of which I\'m certain')                           # write()를 이용해 추가문구 입력
file.close()                                                                   
file = open('C:/Users/renz/Desktop/python/My way.txt', mode='r', encoding ='utf-8')
print(file.read())                                                                   # read()함수를 이용하여 전체 내용을 출력합니다.

