
# Assignment Number... : 6
# Student Name........ : 이택윤
# File Name........... : hw6_이택윤
# Program Description. : 이것은 새로운 함수를 정의하고 이용하며 람다함수를 구현해보는 과제입니다.

def area_triangle(h,w) :            # def를 사용하여 함수  area_triangle를 정의하였고 매개변수로 h와w 를 정의하였다.
    return 0.5*h*w                  # 이 함수는 넓이의 값을 계산하여 return한다.

print(area_triangle(h=10, w=15))    #  함수에 전달인자를 넣고 return된값을 print()를 이용하여 출력한다.

def distance(a,b) :                 # def를 이용하여 함수 distance를 정의하였고 매개변수로 a 와 b 를 받는다.      
    d =0                            
    for i in range(2) :             # 변수 d에 0을 선언하고 for문에서 돌면서 값을 갱신한다.
         d = d + (a[i] - b[i])**2
    return d**(1/2)                 # d에 1/2승 즉, 루트를 씌워서 거리를 return한다.

print(distance(a=(1,2),b=(5,7)))    # 전달인자에 a=(1,2) , b=(5,7) 을 넣어서 그 결과값을 print()를 활용해 출력한다.

def count(n) :                      # def를 이용해 count 함수를 정의하고 매개변수로서 n을 선정한다.
        if n>0 :                    # if - else 문을 사용해 n이 0보다 큰지 아닌지 판단한다. 
            print(n)                # n이 0보다 크다면 출력
            count(n-1)              # 계속해서 count함수를 호출한다. (재귀함수)
        else : 
            print('zero!!')         # n이 0과 같아졌을 시 'zero!!'출력
         
count(n=5)                          # count 함수에 5를 넣고 출력값을 본다.

area_triangle_ld = lambda h,w :  0.5*h*w  # lambda 함수를 이용해 area_triangle함수를 정의하였다.

print(area_triangle_ld(h=10,w=15))        # area_triangle_ld함수에 전달인자를 넣고 print()를 이용해 그 값을 출력한다.

