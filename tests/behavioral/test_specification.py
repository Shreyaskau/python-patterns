import pytest

from patterns.behavioral.specification import (
    AndSpecification,
    CompositeSpecification,
    NotSpecification,
    OrSpecification,
    SuperUserSpecification,
    User,
    UserSpecification,
)


def test_user_specification_with_user():
    spec = UserSpecification()
    user = User()
    assert spec.is_satisfied_by(user) is True


def test_user_specification_with_non_user():
    spec = UserSpecification()
    assert spec.is_satisfied_by("not a user") is False


def test_super_user_specification_with_super_user():
    spec = SuperUserSpecification()
    super_user = User(super_user=True)
    assert spec.is_satisfied_by(super_user) is True


def test_super_user_specification_with_regular_user():
    spec = SuperUserSpecification()
    regular_user = User(super_user=False)
    assert spec.is_satisfied_by(regular_user) is False


def test_and_specification():
    user_spec = UserSpecification()
    super_user_spec = SuperUserSpecification()
    and_spec = user_spec.and_specification(super_user_spec)
    
    assert isinstance(and_spec, AndSpecification)
    
    regular_user = User(super_user=False)
    super_user = User(super_user=True)
    
    assert and_spec.is_satisfied_by(regular_user) is False
    assert and_spec.is_satisfied_by(super_user) is True


def test_or_specification():
    user_spec = UserSpecification()
    super_user_spec = SuperUserSpecification()
    or_spec = user_spec.or_specification(super_user_spec)
    
    assert isinstance(or_spec, OrSpecification)
    
    regular_user = User(super_user=False)
    super_user = User(super_user=True)
    non_user = "not a user"
    
    assert or_spec.is_satisfied_by(regular_user) is True
    assert or_spec.is_satisfied_by(super_user) is True
    assert or_spec.is_satisfied_by(non_user) is False


def test_not_specification():
    user_spec = UserSpecification()
    not_spec = user_spec.not_specification()
    
    assert isinstance(not_spec, NotSpecification)
    
    user = User()
    non_user = "not a user"
    
    assert not_spec.is_satisfied_by(user) is False
    assert not_spec.is_satisfied_by(non_user) is True


def test_complex_specification_chain():
    user_spec = UserSpecification()
    super_user_spec = SuperUserSpecification()
    
    # (User AND SuperUser) OR (NOT User)
    complex_spec = (
        user_spec.and_specification(super_user_spec)
    ).or_specification(user_spec.not_specification())
    
    regular_user = User(super_user=False)
    super_user = User(super_user=True)
    non_user = "not a user"
    
    assert complex_spec.is_satisfied_by(regular_user) is True  # NOT User is True
    assert complex_spec.is_satisfied_by(super_user) is True  # User AND SuperUser is True
    assert complex_spec.is_satisfied_by(non_user) is True  # NOT User is True

