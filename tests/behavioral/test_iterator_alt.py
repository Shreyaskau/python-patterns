import pytest

from patterns.behavioral.iterator_alt import NumberWords


def test_number_words_initialization():
    nw = NumberWords(1, 5)
    assert nw.start == 1
    assert nw.stop == 5


def test_number_words_iteration():
    nw = NumberWords(1, 2)
    result = list(nw)
    assert result == ["one", "two"]


def test_number_words_full_range():
    nw = NumberWords(1, 5)
    result = list(nw)
    assert result == ["one", "two", "three", "four", "five"]


def test_number_words_partial_range():
    nw = NumberWords(2, 4)
    result = list(nw)
    assert result == ["two", "three", "four"]


def test_number_words_single_value():
    nw = NumberWords(1, 1)
    result = list(nw)
    assert result == ["one"]


def test_number_words_stop_iteration():
    nw = NumberWords(1, 5)
    iterator = iter(nw)
    # Consume all items
    list(iterator)
    # Next call should raise StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_number_words_exceeds_maximum():
    nw = NumberWords(1, 10)  # Only 5 words available
    result = list(nw)
    assert result == ["one", "two", "three", "four", "five"]


def test_number_words_start_greater_than_stop():
    nw = NumberWords(3, 2)
    result = list(nw)
    assert result == []


def test_number_words_is_iterable():
    nw = NumberWords(1, 3)
    assert hasattr(nw, "__iter__")
    assert hasattr(nw, "__next__")

