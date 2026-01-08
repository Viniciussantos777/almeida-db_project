def get_cities(conn):
    query = "SELECT id_city, city_name FROM nome_city"
    return conn.execute(query).fetchall()


def get_energy_fonts(conn):
    query = "SELECT pk_id_en_fo, name_energy FROM energy_font"
    return conn.execute(query).fetchall()


def get_years(conn):
    query = "SELECT pk_id_year, year_name FROM year"
    return conn.execute(query).fetchall()


def get_consumption_by_city_all_years(conn, city_id, energy_id):
    query = """
    SELECT
        year.year_name,
        info.info_consum,
        energy_font.name_energy,
        industry.name_indus,
        clime.name_clime
    FROM info
    JOIN year ON info.pk_id_year = year.pk_id_year
    JOIN energy_font ON info.pk_id_en_fo = energy_font.pk_id_en_fo
    JOIN industry ON info.pk_id_indus = industry.pk_id_indus
    JOIN clime ON info.pk_id_clime = clime.pk_id_clime
    WHERE info.id_city = ? AND info.pk_id_en_fo = ?
    ORDER BY year.year_name ASC
    """
    return conn.execute(query, (city_id, energy_id)).fetchall()


def get_consumption_by_city_one_year(conn, city_id, year_id):
    query = """
    SELECT
        year.year_name,
        info.info_consum,
        energy_font.name_energy,
        industry.name_indus,
        clime.name_clime
    FROM info
    JOIN year ON info.pk_id_year = year.pk_id_year
    JOIN energy_font ON info.pk_id_en_fo = energy_font.pk_id_en_fo
    JOIN industry ON info.pk_id_indus = industry.pk_id_indus
    JOIN clime ON info.pk_id_clime = clime.pk_id_clime
    WHERE info.id_city = ? AND info.pk_id_year = ?
    ORDER BY info.info_consum ASC
    """
    return conn.execute(query, (city_id, year_id)).fetchall()

def get_max_consumption_by_year(conn, city_id, energy_id):
    query = '''
        SELECT y.year_name, MAX(i.info_consum), ef.name_energy
        FROM info AS i
        INNER JOIN year AS y ON i.pk_id_year = y.pk_id_year
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_en_fo = ?
        GROUP BY y.year_name
        ORDER BY y.year_name ASC
    '''
    return conn.execute(query, (city_id, energy_id)).fetchall()

def get_min_consumption_by_year(conn, city_id, energy_id):
    query = '''
        SELECT y.year_name, MIN(i.info_consum), ef.name_energy
        FROM info AS i
        INNER JOIN year AS y ON i.pk_id_year = y.pk_id_year
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_en_fo = ?
        GROUP BY y.year_name
        ORDER BY y.year_name ASC
    '''
    return conn.execute(query, (city_id, energy_id)).fetchall()

def get_max_consumption_by_source(conn, city_id, year_id):
    query = '''
        SELECT ef.name_energy, MAX(i.info_consum)
        FROM info AS i
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_year = ?
        GROUP BY ef.name_energy
        ORDER BY MAX(i.info_consum) DESC
    '''
    return conn.execute(query, (city_id, year_id)).fetchall()

def get_min_consumption_by_source(conn, city_id, year_id):
    query = '''
        SELECT ef.name_energy, MIN(i.info_consum)
        FROM info AS i
        INNER JOIN energy_font AS ef ON i.pk_id_en_fo = ef.pk_id_en_fo
        WHERE i.id_city = ? AND i.pk_id_year = ?
        GROUP BY ef.name_energy
        ORDER BY MIN(i.info_consum) ASC
    '''
    return conn.execute(query, (city_id, year_id)).fetchall()