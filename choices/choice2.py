import matplotlib.pyplot as plt
from choices.connect_db import connect
conexao, cursor = connect()

#Gráfico consumo x anos / fonte energética
def pesquisa_cidade_grafico_maximos(escolha_city, escolha_energy):

    # Usamos MAX(info.info_consum) e GROUP BY year.year_name
    # Isso garante que o SQL retorne apenas UMA linha por ano, com o maior valor encontrado
    query = '''
        SELECT y.year_name, MAX(i.info_consum), ef.name_energy
        FROM info AS i
        INNER JOIN year AS y ON i.pk_id_year = y.pk_id_year
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_en_fo = ?
        GROUP BY y.year_name
        ORDER BY y.year_name ASC
    '''
    
    busca = cursor.execute(query, (escolha_city, escolha_energy)).fetchall()

    if not busca:
        print("\n[!] NO DATA FOUND FOR THIS SELECTION.")
        return

    anos_x = []
    consumo_y = []
    nome_fonte = busca[0][2]

    print(f"\nMAX CONSUMPTION PER YEAR - Source: {nome_fonte}")
    print(f"{'YEAR':<10} | {'MAX CONSUM':<10}")
    print("-" * 25)

    for ano, max_consumo, fonte in busca:
        print(f"{int(ano):<10} | {int(max_consumo):<10}")
        anos_x.append(str(ano))
        consumo_y.append(max_consumo)

    # Configuração do Gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(anos_x, consumo_y, marker='o', linestyle='-', color='darkred', linewidth=2)
    
    plt.title(f'Peak Consumption per Year - {nome_fonte}')
    plt.xlabel('Years')
    plt.ylabel('Maximum Consumption Value')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)

    print("\nDisplaying peak consumption chart...")
    plt.show()

    conexao.close()
    




# Pesquisa e gráficos com o mínimo e energia
def pesquisa_cidade_grafico_minimos(escolha_city, escolha_energy):

    # Trocamos MAX por MIN para pegar o menor valor de cada ano agrupado
    query = '''
        SELECT y.year_name, MIN(i.info_consum), ef.name_energy
        FROM info AS i
        INNER JOIN year AS y ON i.pk_id_year = y.pk_id_year
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_en_fo = ?
        GROUP BY y.year_name
        ORDER BY y.year_name ASC
    '''
    
    busca = cursor.execute(query, (escolha_city, escolha_energy)).fetchall()

    if not busca:
        print("\n[!] NO DATA FOUND FOR THIS SELECTION.")
        return

    anos_x = []
    consumo_min_y = []
    nome_fonte = busca[0][2]

    print(f"\nMINIMUM CONSUMPTION PER YEAR - Source: {nome_fonte}")
    print(f"{'YEAR':<10} | {'MIN CONSUM':<10}")
    print("-" * 25)

    for ano, min_consumo, fonte in busca:
        print(f"{int(ano):<10} | {int(min_consumo):<10}")
        anos_x.append(str(ano))
        consumo_min_y.append(min_consumo)

    # Configuração do Gráfico
    plt.figure(figsize=(10, 5))
    # Usando uma cor diferente (laranja) para diferenciar do gráfico de máximos
    plt.plot(anos_x, consumo_min_y, marker='o', linestyle='-', color='orange', linewidth=2)
    
    plt.title(f'Minimum Consumption per Year - {nome_fonte}')
    plt.xlabel('Years')
    plt.ylabel('Minimum Consumption Value')
    plt.grid(True, linestyle=':', alpha=0.6)

    print("\nDisplaying minimum consumption chart...")
    plt.show()

    conexao.close()
    
    
def grafico_fontes_maximo(escolha_city, escolha_year):

    # Selecionamos o nome da fonte e o maior valor de consumo (MAX)
    # Agrupamos por fonte para evitar a sobreposição de múltiplos registros
    query = '''
        SELECT ef.name_energy, MAX(i.info_consum)
        FROM info AS i
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_year = ?
        GROUP BY ef.name_energy
        ORDER BY MAX(i.info_consum) DESC
    '''
    
    busca = cursor.execute(query, (escolha_city, escolha_year)).fetchall()

    if not busca:
        print("\n[!] NO DATA FOUND FOR THIS CITY AND YEAR.")
        return

    # Preparação das listas para o gráfico
    fontes = [row[0] for row in busca]
    consumos_max = [row[1] for row in busca]

    # --- Configuração do Gráfico ---
    plt.figure(figsize=(12, 7))
    
    # Criando as barras
    cores = ['#2c3e50', '#e67e22', '#27ae60', '#2980b9', '#8e44ad', '#c0392b']
    barras = plt.bar(fontes, consumos_max, color=cores)

    # Adicionando os valores exatos acima das barras para clareza
    for barra in barras:
        height = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., height + 0.5,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold')

    # Títulos e Labels em Inglês
    plt.title(f'Peak Energy Consumption by Source\nCity ID: {escolha_city} | Year ID: {escolha_year}', fontsize=14)
    plt.xlabel('Energy Sources', fontsize=12)
    plt.ylabel('Maximum Consumption Value', fontsize=12)
    
    plt.xticks(rotation=30, ha='right') # Inclinação para evitar sobreposição de nomes
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    print("\nOpening peak consumption bar chart...")
    plt.show()

    conexao.close()


