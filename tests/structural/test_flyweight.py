import pytest

from patterns.structural.flyweight import Card


def test_card_creation():
    card = Card("9", "h")
    assert card.value == "9"
    assert card.suit == "h"


def test_card_repr():
    card = Card("9", "h")
    assert repr(card) == "<Card: 9h>"


def test_flyweight_same_instance():
    c1 = Card("9", "h")
    c2 = Card("9", "h")
    assert c1 is c2
    assert c1 == c2


def test_flyweight_different_cards():
    c1 = Card("9", "h")
    c2 = Card("10", "h")
    assert c1 is not c2
    assert c1 != c2


def test_flyweight_shared_state():
    c1 = Card("9", "h")
    c1.new_attr = "temp"
    c2 = Card("9", "h")
    assert hasattr(c2, "new_attr")
    assert c2.new_attr == "temp"


def test_flyweight_pool_clearing():
    c1 = Card("9", "h")
    c1.new_attr = "temp"
    
    Card._pool.clear()
    
    c2 = Card("9", "h")
    assert not hasattr(c2, "new_attr")


def test_multiple_cards():
    c1 = Card("9", "h")
    c2 = Card("9", "s")
    c3 = Card("10", "h")
    
    assert c1 is not c2  # Different suit
    assert c1 is not c3  # Different value
    assert c2 is not c3  # Different value and suit


def test_flyweight_pool_size():
    Card._pool.clear()
    
    Card("9", "h")
    Card("9", "h")  # Should reuse
    Card("10", "h")
    
    # Should have 2 unique cards
    assert len(Card._pool) == 2

