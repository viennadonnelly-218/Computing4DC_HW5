import random 
import math 
from abc import ABCMeta, abstractmethod

#########################
# 1

class Patient:
    def __init__(self, name: str, symptoms: list[str]):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}
        
    def add_test(self, test: str, results: bool):
        self.tests[test] = results
    
    def has_covid(self) -> float:
        if "covid" in self.tests:
            if self.tests["covid"]:
                prob = 0.99
            else:
                prob = 0.01
        else:
            prob = 0.05
            covid_symptoms = ['fever', 'cough', 'anosmia']
            for c_symptom in covid_symptoms:
                if c_symptom in self.symptoms:
                    prob += 0.1
        return round(prob ,2)
        # returning the rounded value because instructions specify to return 0.99, 0.01, etc...
            
    
######################

# 2
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
                
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) > 0:
            card = self.cards.pop(0)
            print(card.value, "of", card.suit)
        else:
            print("There are no cards in this deck")
                


###################
# 3

class PlaneFigure (metaclass=ABCMeta):
    @abstractmethod
    def compute_perimeter(self):
        return NotImplementedError
    
    @abstractmethod
    def compute_surface(self):
        return NotImplementedError
    
class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h
    def compute_perimeter(self):
        return self.base + self.c1 + self.c2
    def compute_surface(self):
        return (0.5 * self.base) * self.h
    
class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def compute_perimeter(self):
        return 2 * self.a + 2 * self.b
    def compute_surface(self):
        return self.a * self.b
    
    
class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return 2 * math.pi * self.radius
    def compute_surface(self):
        return math.pi * self.radius**2
    
    