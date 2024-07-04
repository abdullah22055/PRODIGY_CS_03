import string

password = input("Enter the password: ")

#List Cmprehension for different character types
uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

char = [uppercase, lowercase, special, digits]
length = len(password)
score = 0

#for common passwords
with open('passwords.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password is very common. Score: 0 / 7")
    exit()

#scores for length
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1
print(f"Password length is {str(length)}, adding {str(score)} points.")

#scores for char
if sum(char) > 1:
    score += 1
if sum(char) > 2:
    score += 1
if sum(char) > 3:
    score += 1

print(f"Password has {str(sum(char))} different character types, adding {str(sum(char) - 1)} points.")

# Final score and strength message
if score < 4:
    print(f"Password strength is weak. Strength Score is: {str(score)} / 7")
elif score == 4:
    print(f"Password strength is mediocre. Strength Score is: {str(score)} / 7")
elif score > 4 and score < 6:
    print(f"Password strength is good. Strength Score is: {str(score)} / 7")
elif score >= 6:
    print(f"Password strength is strong. Strength Score is: {str(score)} / 7")
