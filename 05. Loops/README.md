#  Number Guessing Game (Loops Portfolio Project)

##  Project Overview
This is a console-based **Number Guessing Game** built to demonstrate mastery of **loops, conditionals, and user input handling** in Python. It's the capstone project for the "Loops" topic in my AI Engineer roadmap (Phase 1: Python Foundations).

The program picks a random number and challenges the user to guess it within a limited number of attempts, with feedback ("Too High"/"Too Low") after every guess. It also includes difficulty levels and a replay option.

##  Features
- Random number generation using the `random` module
- Difficulty selection (**Easy** 1–50, **Medium** 1–100, **Hard** 1–200)
- Limited attempts (10 max) with live attempt counter
- Input validation using `try/except` (handles non-numeric input gracefully)
- "Too High" / "Too Low" / "Correct!" feedback loop
- Win/loss detection using a `while...else` loop (loop-`else` runs only if attempts run out without guessing correctly)
- Replay option (`play again?`) using an outer `while True` loop with a `break` condition

##  Concepts Practiced
| Concept | Where it's used |
|---|---|
| `while` loops | Main guessing loop, outer replay loop |
| `for` / `range()` | (learned earlier in this topic, applied conceptually to attempt counting) |
| `break` | Exiting the guessing loop on a correct guess; exiting replay loop on "no" |
| `continue` | (understood from quiz; not directly needed here) |
| loop `else` | Detecting "ran out of attempts" without a manual flag variable |
| Conditionals (`if`/`elif`/`else`) | Difficulty selection, guess comparison |
| Exception handling (`try`/`except`) | Preventing crashes on invalid input |
| f-strings | Clean, readable dynamic output |

##  File
- `13.project.py` — full source code for the game

##  How to Run
```bash
python 13.project.py
```

##  Learning Outcomes
- Understood the practical difference between `while` and `for` loops, and when to choose each
- Learned how loop-`else` avoids the need for a manual "found/not found" flag variable
- Practiced defensive coding with `try/except` to prevent crashes from bad user input
- Built a full interactive program combining nested loops, conditionals, and state (attempts, score) that persists across a game round

##  GitHub Upload Instructions
1. Open **GitHub Desktop**
2. Confirm the repo is `Python-Practice` and the current branch is `main`
3. Make sure `13.project.py` (and this `README.md`) are inside the `05. Loops` folder
4. In GitHub Desktop, you should see the new files listed under "Changes"
5. Write a commit message, e.g.:
   ```
   Add: Number Guessing Game project + README for Loops topic
   ```
6. Click **Commit to main**
7. Click **Push origin** to upload to GitHub
8. Verify on github.com/Kiran-Sarwar/Python-Practice that the files appear in `05. Loops`