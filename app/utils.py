def get_population():
    keys = ['colombia, argentina']
    values = [300,500]
    return keys , values

def population_by_country(data,country):
    result = list(filter(lambda item: item['Country'] == country,data))
    return result
