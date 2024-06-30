
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        name = args[0]
        ob = super().__new__(cls)
        cls.houses_history.append(name)
        return ob
    def __init__(self, gk, d):
        self.gk = gk
        self.d = d
    def __del__(self):
         print(f'{self.gk} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)

