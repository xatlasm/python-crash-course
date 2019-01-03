#City Names
def city_country(city, country):
    """Pairs a city with a country"""
    return city.title() + ', ' + country.title()
result = city_country('tokyo', 'japan')
print(result)