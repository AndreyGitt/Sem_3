def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            yield item.get(args[0])
        else:
            filtered_item = {}
            for arg in args:
                if arg in item:
                    filtered_item[arg] = item[arg]
            if len(filtered_item) > 0:
                yield filtered_item

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    for value in field(goods, 'title'):
        print(value)
    print('-----')
    for value in field(goods, 'title', 'price'):
        print(value)
    print('-----')
    for value in field(goods, 'title', 'color'):
        print(value)


