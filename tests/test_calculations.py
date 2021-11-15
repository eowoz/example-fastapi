from app.calculations import add , subtract, multiply, divide , BankAccount, InsufficientFunds
import pytest


@pytest.fixture
def zero_bank_account():
    print("Inside zero bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3 , 2, 5), 
    (7 , 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(9, 4) == 36

def test_divide():
    assert divide(8, 4) == 2


def test_bank_set_initial_amount(bank_account):
    #bank_account = BankAccount(50)
    #assert bank_account.balance == 50
    assert bank_account.balance == 50


def test_bank_default_amount(zero_bank_account):
    #bank_account = BankAccount()
    #assert bank_account.balance == 0
    print("testing")
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    #bank_account = BankAccount(50) 
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    #bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    #bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (100 , 50, 50), 
    (200 , 100, 100),
    (175, 4, 171),
])
def test_bank_transcations(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    #with pytest.raises(Exception):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
