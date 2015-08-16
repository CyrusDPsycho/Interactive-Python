# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

#Convert name to number
def name_to_number(name):
    if name == 'rock':
        num = 0
    elif name == 'Spock':
        num = 1
    elif name == 'paper':
        num = 2
    elif name == 'lizard':
        num = 3
    elif name == 'scissors':
        num = 4
    else:
        
        print ("Invalid option")
    
    return num

#Convert number to name
def number_to_name(num):
    if num == 0:
        name = "rock"
    elif num == 1:
        name = "Spock"
    elif num == 2:
        name = "paper"
    elif num == 3:
        name = "lizard"
    elif num == 4:
        name = "scissors"
    else:
        
        print "Invalid number"
        
    return name
    
#Computing the winner
def rpsls(player_choice):
    print ""
    print "Player Chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer Chooses", comp_choice
    
    #Conditions to find the winner using modulo 5
    if player_number == comp_number:
        print "   Player and Computer - TIE!!  "
        return
    
    if (comp_number + 1) % 5 == player_number:
        print "   Player wins!!"
        
    elif (comp_number + 2) % 5 == player_number:
        print "   Player wins!!"
        
    else:
        print "   Computer Wins!! "

    
#TestCode
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

