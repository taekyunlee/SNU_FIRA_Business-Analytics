'''
Coding Style
   - redundancy :
   - minor error :
   - major error :
Poor Documentation :
Logical Error :
Compilation Error :
Score : 100/100
TA's comment :
'''

# Assignment Number... : 1
# Student Name........ : 이택윤
# File Name........... : hw1_이택윤
# Program Description. : 이것은 기본적인 자료형과 input 함수를 활용하여 값을 입력받고 그 결과를 출력하는 과제입니다.

season = input('What is your favorite season? ')   # 계절을 입력받기 위해서 input() 이라는 함수를 사용했고 season이라는 변수를 선언했다.
print(season)                                      # 계절을 출력하기 위해서 print() 함수를 사용했다.

date = input('Which date were you born? ')         # 태어난 날짜를 입력받기 위해서 input() 이라는 함수를 사용했고 date라는 변수를 선언했다.

print(type(date))                                  # date의 타입을 출력하기 위해 print()와 type()을 사용했다. 

date = float(date)                                 # date의 자료형을 float타입으로 변경하기 위해 float()을 사용하고 date 변수를 재 선언 하였다.
print(type(date))                                  # 변경된 date변수의 자료형을 print()를 이용하여 출력한다.

print('My favorite season is '+ season + '.'+ ' I was born on the ' + str(int(date))+'th.')   # 계절과 날짜를 한번에 출력하기 위해 print()안에 '+'를 함께 사용하였고 
                                                                                              # float타입인 date변수를 int타입으로 변경한뒤 문자열로서 출력하기 위해 str()을 사용하였다.
                                                 
                                                   
    

