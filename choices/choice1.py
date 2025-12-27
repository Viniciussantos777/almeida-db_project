import sqlite3
import time



def pesquisa_cidade(escolha_1):
    conexao = sqlite3.connect('almeida_db_project.db')
    cursor = conexao.cursor()
    
    busca = list(cursor.execute(f'''SELECT info_consum FROM info WHERE id_city = {escolha_1}'''))
    
    
    




def pesquisa_cidade_ano(escolha_city,escolha_year):
    pass





#Primeira visão dessa escolha:
def initial_choice1():
    conexao = sqlite3.connect('almeida_db_project.db')
    cursor = conexao.cursor()
    
    #Opções de escolha:
    while 1==1:
        print('='*20)
        print('Choose the type of search:')
        print('[1] Per City (All years)')
        print('[2] Per City (Only one year)')
        print('[3] Exit')
        try:
            order=int(input('Put here your choice: '))
            
            #Saída
            if order == 3:
                print('Back to menu...')
                time.sleep(1)
                break
            
            #Escolher info por 1 cidade para todos os anos:
            elif order == 1:
                
                #Escolha cidade
                cursor.execute('''SELECT id_city, city_name FROM nome_city''')
                dados = cursor.fetchall()
                
                opcoes = {id_city: city_name for id_city, city_name in dados}
                
                print('='*20)
                print('Escolha uma das seguintes cidades:')
                for id_city, nome in opcoes.items():
                    print(f"{id_city} - {nome}")
    

                #Escolha_1 é a escolha da 1º opção que só precisa da cidade.
                escolha_1 = int(input('Escolha um dos números: '))
                
                pesquisa_cidade(escolha_1)
                time.sleep(2)
                
                
            #Escolher info por 1 cidade para 1 ano específico:    
            elif order == 2:
                
                #Escolha cidade
                cursor.execute('''SELECT id_city, city_name FROM nome_city''')
                dados = cursor.fetchall()
                
                opcoes = {id_city: city_name for id_city, city_name in dados}
                
                print('='*20)
                print('Escolha uma das seguintes cidades:')
                for id_city, nome in opcoes.items():
                    print(f"{id_city} - {nome}")
    
                escolha_city = int(input('Escolha uma das cidades(Numeros): '))
                
                #Escolha o ano
                cursor.execute('''SELECT pk_id_year, year_name FROM year''')
                dados = cursor.fetchall()
                
                opcoes_year = {pk_id_year: year_name for pk_id_year, year_name in dados}
                
                print('='*20)
                print('Escolha um dos seguintes anos:')
                for pk_id_year, year_name in opcoes_year.items():
                    print(f"{pk_id_year} - {year_name}")
    
                escolha_year = int(input('Escolha um dos anos(Numeros): '))
                
                #Função puxada
                pesquisa_cidade_ano(escolha_city,escolha_year)
                time.sleep(2)
        
        
        #Tratamento de erros:
        except ValueError:
            print('Coloque um número válido!')
            time.sleep(1)
            continue




