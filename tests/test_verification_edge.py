"""Tests for verification edge distinct"""

def test_verification_edge_0():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15

def test_verification_edge_1():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15

def test_verification_edge_2():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15

def test_verification_edge_3():
    claim={"birth_year":1990,"year":1985,"event":"war"}
    assert claim["year"] - claim["birth_year"] < 15
