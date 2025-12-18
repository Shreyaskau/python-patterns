import pytest

from patterns.behavioral.chaining_method import Action, Person


def test_person_initialization():
    person = Person("Jack")
    assert person.name == "Jack"


def test_action_initialization():
    action = Action("move")
    assert action.name == "move"


def test_action_amount_returns_self():
    action = Action("move")
    result = action.amount("5m")
    assert result is action


def test_action_stop():
    action = Action("move")
    # Should not raise an error
    action.stop()


def test_chaining_method_pattern():
    move = Action("move")
    person = Person("Jack")
    # Test that chaining works
    result = person.do_action(move)
    assert result is move
    # Test full chain
    chained = person.do_action(move).amount("5m")
    assert chained is move


def test_multiple_chains():
    person = Person("Alice")
    jump = Action("jump")
    
    # Test multiple chains
    result1 = person.do_action(jump).amount("10m")
    assert result1 is jump
    
    run = Action("run")
    result2 = person.do_action(run).amount("100m")
    assert result2 is run

