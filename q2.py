# A Python program for the Rock, Paper, Scissors game. 
import random

def rock_paper_scissors():
    ''' Write your code for playing Rock Paper Scissors here. '''
    print()
    points = int(input('How many points does it take to win? '))
    options = ['rock', 'paper', 'scissors']
    count = 1
    user_score = 0
    computer_score = 0
    
    while ((user_score < points) and (computer_score < points)):
        print()
        print('********************* ROUND', '#'+str(count), '*********************')
        print()
        user_choice = input('Pick your throw: [r]ock, [p]aper, or [s]cissors? ')
        computer_choice = random.choice(options)
        
        while ((user_choice == 'r' and computer_choice == 'rock') or (user_choice == 'p' and computer_choice == 'paper') or (user_choice == 's' and computer_choice == 'scissors')):
            print('Tie!')
            print()
            user_choice = input('Pick your throw: [r]ock, [p]aper, [s]cissors? ')
            computer_choice = random.choice(options)
            
        if ((user_choice == 'r' and computer_choice == 'scissors') or (user_choice == 'p' and computer_choice == 'rock') or (user_choice == 's' and computer_choice == 'paper')) :
            print('Computer threw', computer_choice+',', 'you win!')
            user_score = user_score + 1
            
        elif ((user_choice == 'r' and computer_choice == 'paper') or (user_choice == 'p' and computer_choice == 'scissors') or (user_choice == 's' and computer_choice == 'rock')):
            print('Computer threw', computer_choice+',', 'you lose!')
            computer_score = computer_score + 1
            
        count = count + 1
        print()
        print('Your score:', user_score)
        print("Computer's score:", computer_score)
        
    print()
    print('********************* GAME OVER ********************')
    print() 
    
    if user_score > computer_score:
        print('You win!')
        
    elif computer_score > user_score:
        print('Computer wins!')

def main(): 
    print('ROCK PAPER SCISSORS in Python')
    print()
    print('Rules: 1) Rock wins over Scissors.')
    print('       2) Scissors wins over Paper.')
    print('       3) Paper wins over Rock.')
    
    rock_paper_scissors()
    
main()
