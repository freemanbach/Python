#!/usr/bin/env python3
# /Users/hobbit/Library/Python/3.7/bin/pytest -v test_findvalue.py
# https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
# https://pediaa.com/difference-between-cloud-computing-and-distributed-computing/
import findvalue
import pytest

def test_findLarge():
    val = findvalue.findLarge(1,4,6)
    assert val == 4

def test_findLarge():
    val = findvalue.findLarge(8,4,6)
    assert val == 8

def test_findLarge():
    val = findvalue.findLarge(20,5,60)
    assert val == 60
    
def test_findSmall():
    val = findvalue.findSmall(1,4,6)
    assert val == 1

def test_findSmall():
    val = findvalue.findSmall(8,4,6)
    assert val == 4

def test_findSmall():
    val = findvalue.findSmall(20,5,60)
    assert val == 5
