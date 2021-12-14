class Tomato:
    states = {
        1: 'зеленый',
        2: 'молочный',
        3: 'бурый',
        4: 'розовый',
        5: 'созрел'
    }

    def __init__(self, index):
        self._index = index
        self.i = 1
        self._state = self.states[self.i]

    def grow(self):
        if self.i < 5:
            self.i += 1
            self._state = self.states[self.i]
            print(f'Текущая стадия : {self._state}')
        else:
            raise ValueError('Помидор созрел, дальше растить нельзя')

    def is_ripe(self):
        if self._state == 'созрел':
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, var):
        self.tomatoes = [Tomato(index) for index in range(0, var)]

    def grow_all(self):
        for _ in self.tomatoes:
            _.grow()

    def all_are_ripe(self):
        for _ in self.tomatoes:
            if all([_.is_ripe() for i in self.tomatoes]) is True:
                print('Все помидоры созрели')
                return True
            else:
                return False


class Gardener:

    def __init__(self, name, var):
        self.name = name
        self._plant = var

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe() is True:
            print(f'Все растения созрели. {self.name} собрал урожай.')
            self._plant.tomatoes.clear()
        else:
            print(f'Помидоры садовника {self.name} еще не дозрели')

    def knowledge_base(self):
        print(f'Справка по садоводству:\n'
              f'Садовник : {self.name}\n'
              f'Количество помидоров на кусте: {len(self._plant.tomatoes)}')
        for i in self._plant.tomatoes:
            print(f'Текущая стадия помидора: {i._state}')


Pomidornii_Kust = TomatoBush(4)
Richard = Gardener('Richard', Pomidornii_Kust)
Richard.knowledge_base()

Richard.harvest()
Richard.work()
Richard.work()
Richard.knowledge_base()
Richard.work()
Richard.harvest()
Richard.work()
Richard.harvest()
Richard.knowledge_base()