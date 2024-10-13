# Snake_water_Gun-Game
here we created a game called **sanke** **water** **gun** this is similar to the game **rock** **paper** **scissors** you can also use this logic to use this to play rock paper scissors also I will mention that in the coad

this code is written in two logics one is using integer and another is using the names

Here’s an explanation of both programs, highlighting the differences in their logic:

### Program 1:
1. **Logic:**
   - The user selects their choice by typing `"Snake"`, `"Water"`, or `"Gun"` via an input string. The computer randomly chooses one of these options.
   - The `check()` function compares the choices between the user and the computer:
     - If they choose the same option, it returns `0` (draw).
     - If the computer's choice defeats the user's, it returns `-1` (user loses).
     - Otherwise, it returns `1` (user wins).
   
2. **Input Method:** 
   - The user enters a string (`"Snake"`, `"Water"`, or `"Gun"`), and the choices are compared using strings.
   
3. **Random Choice:**
   - The computer uses `random.choice()` to randomly select from a list of strings `["Snake", "Gun", "Water"]`.

---

### Program 2:
1. **Logic:**
   - In this version, the user inputs a number (`0`, `1`, or `2`) corresponding to "Snake," "Water," or "Gun". The computer randomly generates a number between `0` and `2`.
   - The `check()` function uses numbers to compare the choices:
     - `0` represents "Snake", `1` represents "Water", and `2` represents "Gun".
     - As in the first program, the function returns `0` for a draw, `-1` for a loss, and `1` for a win.

2. **Input Method:** 
   - The user enters an integer (`0`, `1`, or `2`) instead of a string. The game logic is based on these integer values.

3. **Random Choice:**
   - The computer uses `random.randint(0, 2)` to generate its choice as a number.

---

### Key Differences:
1. **Input Type:**
   - The first program uses strings (`"Snake"`, `"Water"`, `"Gun"`) for both user input and computer choices.
   - The second program uses integers (`0`, `1`, `2`), with each number representing one of the options.

2. **Random Choice Mechanism:**
   - The first program uses `random.choice()` to select from a list of strings.
   - The second program uses `random.randint(0, 2)` to generate a number representing the options.

3. **Comparison Logic:**
   - In the first program, the comparison is done between strings (e.g., `"Snake" == "Water"`).
   - In the second program, comparisons are based on integers (`0 == 1`).

Both programs achieve the same result, but the second one uses numerical logic, which is often faster and more compact, while the first uses more human-readable string comparisons.
