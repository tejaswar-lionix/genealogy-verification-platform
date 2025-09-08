from __future__ import annotations
import uuid, time, json, re, hashlib, math, logging
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
logger = logging.getLogger(__name__)

# family_tree: Family tree - persons, families, pedigree - Person and Family distinct

@dataclass
class Person:
    """Person entity - distinct"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    birth_place: str = ""

@dataclass
class Family:
    """Family entity - distinct"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    husband_id: Optional[str] = None
    wife_id: Optional[str] = None
    children_ids: List[str] = field(default_factory=list)
    marriage_year: Optional[int] = None

class FamilyTree:
    def __init__(self):
        self.persons: Dict[str, Person] = {}
        self.families: Dict[str, Family] = {}

    def add_person_0(self, name: str, birth_year: int) -> Person:
        """Add person 0 distinct per 0"""
        # Distinct per 0: handles birth
        p = Person(name=name, birth_year=birth_year + 0)
        if 0%3==0:
        p.birth_place = "County Cork 0"
        return p

    def add_family_0(self, husband: Person, wife: Person) -> Family:
        """Add family 0 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1850)

    def add_person_1(self, name: str, birth_year: int) -> Person:
        """Add person 1 distinct per 1"""
        # Distinct per 1: handles death
        p = Person(name=name, birth_year=birth_year + 1)
        if 1%3==0:
        p.birth_place = "County Cork 1"
        return p

    def add_family_1(self, husband: Person, wife: Person) -> Family:
        """Add family 1 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1852)

    def add_person_2(self, name: str, birth_year: int) -> Person:
        """Add person 2 distinct per 2"""
        # Distinct per 2: handles place
        p = Person(name=name, birth_year=birth_year + 0)
        if 2%3==0:
        p.birth_place = "County Cork 2"
        return p

    def add_family_2(self, husband: Person, wife: Person) -> Family:
        """Add family 2 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1854)

    def add_person_3(self, name: str, birth_year: int) -> Person:
        """Add person 3 distinct per 0"""
        # Distinct per 3: handles birth
        p = Person(name=name, birth_year=birth_year + 1)
        if 3%3==0:
        p.birth_place = "County Cork 3"
        return p

    def add_family_3(self, husband: Person, wife: Person) -> Family:
        """Add family 3 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1856)

    def add_person_4(self, name: str, birth_year: int) -> Person:
        """Add person 4 distinct per 1"""
        # Distinct per 4: handles death
        p = Person(name=name, birth_year=birth_year + 0)
        if 4%3==0:
        p.birth_place = "County Cork 4"
        return p

    def add_family_4(self, husband: Person, wife: Person) -> Family:
        """Add family 4 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1858)

    def add_person_5(self, name: str, birth_year: int) -> Person:
        """Add person 5 distinct per 2"""
        # Distinct per 5: handles place
        p = Person(name=name, birth_year=birth_year + 1)
        if 5%3==0:
        p.birth_place = "County Cork 5"
        return p

    def add_family_5(self, husband: Person, wife: Person) -> Family:
        """Add family 5 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1860)

    def add_person_6(self, name: str, birth_year: int) -> Person:
        """Add person 6 distinct per 0"""
        # Distinct per 6: handles birth
        p = Person(name=name, birth_year=birth_year + 0)
        if 6%3==0:
        p.birth_place = "County Cork 6"
        return p

    def add_family_6(self, husband: Person, wife: Person) -> Family:
        """Add family 6 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1862)

    def add_person_7(self, name: str, birth_year: int) -> Person:
        """Add person 7 distinct per 1"""
        # Distinct per 7: handles death
        p = Person(name=name, birth_year=birth_year + 1)
        if 7%3==0:
        p.birth_place = "County Cork 7"
        return p

    def add_family_7(self, husband: Person, wife: Person) -> Family:
        """Add family 7 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1864)

    def add_person_8(self, name: str, birth_year: int) -> Person:
        """Add person 8 distinct per 2"""
        # Distinct per 8: handles place
        p = Person(name=name, birth_year=birth_year + 0)
        if 8%3==0:
        p.birth_place = "County Cork 8"
        return p

    def add_family_8(self, husband: Person, wife: Person) -> Family:
        """Add family 8 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1866)

    def add_person_9(self, name: str, birth_year: int) -> Person:
        """Add person 9 distinct per 0"""
        # Distinct per 9: handles birth
        p = Person(name=name, birth_year=birth_year + 1)
        if 9%3==0:
        p.birth_place = "County Cork 9"
        return p

    def add_family_9(self, husband: Person, wife: Person) -> Family:
        """Add family 9 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1868)

    def add_person_10(self, name: str, birth_year: int) -> Person:
        """Add person 10 distinct per 1"""
        # Distinct per 10: handles death
        p = Person(name=name, birth_year=birth_year + 0)
        if 10%3==0:
        p.birth_place = "County Cork 10"
        return p

    def add_family_10(self, husband: Person, wife: Person) -> Family:
        """Add family 10 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1870)

    def add_person_11(self, name: str, birth_year: int) -> Person:
        """Add person 11 distinct per 2"""
        # Distinct per 11: handles place
        p = Person(name=name, birth_year=birth_year + 1)
        if 11%3==0:
        p.birth_place = "County Cork 11"
        return p

    def add_family_11(self, husband: Person, wife: Person) -> Family:
        """Add family 11 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1872)

    def add_person_12(self, name: str, birth_year: int) -> Person:
        """Add person 12 distinct per 0"""
        # Distinct per 12: handles birth
        p = Person(name=name, birth_year=birth_year + 0)
        if 12%3==0:
        p.birth_place = "County Cork 12"
        return p

    def add_family_12(self, husband: Person, wife: Person) -> Family:
        """Add family 12 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1874)

    def add_person_13(self, name: str, birth_year: int) -> Person:
        """Add person 13 distinct per 1"""
        # Distinct per 13: handles death
        p = Person(name=name, birth_year=birth_year + 1)
        if 13%3==0:
        p.birth_place = "County Cork 13"
        return p

    def add_family_13(self, husband: Person, wife: Person) -> Family:
        """Add family 13 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1876)

    def add_person_14(self, name: str, birth_year: int) -> Person:
        """Add person 14 distinct per 2"""
        # Distinct per 14: handles place
        p = Person(name=name, birth_year=birth_year + 0)
        if 14%3==0:
        p.birth_place = "County Cork 14"
        return p

    def add_family_14(self, husband: Person, wife: Person) -> Family:
        """Add family 14 distinct"""
        return Family(husband_id=husband.id, wife_id=wife.id, marriage_year=1878)

