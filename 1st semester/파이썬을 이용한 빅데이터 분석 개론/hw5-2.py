
# Assignment Number... : 5
# Student Name........ : 이택윤
# File Name........... : hw5_이택윤
# Program Description. : try, except 문을 이용하여 소수판별을 하는 과제입니다.

while True :             # while을 사용하여 양의정수가 입력될 때까지 무한루프를 돌린다. 
    try :                  
        number = int(input('임의의 양의 정수를 입력하세요: '))   # input()을 이용하여 양의 정수를 받는다.
        if number <=0 or number ==1 :                          # 입력받은 수가 0보다 작거나 같은경우와  1인경우 예외를 생성한다.   
            raise ValueError 
        for i in range(2,number) :                             # for문에서 숫자 2와 입력받은 수 사이의 어떠한 수로 나눠진다면 소수가 아닌것을 나타내고 그 이유를 보여준다.
            if number%i == 0 :
                print('{}x{} \n이 숫자는 소수가 아닙니다.'.format(i,int(number/i)))
                break
        else :
            print('이 숫자는 소수입니다')                      # 소수인 경우의 출력
            break 
        break
    except ValueError :                                      # 예외처리 -> value error라고 출력하며 1보다 큰 양의 정수를 입력하라고 출력한다. 
                print('ValueError: 1보다 큰 양의 정수를 입력하세요.')   

