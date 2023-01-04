from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self, stretch=False):
        self.dogs = Queue()
        self.cats = Queue()
        self.stretch = stretch

        if stretch:
            self.animals = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cats.enqueue(animal)
        else:
            self.dogs.enqueue(animal)

    def dequeue(self, pref=""):
        if pref == "cat":
            return self.cats.dequeue()
        elif pref == "dog":
            return self.dogs.dequeue()


class Dog:
    def __repr__(self):
        return

class Cat:
    def __repr__(self):
        return
