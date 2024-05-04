import utils

data = [
    {
        'Country': 'Argentina',
        'Population': '1233131'
    },
    {
        'Country': 'Colombia',
        'Population': '332311'
    }
]


def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input('Type country => ')

    result = utils.population_by_country(data, country)
    print(result)
if __name__ == '__main__':
    run()