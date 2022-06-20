class Tomato:
    states = {0: 'green', 1: 'brown', 2: 'red'}
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        for key, value in Tomato.states.items():
            if self._state == value and not self.is_ripe():
                self._state = Tomato.states[key + 1]
                break

    def is_ripe(self):
        if self._state == 'red':
            return True

class TomatoBush(Tomato):
    def __init__(self, count):
        tomatoesList = list()
        for i in range(count):
            tomatoesList.append(Tomato(i))
        self.tomatoes = tomatoesList

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        ripe_count = 0
        for i in self.tomatoes:
            if i.is_ripe():
                ripe_count += 1
        if ripe_count == len(self.tomatoes):
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, bush):
        self.name = name
        bushik = TomatoBush(0)
        bushik = bush
        self._plant = bushik

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай с куста собран')
        else:
            print('Еще не весь куст созрел')

    @staticmethod
    def knowledge_base():
        print('СПРАВКА: Садоводство - "Посади, вырости и продай"')

Gardener.knowledge_base()
bush1 = TomatoBush(5)
Genka = Gardener('Геннадий', bush1)
Genka.work()
Genka.harvest()
while bush1.all_are_ripe() == False:
    Genka.work()
Genka.harvest()
