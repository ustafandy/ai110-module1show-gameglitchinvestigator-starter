import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logic_utils import check_guess, get_range_for_difficulty


def test_check_guess_returns_hint_message():
    message = check_guess(40, 50)
    assert isinstance(message, str) and len(message) > 0
    #FIX: Created this function using Agent AI 
    
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_easy_range_is_1_to_20():
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20)
#FIX: Created this function using Agent AI 