from unittest.mock import Mock, patch

import pytest

from patterns.structural.facade import (
    CPU,
    ComputerFacade,
    Memory,
    SolidStateDrive,
)


def test_cpu_methods():
    cpu = CPU()
    # Should not raise errors
    cpu.freeze()
    cpu.jump("0x00")
    cpu.execute()


def test_memory_load():
    memory = Memory()
    # Should not raise errors
    memory.load("0x00", "test data")


def test_solid_state_drive_read():
    ssd = SolidStateDrive()
    result = ssd.read("100", "1024")
    assert isinstance(result, str)
    assert "100" in result
    assert "1024" in result


def test_computer_facade_initialization():
    facade = ComputerFacade()
    assert isinstance(facade.cpu, CPU)
    assert isinstance(facade.memory, Memory)
    assert isinstance(facade.ssd, SolidStateDrive)


def test_computer_facade_start():
    facade = ComputerFacade()
    # Should not raise errors
    facade.start()


def test_computer_facade_start_integrates_components():
    facade = ComputerFacade()
    
    with patch.object(facade.cpu, "freeze") as mock_freeze, \
         patch.object(facade.cpu, "jump") as mock_jump, \
         patch.object(facade.cpu, "execute") as mock_execute, \
         patch.object(facade.memory, "load") as mock_load, \
         patch.object(facade.ssd, "read", return_value="test data") as mock_read:
        
        facade.start()
        
        mock_freeze.assert_called_once()
        mock_read.assert_called_once()
        mock_load.assert_called_once()
        mock_jump.assert_called_once()
        mock_execute.assert_called_once()


def test_facade_encapsulates_complexity():
    facade = ComputerFacade()
    # Start method should handle all the complexity internally
    # without requiring client to know about CPU, Memory, SSD details
    facade.start()

