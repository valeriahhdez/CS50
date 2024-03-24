from jar import Jar
import pytest


def test_init_negative_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


    # Deposit a positive integer n, where n is less than or equal to the jar's remaining capacity
def test_deposit_positive_integer_less_than_capacity():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    # Deposit a positive integer n, where n is greater than the jar's remaining capacity
def test_deposit_positive_integer_greater_than_capacity():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)
    
    # withdraws cookies when there are enough in the jar
def test_withdraw_with_enough_cookies():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

    # raises ValueError when n is negative
def test_withdraw_with_negative_n():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-5)