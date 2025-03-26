This Python program generates secure, random passwords by combining words, numbers, and special characters. 
It uses the passwordmeter library to evaluate the strength of the generated password. 
The program automatically downloads a word list from GitHub if it doesn't already exist, ensuring fresh and varied password generation.

Features
Random Password Generation: Combines capitalized words, random digits, and special characters.
Strength Evaluation: Uses passwordmeter to assess password complexity.
Dynamic Word List: Downloads and caches a large word list (~370K English words) for variety.
Error Handling: Automatically verifies the integrity of the word list and gracefully handles errors.

Usage
1. Install dependencies: pip install passwordmeter
2. Run the program: python3 main.py
3. Example output: Password: RunningMonkey9245! Strength: 0.87500

This tool is ideal for generating strong, memorable passwords with a balance of readability and security.
