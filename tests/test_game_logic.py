from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Additional tests for parse_guess edge cases
def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_decimal_rejected():
    ok, value, err = parse_guess("4.9")
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False

# Additional tests for update_score
def test_update_score_win():
    score = update_score(0, "Win", 1)
    assert score > 0

def test_update_score_too_high_deducts():
    score = update_score(20, "Too High", 2)
    assert score == 15

def test_update_score_too_low_deducts():
    score = update_score(20, "Too Low", 3)
    assert score == 15


# Additional tests for parse_guess edge cases
def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_decimal_rejected():
    ok, value, err = parse_guess("4.9")
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False

# Additional tests for update_score
def test_update_score_win():
    score = update_score(0, "Win", 1)
    assert score > 0

def test_update_score_too_high_deducts():
    score = update_score(20, "Too High", 2)
    assert score == 15

def test_update_score_too_low_deducts():
    score = update_score(20, "Too Low", 3)
    assert score == 15

