# Assignment Number... : 2
# Student Name........ : 이택윤
# File Name........... : hw2_이택윤
# Program Description. : 이것은 문자열 자료형의 변수를 생성하고 슬라이싱하여 출력하는 과제입니다.

cellphone ='Samsung Galaxy J7' #cellphone 이라는 변수에 핸드폰 기종이름과 제조사 명을 선언하였다.
print(cellphone)               #print()를 이용하여 cellphone변수를 출력하였다.

company = cellphone[:7]        #문자열 슬라이싱을 이용하여 제조사인 'Samsung'을 company라는 변수에 저장하였다.
print(company)                 #print()를 이용하여 company 변수를 출력하였다.

model =cellphone[8:]           #문자열 슬라이싱을 이용하여 모델명인 'Galaxy J7'을 model이라는 변수에 저장하였다.
print(model)                   #print()를 이용하여 model 변수를 출력하였다.

print(type(company))           #type()과 print()를 이용하여 company 와 model 변수의 자료형을 출력하였다.
print(type(model))
 
print('It had been that way for days and days.\
\n And then, just before the lunch bell rang, he walked into our \nclass room. \
\n Stepped through that door white and softly as the snow.') 
                               # print() 와 그 안에서 '\n'을 사용하여 줄바꿈을 하였고 정해진 형식에 따라 출력하였다.
                               # 또한 '\'을 이용하여 line continuation을 적용하였다.

