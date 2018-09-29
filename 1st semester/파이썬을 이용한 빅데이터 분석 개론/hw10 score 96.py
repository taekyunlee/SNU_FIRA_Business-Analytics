# Assignment Number... : 10
# Student Name........ : 이택윤
# File Name........... : hw10_이택윤
# Program Description. : 이것은 파일을 열고 자료를 처리하는 과제입니다.

file = open('C:/users/renz/Desktop/python/subway.txt', mode= 'r' , encoding ='utf-8')  # open()을 이용하여 파일을 읽어옵니다.   
lines = file.readlines()     # readlines()를 이용하여 각 행을 문자열 자료형으로 가지는 리스트를 lines에 선언합니다.
file.close()                 # 파일을 닫는다. 

subway_data = []             # 리스트 변수 subway_data 선언

for i in range(1,len(lines)) :   # for문을 돌면서 lines원소 각각을 ','기준으로 구분하고 각각의 key에대한 값으로서 집어넣는다.   
                                 # append()를 이용하여 subway_data에 계속해서 추가한다.
    subway_data.append({'날짜': lines[i].split(',')[0], '요일':lines[i].split(',')[1],  '구분' :lines[i].split(',')[2],           
                           '7': int(lines[i].split(',')[3]), '8'  :int(lines[i].split(',')[4]),    '9'  :int(lines[i].split(',')[5]),
                          '10': int(lines[i].split(',')[6]), '11' : int(lines[i].split(',')[7].rstrip())})
    
print('******************************* 테스트 1 *******************************')    
print('월요일의 승하차 정보만 모은 목록') 
print()

mon =[]      # 리스트 변수 mon 선언                     
for i in range(len(subway_data)) :    # for문을 돌면서 조건문을 통해 월요일의 승하차 정보만 mon에 모아서 한번에 출력한다.
        
       if subway_data[i]['요일'] == '월' :
            mon.append(subway_data[i])
print(mon)                            
print()                               # 한 줄 띄워준다.
        
print('******************************* 테스트 2 *******************************') 
print('가장 많은 승차 인원수를 기록한 날의 날짜와 요일 시간 그리고 인원수를 출력')
print()

get = []        # 리스트 변수 get 선언      
for i in range(len(subway_data)) :       # for문을 돌면서 각 날짜별로 '승차'에 대한 정보만 get에 모은다. 
       if subway_data[i]['구분'] =='승차' :
            get.append(subway_data[i]) 

extract = []   # 리스트 변수 extract 선언                    
for i in range(len(get)) :               # for문을 돌면서 각 날짜별로 최대인원수를 기록한 자료의 정보만 모은다.
     extract.append({'날짜' : get[i]['날짜'] , '요일' :get[i]['요일'] , 
                     '시간' : sorted(sorted(get[i].items())[0:5], key = lambda x : x[1],reverse = True)[0][0],
                     '승차인원' : sorted(sorted(get[i].items())[0:5], key = lambda x : x[1],reverse = True)[0][1]})       

        
max =  extract[0]['승차인원']                # 첫번째 승차인원을 최대값으로서 설정한다.
for i in range(len(extract)) :              # for문을 돌면서 나온 extract[i]['승차인원'] 값이 기존의 최대값보다 크면 새로나온것이 최대값으로 갱신된다.   
      if extract[i]['승차인원'] > max :
            max = extract[i]['승차인원']
              
      else :                                # 기존의 최대값이 여전히 크면 여전히 최대값으로서 작용
            max = max
            
for i in range(len(extract)) :              # for문을 돌면서 조건문에서 승차인원이 max값인 자료의 날짜, 요일 , 시간, 승차인원을을 출력한다.
      if extract[i]['승차인원'] == max  :
            print('날짜 : {} , 요일 : {} , 시간대 : {} , 승차인원 : {}'.format(extract[i]['날짜'],
                                                                          extract[i]['요일'],
                                                                    extract[i]['시간'],
                                                                  extract[i]['승차인원'])) 
print()       # 한 줄 띄워 준다.

print('******************************* 테스트 3 *******************************') 
print('시간대별 평균 승차 인원수 출력') 
print()

time7 = []              # 각각의 시작 시간대별로 리스트변수 time 선언
time8 = []
time9 = []
time10 = []
time11 = [] 

for i in range(len(get)) :              # 위에서 선언했던 승차 정보만 모은 get 변수를 이용하여 각각의 시간대별로 승차인원수 정보를 모은다.
        time7.append(get[i]['7'])
        time8.append(get[i]['8'])
        time9.append(get[i]['9'])
        time10.append(get[i]['10'])
        time11.append(get[i]['11'])
        
print('7~8시 평균 승차인원수 : {}'.format(sum(time7)/len(time7)))     # 시간대별 총인원수의 합을 그 시간대의 time변수의 크기로 나눈다. 
print('8~9시 평균 승차인원수 : {}'.format(sum(time8)/len(time8)))
print('9~10시 평균 승차인원수 : {}'.format(sum(time9)/len(time9)))
print('10~11시 평균 승차인원수 : {}'.format(sum(time10)/len(time10)))
print('11~12시 평균 승차인원수 : {}'.format(sum(time11)/len(time11)))

