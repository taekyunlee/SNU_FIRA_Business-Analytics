# Assignment Number...: 4
# Student Name........: 이현호
# File Name...........: hw4_이현호
# Program Description.: 제어문을 활용하는 과제입니다.



"""
restaurant_list = {'상호' : ['A', 'B', 'C', 'D', 'E', 'F'], '메뉴' : ['피자', '치킨', '짜장면', '초밥', '치킨', '족발'], '가격(원)' : [20000, 18000, 5000, 15000, 23000, 30000]}
                                                                                                                            # restaurant_list 변수에 dict 자료형을 할당합니다.
want_to_eat = input('먹고 싶은 음식을 입력하세요 : ')                                                                       # want_to_eat 변수에 input()함수를 이용해 먹고싶은 음식을 입력받아 할당합니다.

if want_to_eat not in restaurant_list.get('메뉴') :                                                                         # if문과 in 을 이용하여 want_to_eat 변수가 ['피자', '치킨', '짜장면', '초밥', '치킨', '족발'] 중에 있는지 확인합니다.
                                                                                                                            # ['피자', '치킨', '짜장면', '초밥', '치킨', '족발'] 값을 가져오기 위해서 get()함수를 이용합니다.
    print('결과가 없습니다.')                                                                                               # 또한 in 앞에 not을 사용하여 want_to_eat가 메뉴에 없을 때 True값을 반환하고 print('결과가 없습니다.')함수를 이용하여 출력합니다.
else :
    i = 0                                                                                                                   # False값을 반환한경우 else문이 실행되는데, while문을 이용한 순환문을 만들었다. 순환횟수를 위해서 i=0이라고 할당하였다.
    while i < len(restaurant_list.get('메뉴')) :                                                                            # while문의 시작점인 횟수는 i < 메뉴의 개수로 하였다.                         
        if restaurant_list.get('메뉴')[i] == want_to_eat :                                                                  # 메뉴의 개수동안 if를 통해서 want_to_eat가 restaurant_list.get('메뉴')[i] 즉 i번째 있는 메뉴의 index를 찾고,
            print('식당 {}, 가격 {} 원'.format(restaurant_list.get('상호')[i], restaurant_list.get('가격(원)')[i]))         # print()함수와 get()함수를 통해 상호와 가격(원)의 index를 통해 출력한다.
                                                                                                                            # 또한 format을 사용하여 print()함수를 보다 편하게 이용하였다.
        i += 1                                                                                                              # index는 0부터 매 회마다 +1을 통해 len()함수 즉 메뉴의 개수까지 작동한다.
        
                                                                                                                            # 논리는 만약 사용자가 입력한 음식이 메뉴에 없지 않으면, 사용자가 입력한 메뉴를 restaurant_list에 있는
                                                                                                                            # 메뉴들은 순서대로 일치하는 지를 확인하고 일치한다면, 식당과 가격(원)을 출력한다.
                                                                                                                            # 이렇게 한 이유는 else문이 want_to_eat이 restaurant_list의 메뉴에 반드시 있으므로
                                                                                                                            # want_to_eat이 restaurant_list의 모든 메뉴들과 한번씩 검사를 하여서 모든 상호와 가격을 출력할 수 있도록 만들었다.
"""





restaurant_list = [{'상호' :'A', '메뉴' : '피자', '가격(원)' : 20000},
                   {'상호' :'B', '메뉴' : '치킨', '가격(원)' : 18000},
                   {'상호' :'C', '메뉴' : '짜장면', '가격(원)' : 5000},
                   {'상호' :'D', '메뉴' : '초밥', '가격(원)' : 15000},
                   {'상호' :'E', '메뉴' : '치킨', '가격(원)' : 23000},
                   {'상호' :'F', '메뉴' : '족발', '가격(원)' : 30000}]                                             # restaurant_list 리스트 변수에 dict 자료형을 할당합니다.


want_to_eat = input('먹고 싶은 음식을 입력하세요 : ')                                                              # want_to_eat 변수에 input()함수를 이용해 먹고싶은 음식을 입력받아 할당합니다.


i = 0                                                                                                              # i는 밑의 순환문에서 사용되는 순환횟수이며, 
x = 0
while i < len(restaurant_list) :
    if (want_to_eat in restaurant_list[i]['메뉴']) :
        x += 1
    i += 1
else :
    if (x == 0) :
        print('결과가 없습니다.')

i = 0
while i < len(restaurant_list) :
    if restaurant_list[i].get('메뉴') == want_to_eat :
        print('식당 {}, 가격 {} 원'.format(restaurant_list[i].get('상호'), restaurant_list[i].get('가격(원)'))) 
    i += 1
