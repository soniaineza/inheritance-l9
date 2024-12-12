from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk")
class snake(animal):
    def move(self):
        print("i can crawl")
a=human()
a.move()
b=snake()
b.move()