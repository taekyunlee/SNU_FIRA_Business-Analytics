
# Assignment Number... : 3
# Student Name........ : 이택윤
# File Name........... : hw3_이택윤
# Program Description. : 이것은 문자열 서식 및 리스트,튜플 그리고 이들에 대한 슬라이싱을 이용하여 결과물을 출력하는 과제 입니다.

steak = 30000                           # steak, VAT 각각에 30000과 0.15를 선언하였습니다.
VAT = 0.15 

print('스테이크의 원래 가격은 {} 원입니다. 하지만 VAT 가 {}%로, 계산하셔야 할 \n가격은 {} 원입니다.'.format(steak,int(VAT*100),int((steak+steak*(VAT))))) 
                                        # print() 와 str.format() 메소드를 활용하여 문자열 서식설정을 하여 각각의 값들이 반영되어 출력되도록 하였습니다.     
    
s = '@^TrEat EvEryonE yOu meet likE you want tO be treated.$%'     # 주어진 문장을 변수 s에 선언 하였습니다.
s = s[:3] + s[3:].lower()                                          # 가장처음의 T문자를 그대로 유지하기 위하여 앞부분을 슬라이싱 한 것과 뒷부분을 슬라이싱하여 소문자로 바꾼것을 결합하였습니다. 
s = s.strip('@%^$')                                                # 문자열 앞뒤에 있는 특수문자를 제거하기 위하여 strip()메소드를 이용하였습니다.
print(s)                                                           # print() 이용하여 출력하였습니다.

numbers =(2,18,26,89,45,39,14)                                     # numbers라는 변수에 튜플을 주어진 순서대로 선언하였습니다.
print(numbers)                                                     # print() 이용하여 출력하였습니다.
print(len(numbers))                                                # print() 이용하여 요소의 개수를 출력하였습니다.

fruits = ['apple','orange','strawberry','pear','kiwi']             # fruits라는 변수에 리스트를 생성하였습니다.
print(fruits)                                                      # print() 이용하여 리스트를 출력하였습니다.

fruits_sub = fruits[:3]                                            # 슬라이싱을 이용하여 리스트의 첫 세 요소를 가져와서 fruits_sub에 선언하였습니다.
print(fruits_sub)                                                  # print() 이용하여 fruits_sub를 출력하였습니다.




