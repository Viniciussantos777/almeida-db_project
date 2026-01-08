from data.connect_db import connect_db
from data.repositories import (
    get_cities,
    get_energy_fonts,
    get_years,
    get_consumption_by_city_all_years,
    get_consumption_by_city_one_year
)


def listar_cidades():
    conn, _ = connect_db()
    dados = get_cities(conn)
    conn.close()
    return dados


def listar_fontes_energia():
    conn, _ = connect_db()
    dados = get_energy_fonts(conn)
    conn.close()
    return dados


def listar_anos():
    conn, _ = connect_db()
    dados = get_years(conn)
    conn.close()
    return dados


def consumo_por_cidade_all_years(city_id, energy_id):
    conn, _ = connect_db()
    dados = get_consumption_by_city_all_years(conn, city_id, energy_id)
    conn.close()
    return dados


def consumo_por_cidade_one_year(city_id, year_id):
    conn, _ = connect_db()
    dados = get_consumption_by_city_one_year(conn, city_id, year_id)
    conn.close()
    return dados

# Adicione as novas funções do repository no import lá no topo:
from data.repositories import (
    # ... as que já existiam,
    get_max_consumption_by_year,
    get_min_consumption_by_year,
    get_max_consumption_by_source,
    get_min_consumption_by_source
)

def listar_consumo_max_por_ano(city_id, energy_id):
    conn, _ = connect_db()
    dados = get_max_consumption_by_year(conn, city_id, energy_id)
    conn.close()
    return dados

def listar_consumo_min_por_ano(city_id, energy_id):
    conn, _ = connect_db()
    dados = get_min_consumption_by_year(conn, city_id, energy_id)
    conn.close()
    return dados

def listar_consumo_max_por_fonte(city_id, year_id):
    conn, _ = connect_db()
    dados = get_max_consumption_by_source(conn, city_id, year_id)
    conn.close()
    return dados

def listar_consumo_min_por_fonte(city_id, year_id):
    conn, _ = connect_db()
    dados = get_min_consumption_by_source(conn, city_id, year_id)
    conn.close()
    return dados