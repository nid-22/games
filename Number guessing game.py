import random 
  
print("Number guessing game")
number = random.randint(1, 9)
turns=1
while turns < 4:
    # Enter a number between 1 to 9  
    guess = int(input("Guess a number between 1 to 9"))
    if guess == number: 
          
        
        print("Congratulation YOU WON!!!") 
        break
          
     
    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 
  
                
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
          
    # Increase the value of chance by 1 
    turns += 1
          
          
# Check whether the user   
# guessed the correct number  
if not turns < 4: 
    print("YOU LOSE!!! The number is", number)
