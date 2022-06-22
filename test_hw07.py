import pytest
import os
import queue
from hw07 import LogWriter, Repeater, RepeaterTwice, SomeErrorExecutor, EmptyCommand
from hw07 import (
    LogWriterEHandler,
    RepeaterEHandler,
    RepeaterTwiceEHandler,
    RepeaterLogWriterEHandler,
    RepeaterTwiceLogWriterEHandler,
)


def test_LogWriter():
    e = ValueError("value_error")
    logwriter = LogWriter(e)
    logwriter.execute()
    with open("log.txt", "r") as file:
        content = file.read()
    expected_content = f"Exception: {repr(e)}\n"
    assert content == expected_content


def test_Repeater():
    e = ValueError("value_error")
    path = "log_test_Repeater.txt"
    logwriter = LogWriter(e, path, mode="w")
    repeater = Repeater(logwriter)
    repeater.execute()
    with open(path, "r") as file:
        content = file.read()
    expected_content = f"Exception: {repr(e)}\n"
    os.remove(path)
    assert content == expected_content


def test_RepeaterTwice():
    e = ValueError("value_error")
    path = "log_test_RepeaterTwice.txt"
    logwriter = LogWriter(e, path, mode="a")
    repeater = RepeaterTwice(logwriter)
    repeater.execute()
    with open(path, "r") as file:
        content = file.read()
    expected_content = f"Exception: {repr(e)}\n" * 2
    os.remove(path)
    assert content == expected_content


def test_Handler():
    e = ValueError("value_error")
    path = "log_test_RepeaterTwice.txt"
    logwriter = LogWriter(e, path, mode="a")
    repeater = RepeaterTwice(logwriter)
    repeater.execute()
    with open(path, "r") as file:
        content = file.read()
    expected_content = f"Exception: {repr(e)}\n" * 2
    os.remove(path)
    assert content == expected_content


def test_LogWriterEHandler():
    command, ex = None, ValueError("value_error")
    LogWriterEHandler().handle(command, ex)
    with open("log.txt", "r") as file:
        content = file.read()
    expected_content = f"Exception: {repr(ex)}\n"
    assert content == expected_content
