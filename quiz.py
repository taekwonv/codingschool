print("Welcome to QuizQuiz!")
input("Press Enter to start...")

import os
os.system("cls")

score = 0

print("Which is the largest of all sharks?")
print("a. Great white shark")
print("b. Whale shark")
print("c. Bull shark")
print("d. Tiger shark")
answer = input("Your answer: ")

if answer == "b":
	print("Correct!")
	score = score + 50
else:
	print("The largest of all sharks is Whale shark!")

print("")
print("All of the blood in your body travels through your heart once a minute")
answer = input("True or False?")
print("")
if answer.lower() == "true":
	print("Correct!")
	score = score + 50
else:
	print("Nice try! But it is True!")

print("What is the name of Thomas?")
print("a. Tomas")
print("b. Uhhuh?")
print("c. LLL")
print("d. Tiger")
answer = input("Your answer: ")

if answer == "d":
	print("Correct!")
	score = score + 1000
else:
	print("The largest of all sharks is Whale shark!")

print("")
print("==============================")
print("Your score is " + str(score))
print("Good job!")
print("See you next time!")
