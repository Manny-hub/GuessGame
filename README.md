# 🎯 Guess the Number - Python Game

A simple, interactive number guessing game built with Python. The program randomly selects a number between 1 and 20, and the player has **6 chances** to guess it correctly.

## 💡 How it Works

- The program generates a random number between 1 and 20.
- You have **6 attempts** to guess the correct number.
- After each guess, the program gives feedback:
  - "Too low..." if your guess is smaller than the secret number.
  - "Try something lower..." if your guess is higher than the number.
  - If correct, it congratulates you and shows how many guesses it took.
- If you fail to guess correctly after 6 attempts, the program reveals the correct number.

## 🧠 Technologies Used

- Python 3
- `random` module

## 🚀 How to Run

1. Make sure you have Python installed on your computer.
2. Clone this repository or copy the code to your local machine.
3. Open your terminal and navigate to the script location.
4. Run the script:

```bash
python guessgame.py

I am thinking of a number between 1 and 20
Take a guess... 10
Give it another try, your guess is too low...
Take a guess... 15
Hey, you are almost there. Try something lower...
Take a guess... 13
Bravo.. You guessed my number in 3

