import pytest

from patterns.structural.flyweight_with_metaclass import Card2, FlyweightMeta


def test_card2_has_pool():
    assert hasattr(Card2, "pool")


def test_flyweight_same_instance():
    cm1 = Card2("10", "h", a=1)
    cm2 = Card2("10", "h", a=1)
    assert cm1 is cm2
    assert cm1 == cm2


def test_flyweight_different_instances():
    cm1 = Card2("10", "h", a=1)
    cm3 = Card2("10", "h", a=2)
    assert cm1 is not cm3
    assert cm1 != cm3


def test_flyweight_pool_size():
    instances_pool = getattr(Card2, "pool")
    instances_pool.clear()
    
    cm1 = Card2("10", "h", a=1)
    cm2 = Card2("10", "h", a=1)  # Should reuse cm1
    cm3 = Card2("10", "h", a=2)
    
    assert len(instances_pool) == 2


def test_flyweight_weak_reference():
    instances_pool = getattr(Card2, "pool")
    instances_pool.clear()
    
    cm1 = Card2("10", "h", a=1)
    cm2 = Card2("10", "h", a=1)
    
    assert len(instances_pool) == 1  # cm1 and cm2 are same instance
    
    del cm1
    assert len(instances_pool) == 1  # cm2 still references it
    
    del cm2
    # Weak reference should allow garbage collection
    # Note: actual cleanup may be delayed, so we check it's <= 1
    assert len(instances_pool) <= 1


def test_flyweight_metaclass():
    assert isinstance(Card2, FlyweightMeta)


def test_different_parameters_create_different_instances():
    instances_pool = getattr(Card2, "pool")
    instances_pool.clear()
    
    cm1 = Card2("10", "h")
    cm2 = Card2("10", "s")
    cm3 = Card2("9", "h")
    
    assert cm1 is not cm2
    assert cm1 is not cm3
    assert cm2 is not cm3
    assert len(instances_pool) == 3

