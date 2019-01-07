def city_country(city, country, population=''):
    """Generates formatted city-country string"""
    if population:
        formatted_city_country = city.title() + ', ' + country.title() + \
        ' - population ' + str(population)
    else:
        formatted_city_country = city.title() + ', ' + country.title()
        
    return formatted_city_country