def grafico_fontes_minimo(escolha_city, escolha_year):

    # Selecionamos o MIN(info_consum) para pegar o menor registro de cada fonte
    # O GROUP BY garante que não haja sobreposição (uma barra por fonte)
    query = '''
        SELECT ef.name_energy, MIN(i.info_consum)
        FROM info AS i
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_year = ?
        GROUP BY ef.name_energy
        ORDER BY MIN(i.info_consum) ASC
    '''
    
    busca = cursor.execute(query, (escolha_city, escolha_year)).fetchall()

    if not busca:
        print("\n[!] NO DATA FOUND FOR THIS SELECTION.")
        return

    # Preparação das listas
    fontes = [row[0] for row in busca]
    consumos_min = [row[1] for row in busca]

    # --- Configuração do Gráfico ---
    plt.figure(figsize=(12, 7))
    
    # Usando tons de azul/ciano para representar valores "mínimos" ou "frios"
    cores = ['#34495e', '#16a085', '#27ae60', '#2980b9', '#3498db', '#1abc9c']
    barras = plt.bar(fontes, consumos_min, color=cores)

    # Adicionando os valores exatos acima das barras
    for barra in barras:
        height = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., height + 0.2,
                 f'{int(height)}', ha='center', va='bottom', fontsize=10)

    # Títulos e Labels
    plt.title(f'Minimum Energy Consumption by Source\nCity ID: {escolha_city} | Year ID: {escolha_year}', fontsize=14)
    plt.xlabel('Energy Sources', fontsize=12)
    plt.ylabel('Minimum Consumption Value', fontsize=12)
    
    plt.xticks(rotation=30, ha='right')
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    print("\nOpening minimum consumption bar chart...")
    plt.show()

    conexao.close()




def initial_choice2():
    
    #Opções de escolha:
    while True:
        print('='*20)
        print('Choose the type of chart:')
        print('[1] City (Maximum consumption x year)')
        print('[2] City (Minimum consumption x year)')
        print('[3] Maximum consuption per energy font')
        print('[4] Minimum consuption per energy font')
        print('[5] Exit')
        print('='*20)
        try:
            order=int(input('Put here your choice: '))
            
            #Saída
            if order == 5:
                print('Back to menu...')
                break
            
            #Escolher info City (Maximum consumption x year):
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
                if escolha_1 not in opcoes_cidade:
                    print("Cidade inválida!")
                    continue
                
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
                if escolha_2 not in opcoes_energia:
                    print("Opção inválida!")
                    continue
                
                pesquisa_cidade_grafico_maximos(escolha_1,escolha_2)
                
            elif order == 2:
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
                if escolha_1 not in opcoes_cidade:
                    print("Opção inválida!")
                    continue
                
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
                if escolha_2 not in opcoes_energia:
                    print("Opção inválida!")
                    continue
                
                pesquisa_cidade_grafico_minimos(escolha_1,escolha_2)
                
            elif order == 3:
                #Escolha cidade
                cursor.execute('''SELECT id_city, city_name FROM nome_city''')
                dados = cursor.fetchall()
                
                opcoes = {id_city: city_name for id_city, city_name in dados}
                
                print('='*20)
                print('Escolha uma das seguintes cidades:')
                for id_city, nome in opcoes.items():
                    print(f"{id_city} - {nome}")
    
                escolha_city = int(input('Escolha uma das cidades(Numeros): '))
                if escolha_city not in opcoes:
                    print("Opção inválida!")
                    continue
                
                #Escolha o ano
                cursor.execute('''SELECT pk_id_year, year_name FROM year''')
                dados = cursor.fetchall()
                
                opcoes_year = {pk_id_year: year_name for pk_id_year, year_name in dados}
                
                print('='*20)
                print('Escolha um dos seguintes anos:')
                for pk_id_year, year_name in opcoes_year.items():
                    print(f"{pk_id_year} - {year_name}")
    
                escolha_year = int(input('Escolha um dos anos(Numeros): '))
                if escolha_year not in opcoes_year:
                    print("Opção inválida!")
                    continue
                
                #Função puxada
                grafico_fontes_maximo(escolha_city,escolha_year)
        
        
            elif order == 4:
                #Escolha cidade
                cursor.execute('''SELECT id_city, city_name FROM nome_city''')
                dados = cursor.fetchall()
                
                opcoes = {id_city: city_name for id_city, city_name in dados}
                
                print('='*20)
                print('Escolha uma das seguintes cidades:')
                for id_city, nome in opcoes.items():
                    print(f"{id_city} - {nome}")
    
                escolha_city = int(input('Escolha uma das cidades(Numeros): '))
                if escolha_city not in opcoes:
                    print("Opção inválida!")
                    continue
                
                #Escolha o ano
                cursor.execute('''SELECT pk_id_year, year_name FROM year''')
                dados = cursor.fetchall()
                
                opcoes_year = {pk_id_year: year_name for pk_id_year, year_name in dados}
                
                print('='*20)
                print('Escolha um dos seguintes anos:')
                for pk_id_year, year_name in opcoes_year.items():
                    print(f"{pk_id_year} - {year_name}")
    
                escolha_year = int(input('Escolha um dos anos(Numeros): '))
                if escolha_year not in opcoes_year:
                    print("Opção inválida!")
                    continue
                
                #Função puxada
                grafico_fontes_minimo(escolha_city,escolha_year)
                
                #Tratamento de erros:
        except ValueError:
            print('Coloque um número válido!')
            continue
