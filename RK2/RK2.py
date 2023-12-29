import unittest
from RK1_refactor import *

class Test_Program(unittest.TestCase):
    # Компьютеры
    comps = [
        Comp(1, 'Имя моего компьютера'),
        Comp(2, 'Мой ноутбук'),
        Comp(3, 'Рабочий компьютер'),

        Comp(11, 'имя (другого) моего компьютеров'),
        Comp(22, 'мой (другой) ноутбук'),
        Comp(33, '(другой) рабочий компьютер'),
    ]

    # Программы
    progs = [
        Prog(1, 'Chrome', '10.02.8', 262444000, 1),  # ~250 MB
        Prog(1, 'Firefox', '11.22.8', 255444000, 1),  # ~250 MB
        Prog(2, 'PyCharm', '12.02.8', 2600354000, 2),  # ~2,5 GB
        Prog(3, 'Adobe', '6.02.8', 8100437000, 3),  # ~7,6 GB
        Prog(4, 'Visual Studio', '1.02.8', 4200967000, 3),  # ~4 GB
        Prog(5, 'LibreOffice', '7.02.8', 419444000, 3),  # ~400 MB
    ]

    progs_comps = [
        ProgComp(1, 1),
        ProgComp(1, 2),
        ProgComp(2, 3),
        ProgComp(3, 4),
        ProgComp(3, 5),
        ProgComp(3, 6),

        ProgComp(11, 1),
        ProgComp(11, 2),
        ProgComp(22, 3),
        ProgComp(33, 4),
        ProgComp(33, 5),
        ProgComp(33, 6),
    ]


    def test_g1(self):
        # Соединение данных один-ко-многим
        one_to_many = [(p.name, p.mem, c.name)
                       for c in comps
                       for p in progs
                       if p.comp_id == c.id]
        self.assertEqual(g1_solution(one_to_many),
                         [('Adobe', 8100437000, 'Рабочий компьютер'), ('Chrome', 262444000, 'Имя моего компьютера'),
                          ('Firefox', 255444000, 'Имя моего компьютера'),
                          ('LibreOffice', 419444000, 'Рабочий компьютер'), ('PyCharm', 2600354000, 'Мой ноутбук'),
                          ('Visual Studio', 4200967000, 'Рабочий компьютер')])
    def test_g2(self):
        one_to_many = [(p.name, p.mem, c.name)
                       for c in comps
                       for p in progs
                       if p.comp_id == c.id]
        self.assertEqual(g2_solution(one_to_many),
                         [('Рабочий компьютер', 3), ('Имя моего компьютера', 2), ('Мой ноутбук', 1)])

    def test_g3(self):
        # Соединение данных многие-ко-многим
        many_to_many_temp = [(c.name, pc.comp_id, pc.prog_id)
                             for c in comps
                             for pc in progs_comps
                             if c.id == pc.comp_id]

        many_to_many = [(p.name, p.mem, comp_name)
                        for comp_name, com_id, prog_id in many_to_many_temp
                        for p in progs if p.id == prog_id]
        self.assertEqual(g3_solution(many_to_many),
                         {'Имя моего компьютера': ['Chrome'], 'Мой ноутбук': ['Adobe'],
                          'Рабочий компьютер': ['LibreOffice'], 'имя (другого) моего компьютеров': ['Chrome'],
                          'мой (другой) ноутбук': ['Adobe'], '(другой) рабочий компьютер': ['LibreOffice']})
if __name__ == '__main__':
    unittest.main()

