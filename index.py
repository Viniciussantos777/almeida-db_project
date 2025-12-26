import sqlite3
import pandas as pd


df = pd.read_csv('base_limpa.csv')
conexao = sqlite3.connect('almeida_db_project.db')
cursor = conexao.cursor()

colunas_chaves = ['Cidade', 'Ano', 'Fonte Energia', 'Indústria Predominante', 'Clima']


df = df.drop_duplicates(subset=colunas_chaves, keep='first')



def gerar_mapeamento(coluna):
    valores_unicos = df[coluna].unique()
    return {nome: i + 1 for i, nome in enumerate(valores_unicos)}

map_cidade = gerar_mapeamento('Cidade')
map_ano = gerar_mapeamento('Ano')
map_fonte = gerar_mapeamento('Fonte Energia')
map_industria = gerar_mapeamento('Indústria Predominante')
map_clima = gerar_mapeamento('Clima')


df_ids = df.copy()
df_ids['Cidade'] = df_ids['Cidade'].map(map_cidade)
df_ids['Ano'] = df_ids['Ano'].map(map_ano)
df_ids['Fonte Energia'] = df_ids['Fonte Energia'].map(map_fonte)
df_ids['Indústria Predominante'] = df_ids['Indústria Predominante'].map(map_industria)
df_ids['Clima'] = df_ids['Clima'].map(map_clima)


lista_para_db = list(df_ids.itertuples(index=False, name=None))


cursor.executemany('''
    INSERT OR IGNORE INTO info(
        id_city, pk_id_year, pk_id_en_fo, pk_id_indus, pk_id_clime, 
        info_consum, cost_unit, emissions, energy_renew, 
        affect_houses, invest_infra, emission_infra, population
    ) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', lista_para_db)

conexao.commit()
conexao.close()

print(f"Processamento concluído. {len(lista_para_db)} linhas únicas inseridas.")







'''
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
'''