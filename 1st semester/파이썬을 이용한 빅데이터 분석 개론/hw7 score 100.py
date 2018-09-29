# Assignment Number... : 7
# Student Name........ : 이택윤
# File Name........... : hw7_이택윤
# Program Description. : 이것은 제어문을 활용해 재미있는 프로그램을 만들어보는 과제입니다.

print('''  [전략게임 : 포켓몬스터 키우기]

             게임 규칙 : (1) 처음 시작할 때 키우고 싶은 3가지 포켓몬의 이름 중 하나를 입력하여 선택한다.(파이리,꼬부기,이상해씨)중 택1
             
                         (2) 배고픔, 피로도, 위생수준이 10 에 도달하면 포켓몬은 죽는다.
                         
                         (3) 나이가 70이 되면 포켓몬은 죽는다. 단, 진화를 하게되면 나이가 20만큼 젋어지고 경험치가 +1 이된다
                         
                         (4) 진화란 포켓몬의 생물학적 진화이며 진화는 총 2번 할 수 있다.
                         
                         (5) 진화하게 되면 포켓몬의 이름도 그에 따라 바뀐다.
                         
                         (6) 진화는 훈련을 시켜서 경험치를 15로 도달시키면 한번 또 다시 15을 쌓아 30이 되면 또 한 번 진화한다.
                         
                         (7) 진화를 2번하고 난 뒤 훈련을 해도 경험치는 쌓이지만 그 외의 아무변화는 없다.
                         
                         (8) 진화에 따른 포켓몬의 명칭 변화           [파이리-> 리자드 -> 리자몽]
                                                                      [꼬부기-> 어니부기-> 거북왕]
                                                                      [이상해씨-> 이상해풀-> 이상해꽃]  ''')

print('# 선택 가능한 포켓몬 : 파이리, 꼬부기, 이상해씨 \n')    # 입력 가능한 포켓몬의 이름을 보여준다.

name = input('키우고 싶은 포켓몬의 이름을 입력하시오 : ')      # name에 키우고 싶은 포켓몬의 이름을 입력받는다.

print()                                                        # 한 줄 띄어 보여줌

while(True) :                                                  # while()을 이용하여 만일 포켓몬 이름을 잘못 입력했을시 올바르게 입력하라고 안내한다.  
    if name in ['파이리','꼬부기','이상해씨'] :                # 정상적으로 입력했다면 그냥 빠져나간다.
           break 
    else :
           name = input('키우고 싶은 포켓몬의 이름을 올바르게 입력하십시오 :')
          
if name == '파이리'  :                                         # 포켓몬의 진화에 따른 명칭을 if문을 사용하여 할당한다.
    name2 = '리자드'
    name3 = '리자몽'
elif name == '꼬부기' : 
    name2 = '어니부기'
    name3 = '거북왕'
else : 
    name2 = '이상해풀'
    name3 = '이상해꽃'

hunger = 0                                        # 배고픔, 피로도 , 위생 , 경험치 ,나이에 대한 초기값을 0으로서 설정한다.                                            
fatigue = 0
hygiene = 0
experience = 0 
age = 0 

print('*** {}의 신체상태 ***\n'.format(name))     # 배고픔, 피로도 , 위생 , 경험치 ,나이에 대한 초기값을 출력해서 보여준다.
print('배고픔: {}'.format(hunger))
print('피로도: {}'.format(fatigue))
print('경험치: {}'.format(experience)) 
print('위생 수준: {}'.format(hygiene))
print('나이 :{}\n'.format(age))

