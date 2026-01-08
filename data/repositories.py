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
