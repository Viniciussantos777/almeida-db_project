import sqlite3
import pandas as pd
import time
import choices

conexao = sqlite3.connect('almeida_db_project.db')
cursor = conexao.cursor()
   
while 1==1:
    print('-=-'*20)
    print('Welcome to Almeida_DB System!')
    print('Choose your necessity:')
    print('[1] Consumption by energy type')
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
            print('Youre loggin off from Almeida_DB!')
            time.sleep(1)
            break
        
        elif order == 1:
            choices.initial_choice1()
            time.sleep(1)
    
    except ValueError:
        print('Coloque um número válido!')
        time.sleep(1)
        continue
