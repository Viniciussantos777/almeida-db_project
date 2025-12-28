import time
import choices

# Hud de escolhas
while 1==1:
    print('-=-'*20)
    print('''
    Welcome to Almeida_DB System!
    Choose your necessity:
    [1] Cities' consumption by energy type
    [2] Charts comparing cities
    [3] -
    [4] -
    [5] -
    [6] -
    [7] EXIT'''
    )
    print('-=-'*20)
    
    try:
        
        order=int(input('Put here your choice: '))
        

        if order == 7:
            print('Youre loggin off from Almeida_DB!')
            time.sleep(1)
            break
        
        # Escolha nº 1
        elif order == 1:
            time.sleep(1)
            choices.initial_choice1()
            
            
        elif order == 2:
            time.sleep(1)
            choices.initial_choice2()
            
    
    except ValueError:
        print('Coloque um número válido!')
        time.sleep(1)
        continue
