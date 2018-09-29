
# Assignment Number... : 5
# Student Name........ : 이택윤
# File Name........... : hw5_이택윤
# Program Description. : 이것은 if_else 문과 while, for 문을 활용하여 원하는 결과를 출력하는 과제입니다.


a = int(input('Enter a: '))        # int() 와 input()을 활용하여 각각의 변수 a,b,c에 정수를 선언합니다.
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a>b and a>c  :                  # if_else 문을 이용하여 입력된 a,b,c의 값을 비교하여 작은 값 두개의 합을 출력합니다.
    print(b+c)                                       
elif b>a and b>c :
    print(a+c)
else   :
    print(a+b)

    
city = input('Enter the name of the city: ')    # input()을 활용하여 도시의 이름을 입력 받습니다.

if city == 'Seoul' :                            # if_else 문을 활용하여 입력받은 도시의 이름과 그 도시의 면적을 문자열 서식을 통해서 출력합니다.
    size = 605
elif city =='New York' :
    size = 789 
elif city =='Beijing' : 
    size = 16808
else : 
    size ='Unknown'
    
print('The size of {} is {}'.format(city , size))    



import math                     # math 라이브러리를 import를 이용해서 불러옵니다.
for i in range(10) :            # 0부터 9까지의 10개의 정수의 계승 값을 구하기 위해서 for문을 이용하고 그 안에서 math.factorial()을 적용합니다.
      print(math.factorial(i)) 

j=0         
while j< 10 :                   # 마찬가지로 while 문을 이용하고 그 안에서 math.factorial()을 이용하여 계승 값을 구합니다.
      print(math.factorial(j)) 
      j+=1 

