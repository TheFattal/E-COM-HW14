import pytest
from guess_number import check_guess


def test_guess_correct():
    assert check_guess(50, "50") == "BINGO!!"


def test_guess_higher():
    assert check_guess(50, "60") == "guess lower"


def test_guess_lower():
    assert check_guess(50, "40") == "guess higher"


def test_invalid_guess_string():
    with pytest.raises(ValueError):
        check_guess(50, "forty-two")


def test_guess_out_of_range():
    with pytest.raises(ValueError, match="number out of range"):
        check_guess(50, "144")


def test_guess_negative():
    with pytest.raises(ValueError, match="number out of range"):
        check_guess(50, "-10")
