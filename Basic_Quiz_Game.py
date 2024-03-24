print("Welcome to the Python basic quiz! ")

playing =input("Are you ready to test your skills and have some fun? ")

if playing.lower() != "yes":
    quit()

print("Let's get started! ")
score =0

answer = input("How do you calculate the square root of a number in Python? ")
if answer.lower() == "sqrt()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the exponentiation operator in Python? ")
if answer.lower() == "**":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How can you generate a random number between 0 and 1 in Python? ")
if answer.lower() == "random.random()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What module do you need to import to use mathematical functions like sin(), cos(), and tan() in Python? ")
if answer.lower() == "math":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 

print("You're doing great! Let's see if you can tackle the next one.")

answer = input("What is the result of 5 / 2 in Python 3? ")
if answer.lower() == "2.5":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 


answer = input("How can you round a floating-point number to the nearest integer in Python? ")
if answer.lower() == "round()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 

answer = input("What function can you use to find the maximum value in a list in Python? ")
if answer.lower() == "max()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 

print("Here comes the final challenge! Give it your best shot. 🎯")

answer = input("How do you calculate the factorial of a number in Python? ")
if answer.lower() == "math.factorial()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")
