import choices

while True:
    print('-=-'*20)
    print('''
    Welcome to Almeida_DB System!
    Choose your necessity:
    [1] Cities' consumption by energy type
    [2] Charts comparing cities
    [3] EXIT'''
    )
    print('-=-'*20)
    
    try:
        
        order=int(input('Put here your choice: '))
        
        # Saída do programa
        if order == 3:
            print('Youre loggin off from Almeida_DB!')
            break
        
        # Escolha nº 1
        elif order == 1:
            choices.initial_choice1()
            
        # Escolha nº 2
        elif order == 2:
            choices.initial_choice2()
            pass
    
    except ValueError:
        print('Coloque um número válido!')
        continue
