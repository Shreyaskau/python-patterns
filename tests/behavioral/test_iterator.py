import pytest

from patterns.behavioral.iterator import count_to, count_to_five, count_to_two


def test_count_to_two():
    result = count_to_two()
    assert list(result) == ["one", "two"]


def test_count_to_five():
    result = count_to_five()
    assert list(result) == ["one", "two", "three", "four", "five"]


def test_count_to_with_different_values():
    assert list(count_to(1)) == ["one"]
    assert list(count_to(3)) == ["one", "two", "three"]
    assert list(count_to(5)) == ["one", "two", "three", "four", "five"]


def test_count_to_zero():
    result = count_to(0)
    assert list(result) == []


def test_count_to_greater_than_five():
    result = count_to(10)
    assert list(result) == ["one", "two", "three", "four", "five"]


def test_iterator_consumption():
    result = count_to_two()
    first_list = list(result)
    second_list = list(result)  # Generator is consumed
    assert first_list == ["one", "two"]
    assert second_list == []


def test_count_to_is_generator():
    result = count_to(2)
    assert hasattr(result, "__iter__")
    assert hasattr(result, "__next__")

