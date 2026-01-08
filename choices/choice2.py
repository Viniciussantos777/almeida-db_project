import matplotlib.pyplot as plt
from services.energy_services import (
    listar_cidades,
    listar_fontes_energia,
    listar_anos,
    listar_consumo_max_por_ano,
    listar_consumo_min_por_ano,
    listar_consumo_max_por_fonte,
    listar_consumo_min_por_fonte
)

# --- FUNÇÕES DE GRÁFICOS (UI) ---

def pesquisa_cidade_grafico_maximos(escolha_city, escolha_energy):
    # Chama o serviço em vez de usar cursor.execute
    busca = listar_consumo_max_por_ano(escolha_city, escolha_energy)

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

    plt.figure(figsize=(10, 5))
    plt.plot(anos_x, consumo_y, marker='o', linestyle='-', color='darkred', linewidth=2)
    plt.title(f'Peak Consumption per Year - {nome_fonte}')
    plt.xlabel('Years')
    plt.ylabel('Maximum Consumption Value')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.show()


def pesquisa_cidade_grafico_minimos(escolha_city, escolha_energy):
    busca = listar_consumo_min_por_ano(escolha_city, escolha_energy)

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

    plt.figure(figsize=(10, 5))
    plt.plot(anos_x, consumo_min_y, marker='o', linestyle='-', color='orange', linewidth=2)
    plt.title(f'Minimum Consumption per Year - {nome_fonte}')
    plt.xlabel('Years')
    plt.ylabel('Minimum Consumption Value')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()


def grafico_fontes_maximo(escolha_city, escolha_year):
    busca = listar_consumo_max_por_fonte(escolha_city, escolha_year)

    if not busca:
        print("\n[!] NO DATA FOUND FOR THIS CITY AND YEAR.")
        return

    fontes = [row[0] for row in busca]
    consumos_max = [row[1] for row in busca]

    plt.figure(figsize=(12, 7))
    cores = ['#2c3e50', '#e67e22', '#27ae60', '#2980b9', '#8e44ad', '#c0392b']
    barras = plt.bar(fontes, consumos_max, color=cores)

    for barra in barras:
        height = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., height + 0.5,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold')

    plt.title(f'Peak Energy Consumption by Source\nCity ID: {escolha_city} | Year ID: {escolha_year}', fontsize=14)
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()


def grafico_fontes_minimo(escolha_city, escolha_year):
    busca = listar_consumo_min_por_fonte(escolha_city, escolha_year)

    if not busca:
        print("\n[!] NO DATA FOUND FOR THIS SELECTION.")
        return

    fontes = [row[0] for row in busca]
    consumos_min = [row[1] for row in busca]

    plt.figure(figsize=(12, 7))
    cores = ['#34495e', '#16a085', '#27ae60', '#2980b9', '#3498db', '#1abc9c']
    barras = plt.bar(fontes, consumos_min, color=cores)

    for barra in barras:
        height = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., height + 0.2,
                 f'{int(height)}', ha='center', va='bottom', fontsize=10)

    plt.title(f'Minimum Energy Consumption by Source\nCity ID: {escolha_city} | Year ID: {escolha_year}', fontsize=14)
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()


# --- MENU PRINCIPAL (ENTRY POINT DA UI) ---

def initial_choice2():
    while True:
        print('\n' + '='*30)
        print('    CHART DASHBOARD')
        print('[1] City (Max consumption x Year)')
        print('[2] City (Min consumption x Year)')
        print('[3] Max consumption per Energy Source')
        print('[4] Min consumption per Energy Source')
        print('[5] Exit')
        print('='*30)
        
        try:
            order = int(input('Select an option: '))
            
            if order == 5:
                print('Returning to main menu...')
                break
            
            # OPÇÃO 1 e 2: Precisam de Cidade e Fonte de Energia
            if order in [1, 2]:
                # Listar Cidades usando o Service
                dados_cidade = listar_cidades()
                opcoes_cidade = {id_c: nome for id_c, nome in dados_cidade}
                
                print('\nAvailable Cities:')
                for id_c, nome in opcoes_cidade.items():
                    print(f"{id_c} - {nome}")
                
                escolha_city = int(input('Choose City ID: '))
                if escolha_city not in opcoes_cidade:
                    print("Invalid City!")
                    continue

                # Listar Fontes usando o Service
                dados_energia = listar_fontes_energia()
                opcoes_energia = {id_e: nome for id_e, nome in dados_energia}
                
                print('\nAvailable Energy Sources:')
                for id_e, nome in opcoes_energia.items():
                    print(f"{id_e} - {nome}")
                
                escolha_energy = int(input('Choose Source ID: '))
                if escolha_energy not in opcoes_energia:
                    print("Invalid Source!")
                    continue

                if order == 1:
                    pesquisa_cidade_grafico_maximos(escolha_city, escolha_energy)
                else:
                    pesquisa_cidade_grafico_minimos(escolha_city, escolha_energy)

            # OPÇÃO 3 e 4: Precisam de Cidade e Ano
            elif order in [3, 4]:
                # Listar Cidades
                dados_cidade = listar_cidades()
                opcoes_cidade = {id_c: nome for id_c, nome in dados_cidade}
                
                for id_c, nome in opcoes_cidade.items():
                    print(f"{id_c} - {nome}")
                
                escolha_city = int(input('Choose City ID: '))
                if escolha_city not in opcoes_cidade:
                    print("Invalid City!")
                    continue

                # Listar Anos
                dados_anos = listar_anos()
                opcoes_year = {id_y: nome for id_y, nome in dados_anos}
                
                print('\nAvailable Years:')
                for id_y, nome in opcoes_year.items():
                    print(f"{id_y} - {nome}")
                
                escolha_year = int(input('Choose Year ID: '))
                if escolha_year not in opcoes_year:
                    print("Invalid Year!")
                    continue

                if order == 3:
                    grafico_fontes_maximo(escolha_city, escolha_year)
                else:
                    grafico_fontes_minimo(escolha_city, escolha_year)

        except ValueError:
            print('Please, enter a valid number!')
            continue