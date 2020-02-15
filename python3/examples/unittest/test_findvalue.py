#!/usr/bin/env python3

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
