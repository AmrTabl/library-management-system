import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import csv
import pytest
from models.user import User
from models.borrow_record import BorrowRecord




TEST_USERS = "data/test_users.csv"
TEST_BORROW = "data/test_borrow.csv"


@pytest.fixture(autouse=True)
def setup_and_cleanup():
    User.file = TEST_USERS
    BorrowRecord.file = TEST_BORROW

    with open(TEST_USERS, "w", newline=""):
        pass

    with open(TEST_BORROW, "w", newline=""):
        pass

    yield

    if os.path.exists(TEST_USERS):
        os.remove(TEST_USERS)
    if os.path.exists(TEST_BORROW):
        os.remove(TEST_BORROW)



def test_user_register():
    User.register("Test User", "test@mail.com", "1234", "student")
    users = User.get_all()
    assert len(users) == 1
    assert users[0].email == "test@mail.com"



def test_user_validate():
    User.register("Admin", "admin@mail.com", "admin", "admin")
    user = User.validate("admin@mail.com", "admin")
    assert user is not None
    assert user.role == "admin"



def test_borrow_create():
    BorrowRecord.create("1", "10")
    records = BorrowRecord.get_all()
    assert len(records) == 1
    assert records[0].studentID == "1"



def test_get_by_student():
    BorrowRecord.create("1", "10")
    BorrowRecord.create("2", "11")
    BorrowRecord.create("1", "12")

    records = BorrowRecord.get_by_student("1")
    assert len(records) == 2
