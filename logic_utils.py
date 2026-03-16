def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100
#FIX: Refactored logic into logic_utils.py using Copilot Agent mode

def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns:
        (ok: bool, guess_int: int | None, error_message: str | None)
    """

    raw = raw.strip()

    if raw == "":
        return False, None, "Please enter a number."

    try:
        guess = int(raw)
        return True, guess, None
    except ValueError:
        return False, None, "Please enter a valid number."
#FIX: Refactored logic into logic_utils.py using Copilot Agent mode

def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"
#FIX: Refactored logic into logic_utils.py using Copilot Agent mode

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
