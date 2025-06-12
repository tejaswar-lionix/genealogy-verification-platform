"""Tests for verification core distinct"""

def test_verification_core_0():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15

def test_verification_core_1():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15

def test_verification_core_2():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15

def test_verification_core_3():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15
