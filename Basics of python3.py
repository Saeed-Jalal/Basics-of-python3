#For Loop
import random
n = 20
toBeGussed = int(n * random.random())+1 #This is a code to genrate the random "toBeGussed" number.
guess = 0
while guess != toBeGussed:
    guess =  int(input("Please enter the New number: "))
    if guess > 0:
        if guess > toBeGussed:
            print("Your number is too high.")
        elif guess < toBeGussed:
            print("Your number is too low.")
    else:
        print("Sorry.")
        break
else:
    print("Congrats, You are genius.")

#For Loop
Clothes = ["Jeans","Shirts","T-Shirts","Jackets"]
for cloth in Clothes:
    print("My collection is: ",cloth)
print("This is my normal clothes collection.")

numbers = (1,5)
for i in (numbers):
    print("My number: ",i)
print("Thats it.")
#Practice
num = int(input("Enter the Number:"))
factorial = 1

if num < 0:
    print("it has to be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i

print("This is the factorila number as a answer:",factorial)

#Practice 2
import random
guessesTaken = 0
print('Hello, What is your name? ')
myName = input()
number = random.randint(1,20)
print("Mr."+myName+", I am thinking about a number between -> 1,20.")
while guessesTaken < 6:
    print("Take a guess. ")
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess< number:
        print('Your guess is too low.')
    if guess> number:
        print('Your guess is too high')
    if guess == number:
        break
print("Mr. " + myName + "! Well done you are genius.")







