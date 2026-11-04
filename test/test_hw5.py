import pytest

from computing4dc_hw5 import hw5

# tests for Q1 below, patient class

def test_patient_default_covid_risk():
    # initialise a patient with no symptoms
    dobby = hw5.Patient(name="Dobby", symptoms=["long nose", "big ears"])    
    # a default patient with no symptoms should have a 0.05 probability of having covid
    assert dobby.has_covid() == pytest.approx(0.05)

def test_patient_symptoms():
    # now lets add some symptomps
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.symptoms += ["fever", "cough"]
    assert dobby.has_covid() == pytest.approx(0.25)  # +0.1 for each symptom

def test_patient_covid_test():
    # add a positive test!
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.add_test("covid", True)
    assert dobby.has_covid() == pytest.approx(0.99)

def test_patient_covid_test_negative():
    # now add an all-clear
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.add_test("covid", False)
    assert dobby.has_covid() == pytest.approx(0.01)

def test_patient_non_covid_test():
    # add a non-covid test
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.add_test("flu", True)
    assert dobby.has_covid() == pytest.approx(0.05)  # should not affect covid probability

# tests for Q2 - the card & the deck

def test_card_stores_suit_and_value():
    # q2.1: the constructor stores both parameters as attributes
    card = hw5.Card(suit="Hearts", value="A")
    assert card.suit == "Hearts"
    assert card.value == "A"

def test_deck_init_properties():
    deck = hw5.Deck()
    assert len(deck.cards) == 52
    assert all(isinstance(card, hw5.Card) for card in deck.cards)

def test_deck_shuffle():
    deck = hw5.Deck()
    original_order = deck.cards.copy()
    first_card = deck.cards[0]
    deck.shuffle()
    assert deck.cards != original_order  # after shuffle, order should change
    assert deck.cards[0] != first_card  # first card should not be the same
    assert first_card in deck.cards  # but all cards should still be present

def test_deck_draw():
    deck = hw5.Deck()
    initial_count = len(deck.cards)
    drawn_card = deck.draw()
    assert isinstance(drawn_card, hw5.Card)
    assert len(deck.cards) == initial_count - 1  # one card should be removed

def test_deck_draw_empty():
    deck = hw5.Deck()
    # draw all cards
    for _ in range(52):
        deck.draw()
    # now the deck should be empty
    assert len(deck.cards) == 0
    # drawing from empty deck prints a message and returns None
    assert deck.draw() is None


## now onto q3 :)

def test_shapes_inherit_from_planefigure():
    # q3.2-3.3: every shape is a child of PlaneFigure
    shapes = [hw5.Triangle(base=3, c1=4, c2=5, h=2), hw5.Rectangle(a=4, b=5), hw5.Circle(radius=2)]
    assert all(isinstance(shape, hw5.PlaneFigure) for shape in shapes)

def test_triangle_perimeter():
    # let's do a triangle
    triangle = hw5.Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_perimeter() == pytest.approx(12)  

def test_triangle_surface():
    triangle = hw5.Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_surface() == pytest.approx(3)  # (base * height) / 2

def test_rectangle_perimeter():
    rectangle = hw5.Rectangle(a=4, b=5)
    assert rectangle.compute_perimeter() == pytest.approx(18)  # 2*(a+b)

def test_rectangle_surface():
    rectangle = hw5.Rectangle(a=4, b=5)
    assert rectangle.compute_surface() == pytest.approx(20)  # a*b

def test_circle_perimeter():
    circle = hw5.Circle(radius=2)
    assert round(circle.compute_perimeter(), 2) == pytest.approx(12.57)  # 2*pi*r

def test_circle_surface():
    circle = hw5.Circle(radius=2)
    assert round(circle.compute_surface(), 2) == pytest.approx(12.57)  # pi*r^2