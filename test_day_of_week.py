import pytest
from day_of_week import day_of_week


def test_sunday():
    assert day_of_week("1") == "Sunday"


def test_monday():
    assert day_of_week("2") == "Monday"


def test_tuesday():
    assert day_of_week("3") == "Tuesday"


def test_wednesday():
    assert day_of_week("4") == "Wednesday"


def test_thursday():
    assert day_of_week("5") == "Thursday"


def test_friday():
    assert day_of_week("6") == "Friday"


def test_saturday():
    assert day_of_week("7") == "Saturday"


def test_invalid_day():
    with pytest.raises(ValueError, match="Invalid day number"):
        day_of_week("0")

    with pytest.raises(ValueError, match="Invalid day number"):
        day_of_week("8")

    with pytest.raises(ValueError, match="Invalid input: not a number"):
        day_of_week("not-num")
