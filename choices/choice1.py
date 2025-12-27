import sqlite3
import time



def pesquisa_cidade_all_years(escolha_1,escolha_2):
    conexao = sqlite3.connect('almeida_db_project.db')
    cursor = conexao.cursor()
    
    query = '''
    SELECT year.year_name, info.info_consum, energy_font.name_energy, industry.name_indus, clime.name_clime
    FROM info
    INNER JOIN year ON info.pk_id_year = year.pk_id_year
    INNER JOIN energy_font ON info.pk_id_en_fo = energy_font.pk_id_en_fo
    INNER JOIN industry ON info.pk_id_indus = industry.pk_id_indus
    INNER JOIN clime ON info.pk_id_clime = clime.pk_id_clime
    WHERE info.id_city = ? AND info.pk_id_en_fo = ?
'''
    busca = cursor.execute(query, (escolha_1,escolha_2)).fetchall()
    
    print('-'* 75)
    print(f"\n{'YEAR':<10} | {'CONSUM':<10} | {'EN.FONT':<15} | {'INDUSTRY':<20} | {'CLIME':<15}")
    print("-" * 75)

    for ano, consumo, fonte, industria, clima in busca:
        print(f"{int(ano):<10} | {int(consumo):<10} | {str(fonte):<15} | {str(industria):<20} | {str(clima):<15}")
        
    if not busca:
        print("NONE REGISTER FOUND WITH THIS PRESCRIPTIONS!")
    time.sleep(2)
    input("\nTAP 'enter' to continue:")
    
    
    




def pesquisa_cidade_one_year(escolha_city,escolha_year):
    conexao = sqlite3.connect('almeida_db_project.db')
    cursor = conexao.cursor()

    query = '''
    SELECT year.year_name, info.info_consum, energy_font.name_energy, industry.name_indus, clime.name_clime
    FROM info
    INNER JOIN year ON info.pk_id_year = year.pk_id_year
    INNER JOIN energy_font ON info.pk_id_en_fo = energy_font.pk_id_en_fo
    INNER JOIN industry ON info.pk_id_indus = industry.pk_id_indus
    INNER JOIN clime ON info.pk_id_clime = clime.pk_id_clime
    WHERE info.id_city = ? AND info.pk_id_year = ?
'''
    busca = cursor.execute(query, (escolha_city,escolha_year)).fetchall()
    
    print('-'* 75)
    print(f"\n{'YEAR':<10} | {'CONSUM':<10} | {'EN.FONT':<15} | {'INDUSTRY':<20} | {'CLIME':<15}")
    print("-" * 75)

    for ano, consumo, fonte, industria, clima in busca:
        print(f"{int(ano):<10} | {int(consumo):<10} | {str(fonte):<15} | {str(industria):<20} | {str(clima):<15}")
        
    if not busca:
        print("NONE REGISTER FOUND WITH THIS PRESCRIPTIONS!")
    time.sleep(2)
    input("\nTAP 'enter' to continue:")




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
                dados_cidade = cursor.fetchall()
                
                opcoes_cidade = {id_city: city_name for id_city, city_name in dados_cidade}
                
                print('='*20)
                print('Escolha uma das seguintes cidades:')
                for id_city, nome in opcoes_cidade.items():
                    print(f"{id_city} - {nome}")
    

                #Escolha_1 é a escolha da 1º opção que só precisa da cidade e fonte de energia
                escolha_1 = int(input('Escolha um dos números: '))
                
                # Escolha de fonte de energia
                cursor.execute('''SELECT pk_id_en_fo, name_energy FROM energy_font''')
                dados_energia = cursor.fetchall()
                
                opcoes_energia = {pk_id_en_fo: name_energy for pk_id_en_fo, name_energy in dados_energia}
                
                print('='*20)
                print('Escolha uma das seguintes fontes de energia: ')
                for pk_id_en_fo, nome in opcoes_energia.items():
                    print(f"{pk_id_en_fo} - {nome}")
                
                #Escolha_2 é a escolha da 1º opção que só precisa da cidade e fonte de energia
                escolha_2 = int(input('Escolha um dos números: '))
                
                pesquisa_cidade_all_years(escolha_1,escolha_2)
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
                pesquisa_cidade_one_year(escolha_city,escolha_year)
                time.sleep(2)
        
        
        #Tratamento de erros:
        except ValueError:
            print('Coloque um número válido!')
            time.sleep(1)
            continue




