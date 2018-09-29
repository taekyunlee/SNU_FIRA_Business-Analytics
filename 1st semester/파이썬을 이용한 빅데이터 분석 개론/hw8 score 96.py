
# Assignment Number... : 8
# Student Name........ : 이택윤
# File Name........... : hw8_이택윤
# Program Description. : 이것은 패키지와 모듈을 이용하고 함수를 정의하여 원하는 결과를 출력하는 과제입니다.

import datetime , time                     # import를 이용하여 datetime 과 time을 불러옵니다.     
now = datetime.datetime.now()              # now 변수에 datetime.now() 함수를 저장한다.      
print(now.strftime('%Y-%m-%d %H:%M:%S'))  # 시간 표현 형식 정의후 print()를 이용하여 출력한다.

import calendar                            # import를 이용하여 calendar 모듈을 불러옵니다.
print(calendar.isleap(2050))               # isleap()함수를 이용하여 윤년인지 여부를 판단한다.           
print(calendar.weekday(2050,7,7))          # weekday() 함수를 이용하여 2050년 7월7일이 무슨요일인지 출력합니다.

                        
from collections import Counter            # collections 모듈을 불러오고 Counter도 불러옵니다.

def vowel(x) :                             # def를 이용하여 함수를 정의합니다.
    Counter(x)
    for vow in ['a','e','i','o','u'] :     # for 문을 이용하여 해당하는 모음이 Counter(x)안에 있으면 그 모음과 그 모음의 숫자를 문자열 서식을 통해 출력합니다.
        if vow in Counter(x) :
             print('The number of {}: {}'.format(vow, Counter(x)[vow]))
        else :
             print('The number of {}: {}'.format(vow, 0))
    
    for i in range(len(Counter(x).most_common())) :                     # for문을 이용하여 Counter(x).most_common()을 돌면서 모음을 처음 만나면 그 모음을 common변수에 저장한다.
        if Counter(x).most_common()[i][0] in ['a','e','i','o','u'] :   
              common =Counter(x).most_common()[i][0]
              break 
 
    print(x.replace(common, common.upper()))                            # str.replace()를 이용하여 common변수에 저장된 모음을 대문자로 바꿔준다.  
        

vowel('The regret after not doing something is bigger than that of doing something.')     #vowel함수에 인자를 넣어 값을 반환해본다.

