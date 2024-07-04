# Password Strength Checker

Overview
This Python script evaluates the strength of passwords based on various criteria such as length, character types, and commonality.

Features
- Checks for common passwords from a list.
- Evaluates password strength based on:
  - Length
  - Uppercase and lowercase letters
  - Special characters
  - Numeric digits
- Provides a score out of 7 indicating password strength.

Requirements
- Python 3.12
- `passwords.txt` file containing a list of 100 common passwords (one per line)

Usage
1. Clone the repository or download the script.
2. Ensure Python is installed on your system.
3. Create or edit the `passwords.txt` file with common passwords.
4. Run the script:
   python password_strength_checker.py

Input the password you want to evaluate when prompted.
Example
Enter the password: HelloBro1045!123
Password length is 16, adding 4 points.
Password has 4 different character types, adding 3 points.
Password strength is good. Strength Score is: 7 / 7
Notes
Ensure passwords.txt is updated regularly with common passwords.
Adjust scoring criteria in the script as per your requirements.
view license
