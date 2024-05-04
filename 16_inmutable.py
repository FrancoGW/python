items = [
    {
        'producto' : 'camisa',
        'precio': 100
    },
    {
        'producto' : 'pantalones',
        'precio': 300
    },
    {
        'producto' : 'pantalones 2 ',
        'precio': 200
    }
]


def add_taxes(item) : 
    new_item = item.copy()
    new_item['taxes'] = new_item['precio'] * .19
    return new_item

new_items = list(map(add_taxes,items))
print('lista nueva')
print(new_items)
print('lista vieja')
print(items)