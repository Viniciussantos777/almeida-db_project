import sqlite3
import time
import choices

def choice(order):    
    if order == 1:
        return 'escolheu 1'
        
    elif order == 2:
        return 'escolheu 2'

    elif order == 3:
        return 'escolheu 3'
    
    elif order == 4:
        return 'escolheu 4'
        
    elif order == 5:
        return 'escolheu 5'
        
    elif order == 6:
        return 'escolheu 6'
        
    elif order == 7:
        return 'escolheu 7'
        
        
while 1==1:
    print('-=-'*20)
    print('Welcome to Almeida_DB System!')
    print('Choose your necessity:')
    print('[1] -')
    print('[2] -')
    print('[3] -')
    print('[4] -')
    print('[5] -')
    print('[6] -')
    print('[7] EXIT')
    print('-=-'*20)
    
    try:
        
        order=int(input('Put here your choice: '))
        

        if order == 7:
            print('Você está saindo do sistema Almeida_DB!')
            time.sleep(1)
            break
        print(choice(order))
        time.sleep(1)
    
    except ValueError:
        print('Please enter a valid number!')
        continue
