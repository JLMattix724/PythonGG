'''
Created on Nov 3, 2017

@author: Justin Mattix
Python Guessing Game

'''

def main():
    #getting the user input for the range of the random number
    print("Enter a number to guess between ")
    #making the variable n available to Loop
    global n 
    n = int(input())
    print ("I have a number between 1 - " + str(n) + " can you guess it? Enter your Guess. ")
    Loop()
#The loop for the guesses
def Loop():
    count = 1
    #generating the random number
    from random import randint
    RandomNum = randint(1,n)
    guess = False
    while not guess:
        GuessNum = int(input())
        if GuessNum > RandomNum:
            print("Too high")
            #calling the insult function to print an insult
            print (Insults())
            #incrementing the count
            count += 1
        if GuessNum < RandomNum:
            print("Too Low")
            #calling the insult function to print an insult
            print (Insults())
            #incrementing the count
            count += 1
        elif GuessNum == RandomNum:
            print("You got it! Thanks for Playing")
            print("This took you " + str(count) + " times to guess the number.")
            #breaking the loop
            guess = True
            #calling the restart function
            Restart()
            
def Insults():
    from random import randint
    #generating a random number for the insults
    Randominsult = randint(1,10)
    #if statements for the insults that return insults to be printed by the Loop()
    if Randominsult == 1:
        return "A child could do better!"
    if Randominsult == 2:
        return "So close... but close is only good for horseshoes and hand grenades"
    if Randominsult == 3:
        return "Wow... you sure you know what you're doing?"
    if Randominsult == 4:
        return "This might take a while..."
    if Randominsult == 5:
        return "Do you need a hint?"
    if Randominsult == 6:
        return "In Soviet Russia number guess you..."
    if Randominsult == 7:
        return "In an alternate timeline you may have been right"
    if Randominsult == 8:
        return "Did you just discover fire or something?"
    if Randominsult == 9:
        return "How are you taking so long?"
    if Randominsult == 10:
        return "Just quit already"
#For restarting or quitting the program
def Restart():
    #user input
    restart = input("Would you like to play again? Y/N \n")
    #restart condition
    if restart == 'Y':
        main()
    #quit condition
    if restart == 'N':
        print("Goodbye")
        quit()
if __name__ == '__main__':
        main()
    
        
    