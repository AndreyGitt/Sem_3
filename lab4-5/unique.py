class Unique(object):
    def __init__(self, items, **kwargs):
        ignore_case = bool(kwargs.get('ignore_case'))
        self.items = []
        prev_items = set()
        for i in items:
            if ignore_case and i.lower() not in prev_items:
                self.items.append(i)
                prev_items.add(i.lower())
            elif not ignore_case and i not in prev_items:
                self.items.append(i)
                prev_items.add(i)
        self.index = 0

    def __next__(self):
        if self.index < len(self.items):
            res = self.items[self.index]
            self.index += 1
            return res
        raise StopIteration

    def __iter__(self):
        self.index = 0
        return self


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    a = Unique(data1, ignore_case=False)
    print(next(a))
    print(next(a))
    print('-----')
    b = Unique(data2, ignore_case=False)
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print('-----')
    c = Unique(data2, ignore_case=True)
    print(next(c))
    print(next(c))

