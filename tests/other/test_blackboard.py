import random

import pytest

from patterns.other.blackboard import (
    AbstractExpert,
    Blackboard,
    Controller,
    Professor,
    Scientist,
    Student,
)


def test_blackboard_initialization():
    blackboard = Blackboard()
    assert blackboard.experts == []
    assert blackboard.common_state["problems"] == 0
    assert blackboard.common_state["suggestions"] == 0
    assert blackboard.common_state["contributions"] == []
    assert blackboard.common_state["progress"] == 0


def test_blackboard_add_expert():
    blackboard = Blackboard()
    student = Student(blackboard)
    blackboard.add_expert(student)
    assert len(blackboard.experts) == 1
    assert student in blackboard.experts


def test_student_initialization():
    blackboard = Blackboard()
    student = Student(blackboard)
    assert student.blackboard == blackboard


def test_student_is_eager_to_contribute():
    blackboard = Blackboard()
    student = Student(blackboard)
    assert student.is_eager_to_contribute is True


def test_student_contribute():
    random.seed(1234)
    blackboard = Blackboard()
    student = Student(blackboard)
    initial_problems = blackboard.common_state["problems"]
    initial_suggestions = blackboard.common_state["suggestions"]
    initial_progress = blackboard.common_state["progress"]
    
    student.contribute()
    
    assert blackboard.common_state["problems"] > initial_problems
    assert blackboard.common_state["suggestions"] > initial_suggestions
    assert blackboard.common_state["progress"] > initial_progress
    assert "Student" in blackboard.common_state["contributions"]


def test_scientist_initialization():
    blackboard = Blackboard()
    scientist = Scientist(blackboard)
    assert scientist.blackboard == blackboard


def test_scientist_is_eager_to_contribute():
    blackboard = Blackboard()
    scientist = Scientist(blackboard)
    # Can be 0 or 1
    assert scientist.is_eager_to_contribute in [0, 1]


def test_scientist_contribute():
    random.seed(1234)
    blackboard = Blackboard()
    scientist = Scientist(blackboard)
    initial_problems = blackboard.common_state["problems"]
    
    scientist.contribute()
    
    assert blackboard.common_state["problems"] > initial_problems
    assert "Scientist" in blackboard.common_state["contributions"]


def test_professor_initialization():
    blackboard = Blackboard()
    professor = Professor(blackboard)
    assert professor.blackboard == blackboard


def test_professor_is_eager_when_problems_high():
    blackboard = Blackboard()
    blackboard.common_state["problems"] = 150
    professor = Professor(blackboard)
    assert professor.is_eager_to_contribute is True


def test_professor_not_eager_when_problems_low():
    blackboard = Blackboard()
    blackboard.common_state["problems"] = 50
    professor = Professor(blackboard)
    assert professor.is_eager_to_contribute is False


def test_professor_contribute():
    random.seed(1234)
    blackboard = Blackboard()
    blackboard.common_state["problems"] = 150
    professor = Professor(blackboard)
    initial_progress = blackboard.common_state["progress"]
    
    professor.contribute()
    
    assert blackboard.common_state["progress"] > initial_progress
    assert "Professor" in blackboard.common_state["contributions"]


def test_controller_initialization():
    blackboard = Blackboard()
    controller = Controller(blackboard)
    assert controller.blackboard == blackboard


def test_controller_run_loop():
    random.seed(1234)
    blackboard = Blackboard()
    blackboard.add_expert(Student(blackboard))
    blackboard.add_expert(Scientist(blackboard))
    blackboard.add_expert(Professor(blackboard))
    
    controller = Controller(blackboard)
    contributions = controller.run_loop()
    
    assert blackboard.common_state["progress"] >= 100
    assert len(contributions) > 0
    assert isinstance(contributions, list)


def test_abstract_expert():
    with pytest.raises(TypeError):
        AbstractExpert(None)  # Cannot instantiate abstract class

