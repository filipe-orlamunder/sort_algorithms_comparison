import random
import codecs
from abc import ABC, abstractmethod

# Interface da estratégia
class RandomNumberStrategy(ABC):
    @abstractmethod
    def generate_numbers(self, num, start, end):
        pass

# Implementação concreta da estratégia
class UniqueRandomNumberStrategy(RandomNumberStrategy):
    def generate_numbers(self, num, start, end):
        arr = []
        tmp = random.randint(start, end)

        for x in range(num):
            while tmp in arr:
                tmp = random.randint(start, end)
            arr.append(tmp)

        arr.sort()
        return arr

# Classe de contexto
class RandomNumberGenerator:
    def __init__(self, strategy: RandomNumberStrategy):
        self.strategy = strategy

    def create_random_number_list(self, num, start=1, end=100):
        arr = self.strategy.generate_numbers(num, start, end)
        with codecs.open("Data.txt", "w", "utf-8") as file:
            file.write(','.join(map(str, arr)))
        return arr

# Uso do padrão Strategy
strategy = UniqueRandomNumberStrategy()
generator = RandomNumberGenerator(strategy)
print(generator.create_random_number_list(10, 100, 100000))