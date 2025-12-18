import pytest

from patterns.fundamental.delegation_pattern import Delegator, Delegate


def test_delegate_initialization():
    delegate = Delegate()
    assert delegate.p1 == 123


def test_delegate_do_something():
    delegate = Delegate()
    result = delegate.do_something("nothing")
    assert result == "Doing nothing"


def test_delegate_do_something_with_kw():
    delegate = Delegate()
    result = delegate.do_something("something", kw=", faif!")
    assert result == "Doing something, faif!"


def test_delegator_initialization():
    delegate = Delegate()
    delegator = Delegator(delegate)
    assert delegator.delegate == delegate


def test_delegator_accesses_delegate_attribute():
    delegate = Delegate()
    delegator = Delegator(delegate)
    assert delegator.p1 == 123


def test_delegator_accesses_nonexistent_attribute():
    delegate = Delegate()
    delegator = Delegator(delegate)
    with pytest.raises(AttributeError):
        _ = delegator.p2


def test_delegator_calls_delegate_method():
    delegate = Delegate()
    delegator = Delegator(delegate)
    result = delegator.do_something("nothing")
    assert result == "Doing nothing"


def test_delegator_calls_delegate_method_with_kw():
    delegate = Delegate()
    delegator = Delegator(delegate)
    result = delegator.do_something("something", kw=", faif!")
    assert result == "Doing something, faif!"


def test_delegator_calls_nonexistent_method():
    delegate = Delegate()
    delegator = Delegator(delegate)
    with pytest.raises(AttributeError):
        delegator.do_anything()


def test_delegation_pattern_separation():
    # Test that delegation allows composition over inheritance
    delegate = Delegate()
    delegator = Delegator(delegate)
    
    # Delegator can use delegate's functionality
    assert delegator.p1 == delegate.p1
    assert delegator.do_something("test") == delegate.do_something("test")


def test_multiple_delegators_same_delegate():
    delegate = Delegate()
    delegator1 = Delegator(delegate)
    delegator2 = Delegator(delegate)
    
    assert delegator1.p1 == delegator2.p1
    assert delegator1.do_something("test") == delegator2.do_something("test")

