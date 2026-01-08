from services.energy_services import (
    listar_cidades,
    listar_fontes_energia,
    listar_anos,
    consumo_por_cidade_all_years,
    consumo_por_cidade_one_year
)


def mostrar_tabela(dados):
    print('-' * 75)
    print(f"{'YEAR':<10} | {'CONSUM(MWh)':<12} | {'EN.FONT':<15} | {'INDUSTRY':<20} | {'CLIME':<15}")
    print('-' * 75)

    for ano, consumo, fonte, industria, clima in dados:
        print(f"{ano:<10} | {consumo:<12} | {fonte:<15} | {industria:<20} | {clima:<15}")

    if not dados:
        print("NONE REGISTER FOUND WITH THIS PRESCRIPTIONS!")

    input("\nTAP 'enter' to continue:")


def initial_choice1():
    while True:
        print('=' * 20)
        print('Choose the type of search:')
        print('[1] Per City (All years)')
        print('[2] Per City (Only one year)')
        print('[3] Exit')

        try:
            order = int(input('Put here your choice: '))

            if order == 3:
                break

            elif order == 1:
                cidades = listar_cidades()
                for cid, nome in cidades:
                    print(f"{cid} - {nome}")
                city_id = int(input('Choose city: '))

                fontes = listar_fontes_energia()
                for fid, nome in fontes:
                    print(f"{fid} - {nome}")
                energy_id = int(input('Choose energy source: '))

                dados = consumo_por_cidade_all_years(city_id, energy_id)
                mostrar_tabela(dados)

            elif order == 2:
                cidades = listar_cidades()
                for cid, nome in cidades:
                    print(f"{cid} - {nome}")
                print("=-"*20)
                city_id = int(input('Choose city: '))

                anos = listar_anos()
                for aid, ano in anos:
                    print(f"{aid} - {ano}")
                print("=-"*20)
                year_id = int(input('Choose year: '))

                dados = consumo_por_cidade_one_year(city_id, year_id)
                mostrar_tabela(dados)

        except ValueError:
            print('Coloque um número válido!')
