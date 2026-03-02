# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the app, the secret number changed on every single button click, making it impossible to ever win — even if I guessed the exact number I could see in the debug panel. The hint messages were also backwards: when my guess was too high the app said "Go HIGHER!" and when it was too low it said "Go LOWER!", which made the game actively misleading. On top of that, the score was bugged — every even-numbered "Too High" guess rewarded the player +5 points instead of penalising them, so the score was meaningless. Finally, typing a decimal like "4.9" was silently accepted and coerced to "4" without any error shown to the user.

---

## 2. How did you use AI as a teammate?

I used VS Code Copilot (Agent Mode and Inline Chat) throughout Phase 2. For the hint-fix, I highlighted the `check_guess` function and asked Copilot via Inline Chat to "explain this logic step-by-step" — it correctly identified that the messages were swapped (`"Go HIGHER!"` paired with `guess > secret`) and suggested the right fix, which I verified by running the three starter pytest cases. For the decimal-input issue, Copilot suggested using `int(float(raw))` to handle mixed input — I rejected that because it would still silently swallow decimals; I instead enforced a strict `"." in raw` check that returns a clear error message, which I confirmed with a manual test in the running app.

---

## 3. Debugging and testing your fixes

For every fix I first added a `# FIXME` comment at the bug site, then used Copilot Agent Mode to plan and apply the change, and then carefully reviewed the diff before accepting it. I ran `pytest` after each change to confirm the three starter tests still passed and that my new tests also passed (11 tests total). I also ran the live Streamlit app after each fix to manually verify the behaviour: I used the Developer Debug Info panel to confirm the secret stayed stable across submissions, checked that "Too High" and "Too Low" hints now matched the actual comparison, and verified the score only decreased on wrong guesses.

---

## 4. What did you learn about Streamlit and state?

In the original app, `random.randint(low, high)` was called at the top of the script with no session_state guard, so every time Streamlit re-ran the script (which happens on every interaction) the secret was regenerated. I fixed this by wrapping it in `if "secret" not in st.session_state`, which tells Streamlit to only assign the value once per session. The key insight is that Streamlit re-executes the entire Python file from top to bottom on every user interaction — it does not remember variables between runs unless you store them in `st.session_state`. I would explain it to a friend like this: "Imagine your code is a whiteboard that gets erased and redrawn every time you press a button — `session_state` is a sticky note on the side that survives the erase."

---

## 5. Looking ahead: your developer habits

The habit I want to keep is adding `# FIXME` comments before touching any code — it forced me to think clearly about _what_ was wrong before jumping into a fix, which made my Copilot prompts much more specific and useful. Next time I work with AI on a task I would ask it to explain _why_ the fix works, not just what to change, because the decimal coercion suggestion slipped past me until I actually traced through the logic manually. This project changed how I think about AI code: it is a fast first draft, not a finished product — and the bugs it introduces are often subtle logic errors that look plausible at first glance, which is exactly why testing and human review are non-negotiable.

