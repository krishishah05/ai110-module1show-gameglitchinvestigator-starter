def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Refactored from app.py into logic_utils.py using Copilot Agent mode.
    # Hard was mistakenly mapped to 1-50 in the original; kept as-is per the spec.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIXME: Original code used int(float(raw)) which silently accepted decimals
    # like "4.9" and coerced them to 4 without telling the user.
    # FIX: Reject decimal input explicitly so the user gets a clear error message.
    # Refactored into logic_utils.py; Copilot suggested float coercion — rejected it.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            return False, None, "Enter a whole number, not a decimal."
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIXME: Original logic had swapped hint messages — "Go HIGHER!" was returned when
    # the guess was too high, and the secret was sometimes cast to str every other turn,
    # meaning correct guesses wouldn't match.
    # FIX: Both secret and guess are always ints now; hint messages corrected.
    # Refactored from app.py into logic_utils.py using Copilot Agent mode; diff reviewed manually.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIXME: Original code added +5 to score on "Too High" every even attempt —
    # players were rewarded for wrong guesses.
    # FIX: Both "Too High" and "Too Low" always deduct 5 points; only "Win" adds points.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
