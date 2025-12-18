import pytest

from patterns.behavioral.command import (
    DeleteFileCommand,
    HideFileCommand,
    MenuItem,
)


def test_hide_file_command_execute():
    command = HideFileCommand()
    command.execute("test-file")
    assert len(command._hidden_files) == 1
    assert command._hidden_files[0] == "test-file"


def test_hide_file_command_undo():
    command = HideFileCommand()
    command.execute("test-file")
    command.undo()
    assert len(command._hidden_files) == 0


def test_delete_file_command_execute():
    command = DeleteFileCommand()
    command.execute("test-file")
    assert len(command._deleted_files) == 1
    assert command._deleted_files[0] == "test-file"


def test_delete_file_command_undo():
    command = DeleteFileCommand()
    command.execute("test-file")
    command.undo()
    assert len(command._deleted_files) == 0


def test_menu_item_with_hide_command():
    command = HideFileCommand()
    menu_item = MenuItem(command)
    menu_item.on_do_press("test-file")
    assert len(command._hidden_files) == 1


def test_menu_item_with_delete_command():
    command = DeleteFileCommand()
    menu_item = MenuItem(command)
    menu_item.on_do_press("test-file")
    assert len(command._deleted_files) == 1


def test_menu_item_undo():
    hide_command = HideFileCommand()
    menu_item = MenuItem(hide_command)
    menu_item.on_do_press("test-file")
    menu_item.on_undo_press()
    assert len(hide_command._hidden_files) == 0


def test_multiple_commands():
    hide_command = HideFileCommand()
    delete_command = DeleteFileCommand()
    
    hide_item = MenuItem(hide_command)
    delete_item = MenuItem(delete_command)
    
    hide_item.on_do_press("file1")
    delete_item.on_do_press("file2")
    
    assert len(hide_command._hidden_files) == 1
    assert len(delete_command._deleted_files) == 1


def test_command_undo_order():
    command = HideFileCommand()
    command.execute("file1")
    command.execute("file2")
    command.execute("file3")
    
    command.undo()  # Should undo file3
    assert len(command._hidden_files) == 2
    assert command._hidden_files[-1] == "file2"
    
    command.undo()  # Should undo file2
    assert len(command._hidden_files) == 1
    assert command._hidden_files[-1] == "file1"

