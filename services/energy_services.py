from choices.connect_db import connect
from data.repositories import (
    get_cities,
    get_energy_fonts,
    get_years,
    get_consumption_by_city_all_years,
    get_consumption_by_city_one_year
)


def listar_cidades():
    conn, _ = connect()
    dados = get_cities(conn)
    conn.close()
    return dados


def listar_fontes_energia():
    conn, _ = connect()
    dados = get_energy_fonts(conn)
    conn.close()
    return dados


def listar_anos():
    conn, _ = connect()
    dados = get_years(conn)
    conn.close()
    return dados


def consumo_por_cidade_all_years(city_id, energy_id):
    conn, _ = connect()
    dados = get_consumption_by_city_all_years(conn, city_id, energy_id)
    conn.close()
    return dados


def consumo_por_cidade_one_year(city_id, year_id):
    conn, _ = connect()
    dados = get_consumption_by_city_one_year(conn, city_id, year_id)
    conn.close()
    return dados
