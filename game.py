#this program demonstrates a guessing game
from random import randint
#get user input
user=input("Enter username:")
print("Hello there, " + user + "!")

#generate  a random number
number=randint(15,30)

counter=0
while counter <5:
    userno=eval(input("Enter a random  number:"))
    counter += 1 #same as counter=counter+1

    if userno < number :
        print("Sorry, your guess is too low.")

    elif userno  > number :
        print("Sorry , your guess is too high.")
    elif userno  == number:
        break
     
             

print("Game over.")


if userno==number:
    print("Congrats! You won!")
else:
    print("Sorry, The correct number was " ) 
    print(number)   











#using a while loop
#get user number
#generate a random number
#check if user  input is equal to generated number