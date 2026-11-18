print("Welcome to my Cloud & Tech Quiz!")
score = 0

answer1 = input("1. What does AWS stand for? ")
if answer1.lower() == "amazon web services":
    print("Correct!")
    score += 1
else:
    print("Oops! It is Amazon Web Services.")

answer2 = input("2. Is Linux an operating system? (yes/no) ")
if answer2.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Oops! Yes, it is.")

answer3 = input("3. Which tool is used to save and share code versions? ")
if answer3.lower() == "git" or answer3.lower() == "github":
    print("Correct!")
    score += 1
else:
    print("Oops! The answer is Git or GitHub.")

print(f"Game Over! You scored {score} out of 3.")