while(True) :                                       
    
    print('{}에게 어떤 명령을 내릴까요?\n'.format(name))     # 어떤 명령을 내릴 수 있는지 print()를 이용하여 보여준다.
    print('''1 - 훈련시키기 
2 - 먹이주기
3 - 놀기
4 - 잠자기 
5 - 씻기 ''')
    
    print()                                                  # 한 줄 띄어 보여줌
    
    while(True) :
        try : 
            order = int(input('번호를 입력하세요 => '))      # order 변수에 번호를 입력받는다.
            if order in [1,2,3,4,5] :                        # try_except문을 이용하여 1에서 5의 숫자가 아닌것을 입력 했을시 제대로 입력하도록 안내한다. 
                break
            else :
                raise ValueError                             # 1~5의 숫자가 아닐경우 ValueError 발생시킨다.   
        except ValueError :
                print('1부터 5까지의 숫자중 하나를 정확히 입력하세요 \n')
             
    print()                                                  # 한 줄 띄어 보여줌
    
    if order == 1 :                                # 번호 1번 입력한경우 -> 경험치, 피로도, 배고픔 , 위생지수 증가 
             experience +=1
             fatigue +=1 
             hunger +=1  
             hygiene +=1
             print('배고픔이 증가 했습니다.')
             print('위생 상태가 나빠졌습니다.')
             print('경험치가 증가했습니다.' )
             print('피로도가 증가했습니다.\n')
    elif order == 2 :                               # 번호 2번 입력한 경우 -> 배고픔 감소
             hunger -=1
             print('배고픔이 감소했습니다\n.')
    elif order == 3 :                               # 번호 3번 입력한 경우 -> 위생상태 증가 , 피로도 감소
             fatigue -=1 
             hygiene +=1
             print('위생 상태가 나빠졌습니다.')   
             print('피로도가 감소했습니다.\n')
    elif order == 4 :                               # 번호 4번 입력한 경우 -> 피로도 감소
             fatigue -=1 
             print('피로도가 감소했습니다.\n')    
    else :                                          # 번호 5번 입력한 경우 -> 위생수준 나아짐
             hygiene -=1 
             print('위생수준이가 나아졌습니다.\n')
    
    age +=1                                         # 명령이 한 번 끝나고 나면 나이증가                       
    
    print('*** {}의 신체상태 ***\n'.format(name))   #print()를 이용하여 명령후의 신체상태 출력
    print('배고픔: {}'.format(hunger))
    print('피로도: {}'.format(fatigue))
    print('경험치: {}'.format(experience)) 
    print('위생 수준: {}'.format(hygiene))
    print('나이 :{}\n'.format(age))
    
    if experience == 15 :             # 경험치가 15로 쌓인경우 명칭변화 , 나이 20만큼 젊어짐 , 경험치 1추가
                name = name2
                age -=20
                experience +=1
                print('@@@@@@@@@@@@@@@{}로 진화 했습니다!!!@@@@@@@@@@@@@@@\n'.format(name))                                                                 
                
    if experience == 30 :             # 경험치가 30으로 쌓인경우 명칭변화 , 나이 20만큼 젊어짐 , 경험치 1추가
                name = name3
                age -=20  
                experience +=1
                print('###############{}으로 진화 했습니다!!!###############\n'.format(name))

                
    if   hunger == 10  & hygiene == 10 & fatigue == 10 :         # if-elif문을 이용하여 피로도, 위생지수 , 배고픔 지수가 한계지수를 넘었을 시 몬스터가 죽었다는 것을 출력해준다.                  
         print('{}은(는) 죽었습니다. 왜냐하면 밥을 제대로 먹지 못했고 피로하고 씻지 못했기 때문입니다.'.format(name))
         break    
    elif hunger == 10  & fatigue == 10 :
         print('{}은(는) 죽었습니다. 왜냐하면 밥을 제대로 먹지 못했고 피로하기 때문입니다.'.format(name))
         break   
    elif fatigue == 10 & hygiene == 10 :
         print('{}은(는) 죽었습니다. 왜냐하면 피로하고 제대로 씻지 못했기 때문입니다.'.format(name))
         break   
    elif hunger == 10  & hygiene == 10:
         print('{}은(는) 죽었습니다. 왜냐하면 밥을 제대로 먹지 못했고 제대로 씻지 못했기 때문입니다.'.format(name))
         break
    elif hunger == 10  :
         print('{}은(는) 죽었습니다. 왜냐하면 밥을 제대로 먹지 못했기 때문입니다.'.format(name))
         break
    elif fatigue == 10 :
         print('{}은(는) 죽었습니다. 왜냐하면 피로를 제 때 풀지 못했기 때문입니다.'.format(name))    
         break        
    elif hygiene == 10 :
         print('{}은(는) 죽었습니다. 왜냐하면 제대로 씻지 못했기 때문입니다.'.format(name)) 
         break     
    
    if age == 70 :                                        # 나이가 70이 되면 몬스터는 죽고 게임은 끝난다.
        print('{}은(는) 늙어 죽었습니다'.format(name)) 
        break
        
    

