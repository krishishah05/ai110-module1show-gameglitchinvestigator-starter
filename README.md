# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the fixed app: `python -m streamlit run app.py`
3. Run the tests: `pytest`

## 🕵️‍♀️ Your Mission (Completed)

1. **Played the game.** Used the "Developer Debug Info" panel to observe the secret number changing on every submit — confirmed the state bug.
2. **Found and fixed the State Bug.** The secret was regenerated on every Streamlit rerun because it wasn't guarded by `st.session_state`. Fixed with `if "secret" not in st.session_state`.
3. **Fixed the Logic.** The hint messages were swapped — `guess > secret` returned "Go HIGHER!" instead of "Go LOWER!". Fixed in `logic_utils.py`.
4. **Refactored & Tested.** All four functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) moved from `app.py` into `logic_utils.py`. All 11 pytest cases pass.

## 📝 Document Your Experience

**Game purpose:** A number-guessing game where the player picks a difficulty and tries to guess a secret number within a limited number of attempts, earning or losing points based on their guesses.

**Bugs found:**
1. Secret number re-randomised on every Streamlit rerun (not stored in session_state).
2. Hint messages were backwards — "Go HIGHER!" when guess was too high, "Go LOWER!" when too low.
3. Score rewarded the player +5 on "Too High" guesses every even attempt.
4. Decimal input (e.g. "4.9") was silently coerced to an int instead of showing an error.
5. `attempts` was initialised to 1, consuming the first attempt before any guess was made.

**Fixes applied:**
- Wrapped secret generation in `st.session_state` guard.
- Corrected comparison logic and messages in `check_guess`.
- Unified score deduction for all wrong guesses in `update_score`.
- Strict decimal rejection added to `parse_guess`.
- Reset `attempts` initialisation to 0.
- Refactored all game logic into `logic_utils.py`.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
