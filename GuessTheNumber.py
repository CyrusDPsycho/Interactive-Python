#template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simpleguitk as simplegui
import random 
import math

# initialize global variables used in your code here

secret_number = 0
number_range = 100
turns_left = 0


# helper function to start and restart the game
def new_game():
    
    
    global secret_number  
    global turns_left 
    global number_range 
    
    secret_number = random.randrange(0,number_range)
    if number_range == 100 : 	
        turns_left = 7
    elif number_range == 1000 :
        turns_left = 10
    
    print("")
    print("Guess the Number - New Game")
    print ("------------")
    print("This game ranges from 0 to",number_range)
    print("The number of guesses left are",turns_left,"\n")
    
    
    
# define event handlers for control panel
def range100():
    global number_range
    number_range = 100
    new_game()

def range1000():
    global number_range
    number_range = 1000
    new_game()
   
    
def input_guess(guess):
    global secret_number                          
    global turns_left
    global number_range

    print("")
    print ("Your guess was", guess)
    
    #Error Handling
    try:
        
        if int(guess)> number_range: 
           
            print ("Number out of range!")
            print ("Please enter a number within the range of 0 to",number_range,"\n")
            return
        
    except:
        print ("Invalid Entry ")
        print ("Please enter a valid number: \n")
        return
        
    #Computation
    turns_left = turns_left - 1
    print ("Guesses Left: ",turns_left)
    

    if int(guess) > secret_number:
        print ("Lower!")
        
    elif int(guess) < secret_number:
        print ("Higher!")
                                         
    elif int(guess) == secret_number:
        print ("Correct! You Win!\n")
        new_game()
        return
    
    if turns_left == 0:
        print ("\nSorry. You did not guess in time. You lose!\n")
        print ("The answer was",secret_number,"!")
        print ("------------")
        new_game()
        return
    
              
def restart_game():
    print("Restarting Game....")
    timer.start()
    
def timer_man():
    
    print(" \n\tLet's Play! ")
    timer.stop()
    new_game()

    

#Frame Definition    
frame = simplegui.create_frame("Guess The Number!", 250,250)
frame.set_canvas_background('Blue')
timer = simplegui.create_timer(1500,timer_man)

# register event handlers for control elements and start frame
frame.start()
frame.add_input("Enter the number", input_guess, 200)
frame.add_button("Change to range(0-1000)", range1000, 200)
frame.add_button("Change to range(0-100)", range100,200)
frame.add_button("Restart this game", restart_game,200)

# call new_game 
new_game()
